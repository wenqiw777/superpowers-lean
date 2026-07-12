# Superpowers Lean

A lean rewrite of [Superpowers](https://github.com/obra/superpowers) for **Claude Code** and **OpenAI Codex**: four high-level protocol skills plus one goal entry — **254 lines total** — replacing 14 router-enforced skills (3,322 lines).

## Why this exists

The original Superpowers is excellent at enforcing discipline, but it pays for it in context and ceremony:

- A SessionStart router injects ~60 lines into **every** session and mandates a skill check before **any** response — including one-line copy changes.
- 14 skills invoke each other, so loading one protocol tends to pull in several more.
- Process rules, domain knowledge, and personal preferences are all baked into the same skill bodies, so you cannot tune one layer without forking everything.

On strong models the discipline is worth keeping, but the delivery mechanism is not: a capable model does not need 300 lines re-teaching TDD — it needs the entry condition, the stage order, the completion bar, and the decision points. Everything else it either already knows or should read at runtime from *your* configuration.

Superpowers Lean keeps the quality bars (test-first, verification evidence, review loops, authorization gates) at roughly 8% of the runtime footprint, portable across two harnesses.

## Scope — who this is for, and who it is not for

**Good fit:**

- You run a frontier-class model (this was benchmarked on Claude Opus and authored against Claude Fable / Codex). The design bet is that the model already knows the domain content and only needs protocol.
- You maintain your own runtime layers: a short user-level guidance file (hard personal rules), a memory/notes system (environment facts), and per-task plan documents. The skills deliberately delegate specifics to those layers.
- You work across Claude Code and Codex and want one protocol set on both.

**Poor fit:**

- Smaller or older models that benefit from verbose, tutorial-style skills — use the original Superpowers.
- You want batteries-included domain checklists (SQL safety catalogs, framework-specific rules). Lean's rubric names check categories in one line each; deep domain content belongs in dedicated domain skills or your own references.
- You expect to use `guidance/*.md` as-is. Those files are the author's **personal layer** (model policy, verification ladder, working-style rules) and are meant to be replaced with yours; a drift test keeps the shared rules identical across the two surfaces.

## Design

Three rules drive everything:

1. **Skills carry protocol only** — entry conditions, stage order, completion conditions, decision points. A concrete command, path, account, or format template inside a skill is in the wrong layer.
2. **Specifics inject at runtime** — from user-level guidance (personal hard rules), memory (environment/project facts), the plan/ticket document (this task's steps and acceptance), and two on-demand references.
3. **The plan document is the only progress state** — task checkboxes, verification evidence, finding dispositions. Resume after interruption = re-read the plan. No side-car state machine.

Per-session default injection is budgeted and gated: SessionStart hook ≤10 lines (ships one), rendered guidance block ≤25 lines.

## Skills

| Skill | Protocol |
| --- | --- |
| `design-change` | Turn an ambiguous request into an implementation-ready plan; surface material decisions as plain-language numbered options; readiness review loops until no blocker remains. |
| `execute-change` | Implement an approved plan through small verifiable tasks; test-first with recorded red→green evidence; per-step review; progress written back into the plan. |
| `diagnose` | Evidence-backed root-cause investigation that changes nothing; the report (cause, impact, minimal repair option, verification) is the deliverable; repair waits for authorization. |
| `review-and-finish` | Four review profiles (readiness / per-step / bug-only / finish); findings need evidence and severity; non-blocking dispositions are the user's call; delivery actions gate on explicit authorization. |
| `goal` | Entry point: route unready input to design, ready input to execution, verify by deliverable type, finish authorized; resumes from plan-document progress. |

On Claude Code the entry is `/goal <plan-or-ticket> [--ship] [--team-update]` (`commands/goal.md`); on Codex it is the namespaced `goal` plugin skill.

## Surfaces

- **Claude Code adapter:** `commands/`, a one-line SessionStart hook, `guidance/claude.md` rendered into `~/.claude/CLAUDE.md`.
- **Codex adapter:** `.codex-plugin/plugin.json` + the same `skills/`, `guidance/codex.md` rendered into `~/.codex/AGENTS.md`.
- `scripts/render_guidance.py` owns exactly one marked block (`<!-- superpowers-lean:start/end -->`) in each target file, preserves everything outside it, and refuses corrupted or duplicated markers.
- `scripts/check_budgets.py` gates the budgets: skills 250–320 lines total, references ≤120 lines each, guidance block ≤25 lines, hook output ≤10 lines.

## Benchmark

A 20-agent benchmark (Claude Opus runners, independent judges that verify artifacts rather than trust claims):

- **Trigger selection: 11/12** — six scenarios, each run against a clean catalog and a catalog with five competing third-party skills. The one loss was a merge-gate request captured by a similarly named third-party review skill.
- **Protocol compliance: 4/4** — diagnose changed zero files (judge diffed); ambiguous design produced numbered decisions with recommendations and no code; bug-only review reported the planted off-by-one and none of the four style baits; execution ran genuine red→green with the judge independently re-running the suite.

## Tests

```sh
python3 -m unittest discover -s tests
python3 scripts/check_budgets.py
```

## License

MIT. Rewritten from scratch; concept and several protocol ideas trace to [obra/superpowers](https://github.com/obra/superpowers).

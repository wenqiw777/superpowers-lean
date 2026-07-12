---
name: execute-change
description: Implement an approved plan through small, verifiable tasks. Use when scope and acceptance criteria are implementation-ready; do not use for unresolved design decisions.
---

# Execute Change

## Entry

Use only with an implementation-ready plan or an explicitly bounded task.

## Protocol

1. Confirm the current task, its acceptance evidence, and its dependency state.
2. Choose sequential work or independently verifiable delegation according to runtime guidance.
3. For behavior changes with a stable automated check, make the check fail before the minimal implementation and preserve the resulting evidence. Apply documented exceptions only when they fit.
4. Implement the smallest change that meets the task acceptance criteria.
5. Run task-appropriate verification, then request the configured per-step review.
6. Resolve release-blocking findings and re-review. Record completion, evidence, and every non-blocking disposition in the plan document.
7. Route material plan drift to the configured drift handler before continuing.

## Task Boundaries

Keep one task focused on one observable behavior or one inseparable safety change. Fold setup, documentation, and configuration into the task that needs them. Split a task when a reviewer could reasonably accept one part and reject another.

Do not turn each command, file, or test assertion into its own task. The unit of progress is an independently verifiable result.

## Verification Discipline

- Use the verification method named by the plan and runtime guidance.
- Treat a failed check as evidence to investigate, not a reason to weaken the check.
- Do not claim a result from stale output, a different branch, or a partial command.
- Preserve enough evidence in the plan for a later session to understand what passed and why.

## Review Outcomes

- Fix confirmed release blockers before the task is complete.
- If a finding is disproven, record the evidence rather than silently discarding it.
- If a non-blocking finding needs a user decision, surface it before delivery rather than choosing on the user's behalf.
- Do not expand the task to solve unrelated findings unless the user authorizes that scope.

## Recovery

On a resumed session, read the task checkbox, evidence, and open dispositions before acting. Re-run only the minimal verification needed to establish whether the recorded state is still valid.

## Decision Points

Ask the user when scope, product behavior, or authorization changes materially. Do not infer shipping, external writes, or broader cleanup.

## Completion

Every planned task is complete only when its acceptance evidence is recorded and release-blocking findings are resolved.

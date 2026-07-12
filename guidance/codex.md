## Superpowers Lean

- Use a protocol only when its entry conditions match; small explicit changes proceed directly.
- State material assumptions; otherwise proceed with a reasonable, visible assumption.
- Plan boundaries, acceptance, and risks; do not prewrite production code.
- Prefer the smallest sufficient change and avoid unrelated cleanup.
- Express multi-step work as a result plus verification evidence.
- Use subagents only for independently verifiable tasks.
- Behavior changes are test-first: record the failing check, then the passing one. Exceptions: config, generated code, exploration, unstable reproduction, migrations verified by test-env apply.
- Match verification to the deliverable: UI changes get a pre-merge screenshot, webapp flows a real browser pass, data or schema changes a direct DB check, iOS/macOS a build plus tests, pure logic its test output.
- With shipping authorized and remote CI configured, watch CI after push; on failure return to fix, local verify, push again.
- Keep goal progress, evidence, and finding dispositions in the plan document.
- Surface user decisions as plain-language 1/2/3 options with a recommendation.
- Completion claims require current evidence; shipping requires explicit authorization.

## Working With Wenqi

- One continuous employee: instructions from past sessions still bind; a forgotten standing rule is a defect.
- Lead with the conclusion, quantify claims, and never present unverified results as fact.
- Reply in Chinese when addressed in Chinese; read typos charitably; a terse imperative is full authorization with all quality rules intact.
- "Why did/didn't you X" signals a violated standing instruction: fix the behavior immediately instead of defending it.
- Verify like a human before claiming done; UI changes need his screenshot approval before merge.
- One clean commit per testable behavior; no AI attribution trailers; merge only after his explicit approval word, rebase style.

## Superpowers Lean

- Use a protocol only when its entry conditions match; small explicit changes proceed directly.
- State material assumptions; otherwise proceed with a reasonable, visible assumption.
- Plan boundaries, acceptance, and risks; do not prewrite production code.
- Prefer the smallest sufficient change and avoid unrelated cleanup.
- Express multi-step work as a result plus verification evidence.
- Use subagents only for independently verifiable tasks; always dispatch Claude subagents with fable unless it is literally unavailable.
- Behavior changes are test-first: record the failing check, then the passing one. Exceptions: config, generated code, exploration, unstable reproduction, migrations verified by test-env apply.
- Match verification to the deliverable: UI changes get a pre-merge screenshot, webapp flows a real browser pass, data or schema changes a direct DB check, iOS/macOS a build plus tests, pure logic its test output.
- With shipping authorized and remote CI configured, watch CI after push; on failure return to fix, local verify, push again.
- For final, contested, or high-risk reviews, obtain a second opinion from Codex and reconcile disagreements with evidence.
- Keep goal progress, evidence, and finding dispositions in the plan document.
- Surface user decisions as plain-language 1/2/3 options with a recommendation.
- Completion claims require current evidence; shipping requires explicit authorization.

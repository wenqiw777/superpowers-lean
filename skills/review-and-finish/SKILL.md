---
name: review-and-finish
description: Review completed work, verify release evidence, and prepare an authorized finish. Use for plan readiness gates, per-task review, bug-only audits, merge or release preparation, or review feedback.
---

# Review and Finish

## Select a Profile

- **Readiness:** check an unimplemented plan for implementation blockers.
- **Per-step:** check one completed task for scope, regression, and acceptance gaps.
- **Bug-only:** report only confirmed logic, crash, data, or security defects; do not add style findings.
- **Finish:** check release blockers, verification evidence, change scope, and delivery safety.

Read only the selected profile from the configured rubric.

## Finding Standard

Each finding includes the affected behavior, supporting evidence, user impact, and severity. A finding is release-blocking only when it can cause incorrect behavior, crash, data loss, security exposure, failed required verification, or an explicitly violated requirement.

Do not elevate a naming preference, formatting preference, optional abstraction, or unproven concern into a blocker.

## Review Scope

- Review only the selected task, plan, or delivery range.
- Check unchanged code only when the selected requirement crosses that boundary.
- In bug-only mode, prefer `NO BUG FOUND` or stated coverage limits over speculative findings.
- In readiness mode, return the plan to design only for concrete implementation blockers.

## Disposition Rules

For each non-blocking finding, present the user with a recommendation and choices to fix now, accept, or track later. Record the chosen disposition in the plan. The reviewer cannot self-accept a finding on the user's behalf.

## Re-review Rule

After a blocker is fixed, review the changed behavior and its verification evidence again. Do not restart a broad review unless the fix changes scope or exposes a new relevant boundary.

## Second Opinion

For a final review, a contested finding severity, or a high-risk change, obtain the independent second opinion configured in runtime guidance and reconcile disagreements with evidence. Do not trigger it for small mechanical changes.

## Protocol

1. Establish scope and read the relevant artifacts or diff.
2. Report only evidence-backed findings with severity and impact.
3. Resolve release-blocking findings, then re-review the changed result.
4. Present each non-blocking finding to the user with a plain-language disposition recommendation: fix now, accept, or track later.
5. Require current verification evidence before claiming completion.

## Finish Gate

Do not ship, push, open a PR, send a message, discard work, or delete a branch without the authorization required by runtime guidance. Record the final verification and dispositions in the plan document.

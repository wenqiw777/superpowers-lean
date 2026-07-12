# Review Rubric

Select one profile only.

## Readiness

- Does the plan state outcome, boundaries, non-goals, dependencies, and acceptance evidence?
- Are material decisions resolved and task boundaries independently verifiable?
- Is any required migration, compatibility, or safety work missing?

## Per-step

- Does the change meet its task acceptance criteria?
- Does it introduce regression, boundary, or state-management risk?
- Is the verification evidence current and relevant?
- Is task-local code quality (naming, clarity, structure) acceptable without expanding scope?

## Bug-only

- Report only confirmed logic defects, crash paths, data-loss risks, security issues, or material edge cases.
- Anchor every finding to evidence.
- If no confirmed defect exists, say `NO BUG FOUND` or state partial coverage.

## Finish

- Are all release blockers resolved and re-reviewed?
- Are non-blocking findings visibly fixed, accepted, or tracked later?
- Does verification match the change type and delivery risk?
- Is every external or destructive action explicitly authorized?

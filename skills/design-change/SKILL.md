---
name: design-change
description: Clarify and make a change implementation-ready when requirements are ambiguous, architecture choices are material, or a plan needs readiness review. Do not use for small explicit edits.
---

# Design Change

## Entry

Use when a requested change has material ambiguity, multiple viable designs, or needs a readiness review before implementation.

Bypass this protocol for a small, explicit change with an obvious verification path.

## Protocol

1. Establish the requested outcome, constraints, non-goals, and existing context.
2. Surface only decisions that could materially change the result. Present each as plain-language 1/2/3 options with a recommendation.
3. Define boundaries, interfaces, acceptance evidence, risks, and task dependencies. Do not write production-code bodies.
4. For readiness review, identify blocking gaps, resolve them in the plan, and repeat review until no implementation blocker remains.

## Readiness Checks

Treat these as implementation blockers:

- The requested behavior or non-goal is ambiguous.
- A task depends on an interface, data shape, or ordering that is not defined.
- Acceptance cannot distinguish success from a plausible partial implementation.
- A delivery constraint, migration, or compatibility requirement has no owner task.
- A task is too large to receive one independent verification result.

Do not create blockers from personal style preference, hypothetical future abstraction, or unrelated cleanup.

## Decision Discipline

- Give the user a recommendation, a concise tradeoff, and plain-language choices.
- Preserve decisions already made by the user; do not reopen them without contradictory evidence.
- If a reasonable assumption is reversible and does not materially change the outcome, state it and proceed.
- If an assumption changes scope, product behavior, or external authority, stop for a user decision.

## Plan Contract

Each executable task states:

- The independently testable result.
- The affected boundary and any prerequisite task.
- The expected evidence of success.
- The decision point that would require returning to design.

## Handoff to Execution

Before handing a plan to execution, verify that every requirement maps to a task or a declared non-goal. Confirm that task order follows real dependencies rather than file order.

The handoff must answer:

- What is the first verifiable result?
- Which behavior is deliberately out of scope?
- Which evidence demonstrates the completed change to a later reviewer?
- Which change in facts would invalidate the plan?

If these answers are absent, continue readiness review. If they are present, execution owns implementation choices that remain within the approved boundaries.

Do not prescribe implementation bodies during handoff. Keep task contracts stable while allowing minimal, evidence-driven implementation choices.

Use the smallest design that makes verification and user decisions unambiguous.

## Completion

The plan is implementation-ready when its scope, decisions, acceptance evidence, dependencies, and task boundaries are explicit. Record readiness in the plan document.

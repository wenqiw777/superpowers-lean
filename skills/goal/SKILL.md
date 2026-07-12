---
name: goal
description: Run a plan or ticket through the Lean protocol and resume it from plan-document progress. Use when the user explicitly invokes this plugin's Goal workflow with an approved plan or ticket.
---

# Goal

## Entry

Read the plan or ticket and its recorded progress. Determine whether it is implementation-ready.

## Protocol

1. Route an unready input through `design-change`; route a ready input through `execute-change`.
2. Select verification appropriate to the planned deliverable and acceptance evidence.
3. Use `review-and-finish` before any authorized delivery action.
4. Write task state, verification evidence, and finding dispositions back into the plan document.

## Resume Rule

The plan document is the only progress record. Before resuming, distinguish completed tasks with current evidence from incomplete tasks, blocked decisions, and stale evidence. Do not recreate already completed work solely because the session changed.

## Delivery Selection

- Choose verification from the deliverable's acceptance evidence.
- Do not run browser verification for work that has no browser-facing behavior.
- Do not perform delivery actions unless the user has authorized them through the request or approved plan.
- Generate a teammate update only when explicitly requested.

## Stop Conditions

Stop and ask the user when a material product decision, scope expansion, external authority, or unresolved release blocker prevents further safe progress.

## Authorization

Do not infer shipping, pull-request, external-message, or tracking-system authorization from the Goal workflow. Surface material decisions to the user in plain-language options.

## Completion

The Goal completes when the plan document records completed tasks, current verification evidence, and user-visible disposition of non-blocking findings.

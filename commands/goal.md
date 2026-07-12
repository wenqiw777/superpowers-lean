---
description: Run an approved plan through the Lean development protocol.
argument-hint: <plan-or-ticket> [--ship] [--team-update]
---

Use the Goal protocol for the supplied plan or ticket.

1. Determine whether the input is implementation-ready.
2. If it is not ready, use `design-change`; otherwise use `execute-change`.
3. Record task progress, evidence, and finding dispositions in the plan document.
4. Treat an explicit user-supplied `--ship`, or a user-approved plan that requires publishing, as shipping authorization; a model-drafted unapproved plan never authorizes shipping.
5. Produce a teammate update only when `--team-update` is present or the user explicitly asks.

---
name: diagnose
description: Investigate a failure, error, regression, or unexpected behavior and return an evidence-backed diagnosis without modifying production code. Use when the user asks why something happened or requests investigation only.
---

# Diagnose

## Entry

Use for an unexplained failure, regression, or unexpected behavior when repair authorization has not been given.

## Protocol

1. Establish the symptom, affected boundary, and reproducibility.
2. Gather the smallest evidence set that distinguishes plausible causes.
3. Trace the causal path and rule out alternatives that contradict the evidence.
4. Report the root cause, impact, minimal repair option, and verification needed after repair.

## Evidence Standard

- Separate observed facts from inference.
- Prefer the shortest causal chain that explains every observed symptom.
- Name uncertainty when evidence is insufficient to distinguish two causes.
- Do not report a suspected defect as confirmed without direct support.

## Diagnostic Report

Return, in this order:

1. The confirmed symptom and affected boundary.
2. The evidence that establishes the cause.
3. The root cause and impact.
4. A minimal repair option and its verification requirement.
5. Any decision or authority needed before repair.

## Escalation

If reproduction is unavailable, report the coverage limit and the next evidence needed. Do not substitute speculative repair for diagnosis.

## Completion

Deliver an evidence-backed diagnosis. Do not change code, data, configuration, or external state unless the user separately authorizes repair.

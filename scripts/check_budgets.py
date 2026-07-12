#!/usr/bin/env python3
"""Check the Lean source budgets before plugin installation."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def lines(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


def main() -> int:
    skill_lines = sum(lines(path) for path in (ROOT / "skills").glob("*/SKILL.md"))
    references = list((ROOT / "references").glob("*.md"))
    failures: list[str] = []
    if not 250 <= skill_lines <= 320:
        failures.append(f"SKILL.md total is {skill_lines}; expected 250-320")
    for reference in references:
        if lines(reference) > 120:
            failures.append(f"{reference.name} exceeds 120 lines")
    for guidance in (ROOT / "guidance").glob("*.md"):
        if lines(guidance) + 2 > 25:
            failures.append(f"{guidance.name} managed block exceeds 25 lines")
    hook = subprocess.run(
        [str(ROOT / "hooks" / "session-start")], capture_output=True, text=True, check=False
    )
    if len(hook.stdout.splitlines()) > 10:
        failures.append("session-start hook output exceeds 10 lines")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"budgets pass: {skill_lines} skill lines, {len(references)} references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

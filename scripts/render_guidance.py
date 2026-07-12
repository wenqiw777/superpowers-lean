#!/usr/bin/env python3
"""Render one managed guidance block while preserving user-owned content."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


START = "<!-- superpowers-lean:start -->"
END = "<!-- superpowers-lean:end -->"


def managed_block(source: str) -> str:
    body = source.strip()
    return f"{START}\n{body}\n{END}\n"


def replace_block(target: str, block: str) -> str:
    starts = target.count(START)
    ends = target.count(END)
    if starts != ends or starts > 1:
        raise ValueError("expected exactly one balanced managed block")
    if starts == 0:
        prefix = target.rstrip()
        return f"{prefix}\n\n{block}" if prefix else block
    start = target.index(START)
    end = target.index(END, start) + len(END)
    suffix_start = end + (1 if end < len(target) and target[end] == "\n" else 0)
    return f"{target[:start]}{block}{target[suffix_start:]}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    args = parser.parse_args()

    try:
        source = args.source.read_text(encoding="utf-8")
        target = args.target.read_text(encoding="utf-8") if args.target.exists() else ""
        args.target.parent.mkdir(parents=True, exist_ok=True)
        args.target.write_text(replace_block(target, managed_block(source)), encoding="utf-8")
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAUDE_ONLY_PREFIXES = (
    "- Use subagents only for independently verifiable tasks; always dispatch Claude subagents",
    "- For final, contested, or high-risk reviews, obtain a second opinion from Codex",
)
CODEX_SUBAGENT_RULE = "- Use subagents only for independently verifiable tasks."


def lean_bullets(name: str) -> list[str]:
    text = (ROOT / "guidance" / name).read_text(encoding="utf-8")
    section = text.split("## Working With Wenqi")[0]
    return [line for line in section.splitlines() if line.startswith("- ")]


class GuidanceDriftTest(unittest.TestCase):
    def test_shared_lean_rules_are_identical(self) -> None:
        shared_claude = [
            bullet for bullet in lean_bullets("claude.md") if not bullet.startswith(CLAUDE_ONLY_PREFIXES)
        ]
        shared_codex = [bullet for bullet in lean_bullets("codex.md") if bullet != CODEX_SUBAGENT_RULE]
        self.assertEqual(shared_claude, shared_codex)

    def test_surface_specific_rules_present(self) -> None:
        self.assertTrue(
            any(bullet.startswith(CLAUDE_ONLY_PREFIXES[0]) for bullet in lean_bullets("claude.md"))
        )
        self.assertIn(CODEX_SUBAGENT_RULE, lean_bullets("codex.md"))

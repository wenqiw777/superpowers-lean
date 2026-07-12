import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "render_guidance.py"
START = "<!-- superpowers-lean:start -->"
END = "<!-- superpowers-lean:end -->"


class RenderGuidanceTest(unittest.TestCase):
    def render(self, source_text: str, target_text: str) -> tuple[subprocess.CompletedProcess[str], str]:
        with tempfile.TemporaryDirectory() as directory:
            directory_path = Path(directory)
            source = directory_path / "source.md"
            target = directory_path / "target.md"
            source.write_text(source_text, encoding="utf-8")
            target.write_text(target_text, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--source", str(source), "--target", str(target)],
                text=True,
                capture_output=True,
                check=False,
            )
            return result, target.read_text(encoding="utf-8")

    def test_inserts_managed_block_without_changing_unmanaged_content(self) -> None:
        result, rendered = self.render("- concise rule\n", "# Existing guidance\n\nKeep this.\n")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            rendered,
            "# Existing guidance\n\nKeep this.\n\n"
            f"{START}\n- concise rule\n{END}\n",
        )

    def test_replaces_only_existing_managed_block(self) -> None:
        result, rendered = self.render(
            "- new rule\n",
            "# Existing guidance\n\n"
            f"{START}\n- old rule\n{END}\n\nKeep this.\n",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            rendered,
            "# Existing guidance\n\n"
            f"{START}\n- new rule\n{END}\n\nKeep this.\n",
        )

    def test_rejects_duplicate_or_unbalanced_markers(self) -> None:
        result, rendered = self.render(
            "- rule\n",
            f"{START}\n- first\n{END}\n\n{START}\n- second\n{END}\n",
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exactly one", result.stderr)
        self.assertIn("- first", rendered)
        self.assertIn("- second", rendered)


if __name__ == "__main__":
    unittest.main()

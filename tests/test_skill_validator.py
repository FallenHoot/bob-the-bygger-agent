"""Synthetic configuration regressions; no engineering or host certification."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "skills/validate_skills.py")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class FrontmatterTests(unittest.TestCase):
    def test_duplicate_keys_rejected(self):
        for extra in ("status: draft\nstatus: production", "name: other", "triggers: []\ntriggers: [x]"):
            with self.subTest(extra=extra):
                parsed, error = validator.load_frontmatter("---\nname: sample\ndescription: Sample\n" + extra + "\n---\n")
                self.assertIsNone(parsed)
                self.assertIsNotNone(error)

    def test_malformed_shapes(self):
        for body in ("", "[]", "42", "null", "- sample", "[invalid", "1: text"):
            with self.subTest(body=body):
                parsed, error = validator.load_frontmatter("---\n" + body + "\n---\n")
                self.assertIsNone(parsed)
                self.assertIsNotNone(error)

    def test_valid_mapping(self):
        parsed, error = validator.load_frontmatter("---\nname: sample\ndescription: Sample\nload_with: []\n---\n")
        self.assertIsNone(error)
        self.assertEqual(parsed["load_with"], [])

    def test_bad_field_types_report_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory) / "sample"
            folder.mkdir()
            for field in ("description: null", "description: []", "triggers: [3]", "load_with: null"):
                content = "name: sample\n" + ("description: Sample\n" if not field.startswith("description") else "") + field
                (folder / "SKILL.md").write_text("---\n" + content + "\n---\n", encoding="utf-8")
                with self.subTest(field=field):
                    self.assertTrue(any(level == "error" for level, _ in validator.validate_skill(folder)))


if __name__ == "__main__":
    unittest.main()
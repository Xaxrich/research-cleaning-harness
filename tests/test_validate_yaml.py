import sys
import tempfile
import unittest
from pathlib import Path


HARNESS_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HARNESS_ROOT / "scripts"))


class ValidateYamlTests(unittest.TestCase):
    def test_generated_yaml_subset_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "source_index.yaml"
            path.write_text(
                "\n".join(
                    [
                        "sources:",
                        "  - source_id: F_SUP_001",
                        "    framework: superpowers",
                        "    raw_path: raw/superpowers/a.md",
                        "    estimated_topic: \"iOS App Harness: Migration\"",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            from validate_yaml import validate_harness_yaml

            result = validate_harness_yaml(path)

            self.assertTrue(result.ok, result.errors)

    def test_unquoted_colon_space_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "source_index.yaml"
            path.write_text(
                "\n".join(
                    [
                        "sources:",
                        "  - source_id: F_SUP_001",
                        "    estimated_topic: iOS App Harness: Migration",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            from validate_yaml import validate_harness_yaml

            result = validate_harness_yaml(path)

            self.assertFalse(result.ok)
            self.assertIn("line 3 has unsafe unquoted colon-space", result.errors)


if __name__ == "__main__":
    unittest.main()

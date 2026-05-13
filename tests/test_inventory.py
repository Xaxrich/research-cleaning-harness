import sys
import tempfile
import unittest
from pathlib import Path


HARNESS_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HARNESS_ROOT / "scripts"))


class InventoryTests(unittest.TestCase):
    def test_inventory_ignores_appledouble_files_and_assigns_stable_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw_root = Path(tmp) / "superpowers"
            (raw_root / "nested").mkdir(parents=True)
            (raw_root / "b.md").write_text("# B Topic\n\nBody\n", encoding="utf-8")
            (raw_root / "._b.md").write_text("metadata", encoding="utf-8")
            (raw_root / "image.png").write_bytes(b"PNG")
            (raw_root / "nested" / "SKILL.md").write_text(
                "---\nname: nested-skill\n---\n# Skill Topic\n",
                encoding="utf-8",
            )

            from inventory import build_inventory

            records = build_inventory(raw_root, "superpowers", "F_SUP")

            self.assertEqual([record.source_id for record in records], ["F_SUP_001", "F_SUP_002", "F_SUP_003"])
            self.assertEqual([record.relative_path for record in records], ["b.md", "image.png", "nested/SKILL.md"])
            self.assertEqual(records[0].estimated_topic, "B Topic")
            self.assertEqual(records[1].file_type, "image")
            self.assertEqual(records[2].output_card, "output/source_cards/superpowers/F_SUP_003_nested_SKILL.md")

    def test_inventory_writes_markdown_and_yaml_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            harness_root = Path(tmp) / "harness"
            raw_root = Path(tmp) / "raw" / "superpowers"
            raw_root.mkdir(parents=True)
            (raw_root / "a.md").write_text("# A Topic\n", encoding="utf-8")

            from inventory import build_inventory, write_inventory_files

            records = build_inventory(raw_root, "superpowers", "F_SUP")
            write_inventory_files(records, harness_root)

            inventory_md = (harness_root / "SOURCE_INVENTORY.md").read_text(encoding="utf-8")
            source_index = (harness_root / "output" / "data" / "source_index.yaml").read_text(encoding="utf-8")

            self.assertIn("| F_SUP_001 | superpowers |", inventory_md)
            self.assertIn("raw_path: raw/superpowers/a.md", source_index)
            self.assertIn("processing_status: queued", source_index)

    def test_yaml_output_quotes_values_with_colon_space(self):
        with tempfile.TemporaryDirectory() as tmp:
            harness_root = Path(tmp) / "harness"
            raw_root = Path(tmp) / "raw" / "superpowers"
            raw_root.mkdir(parents=True)
            (raw_root / "a.md").write_text("# iOS App Harness: Migration\n", encoding="utf-8")

            from inventory import build_inventory, write_inventory_files

            records = build_inventory(raw_root, "superpowers", "F_SUP")
            write_inventory_files(records, harness_root)

            source_index = (harness_root / "output" / "data" / "source_index.yaml").read_text(encoding="utf-8")

            self.assertIn('estimated_topic: "iOS App Harness: Migration"', source_index)


if __name__ == "__main__":
    unittest.main()

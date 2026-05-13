import json
import sys
import tempfile
import unittest
from pathlib import Path


HARNESS_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HARNESS_ROOT / "scripts"))
sys.path.insert(0, str(HARNESS_ROOT / "tests"))

from test_validate_source_cards import VALID_CARD


class ValidateCleanDataTests(unittest.TestCase):
    def write_minimal_dataset(self, root: Path, mechanisms: list[dict] | None = None, write_conflict_file: bool = False):
        data_dir = root / "output" / "data"
        card_dir = root / "output" / "source_cards" / "superpowers"
        review_dir = root / "output" / "reviews" / "source_cards" / "superpowers"
        conflict_dir = root / "output" / "conflicts"
        data_dir.mkdir(parents=True)
        card_dir.mkdir(parents=True)
        review_dir.mkdir(parents=True)
        conflict_dir.mkdir(parents=True)

        card_path = card_dir / "F_SUP_001_card.md"
        review_path = review_dir / "F_SUP_001_card_review.md"
        card_path.write_text(VALID_CARD, encoding="utf-8")
        review_path.write_text("# Review\n\ndecision | approved\n", encoding="utf-8")

        (data_dir / "source_cards.jsonl").write_text(
            json.dumps(
                {
                    "source_id": "F_SUP_001",
                    "framework": "superpowers",
                    "raw_path": "raw/superpowers/a.md",
                    "source_card": "output/source_cards/superpowers/F_SUP_001_card.md",
                    "status": "reviewed",
                    "mechanisms": ["M-SUP-001"],
                    "review": "output/reviews/source_cards/superpowers/F_SUP_001_card_review.md",
                }
            )
            + "\n",
            encoding="utf-8",
        )
        (data_dir / "source_index.yaml").write_text(
            "\n".join(
                [
                    "sources:",
                    "  - source_id: F_SUP_001",
                    "    framework: superpowers",
                    "    raw_path: raw/superpowers/a.md",
                    "    processing_status: reviewed",
                    "    output_card: output/source_cards/superpowers/F_SUP_001_card.md",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        if mechanisms is not None:
            (data_dir / "mechanisms.jsonl").write_text(
                "".join(json.dumps(row) + "\n" for row in mechanisms),
                encoding="utf-8",
            )

        if write_conflict_file:
            (conflict_dir / "superpowers_conflicts.md").write_text(
                "# Superpowers Conflicts\n\n| conflict_id | sources | resolution |\n|---|---|---|\n| C-SUP-001 | F_SUP_001 | keep |\n",
                encoding="utf-8",
            )

    def test_missing_mechanisms_jsonl_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_minimal_dataset(root)

            from validate_clean_data import validate_clean_data

            result = validate_clean_data(root)

            self.assertFalse(result.ok)
            self.assertIn("missing data file: output/data/mechanisms.jsonl", result.errors)

    def test_mechanism_referenced_by_source_card_must_exist(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_minimal_dataset(root, mechanisms=[])

            from validate_clean_data import validate_clean_data

            result = validate_clean_data(root)

            self.assertFalse(result.ok)
            self.assertIn("mechanism M-SUP-001 referenced by F_SUP_001 is missing from mechanisms.jsonl", result.errors)

    def test_valid_dataset_with_mechanisms_and_conflict_file_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_minimal_dataset(
                root,
                mechanisms=[
                    {
                        "id": "M-SUP-001",
                        "name": "Scope",
                        "source_framework": "superpowers",
                        "source_file_id": "F_SUP_001",
                        "source_card": "output/source_cards/superpowers/F_SUP_001_card.md",
                        "description": "Keeps scope small.",
                        "failure_modes": ["context_pollution"],
                        "ios_harness_targets": [
                            {
                                "target_layer": "Context Layer",
                                "target_file": "docs/agent/FILE_SCOPE_RULES.md",
                                "version": "v0_1",
                                "transfer_method": "rule",
                            }
                        ],
                        "version_priority": "v0_1",
                        "confidence": "medium",
                        "evidence": [
                            {
                                "evidence_id": "E1",
                                "quote_or_summary": "Short evidence summary.",
                                "source_location": "raw/superpowers/a.md:1",
                                "supports": "M-SUP-001",
                            }
                        ],
                    }
                ],
                write_conflict_file=True,
            )

            from validate_clean_data import validate_clean_data

            result = validate_clean_data(root)

            self.assertTrue(result.ok, result.errors)

    def test_superpowers_dataset_requires_conflict_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_minimal_dataset(
                root,
                mechanisms=[
                    {
                        "id": "M-SUP-001",
                        "name": "Scope",
                        "source_framework": "superpowers",
                        "source_file_id": "F_SUP_001",
                        "source_card": "output/source_cards/superpowers/F_SUP_001_card.md",
                        "description": "Keeps scope small.",
                        "failure_modes": ["context_pollution"],
                        "ios_harness_targets": [
                            {
                                "target_layer": "Context Layer",
                                "target_file": "docs/agent/FILE_SCOPE_RULES.md",
                                "version": "v0_1",
                                "transfer_method": "rule",
                            }
                        ],
                        "version_priority": "v0_1",
                        "confidence": "medium",
                        "evidence": [
                            {
                                "evidence_id": "E1",
                                "quote_or_summary": "Short evidence summary.",
                                "source_location": "raw/superpowers/a.md:1",
                                "supports": "M-SUP-001",
                            }
                        ],
                    }
                ],
            )

            from validate_clean_data import validate_clean_data

            result = validate_clean_data(root)

            self.assertFalse(result.ok)
            self.assertIn("missing conflict file: output/conflicts/superpowers_conflicts.md", result.errors)


if __name__ == "__main__":
    unittest.main()

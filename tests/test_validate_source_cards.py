import sys
import tempfile
import unittest
from pathlib import Path


HARNESS_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HARNESS_ROOT / "scripts"))


VALID_CARD = """# Source Card: F_SUP_001 - A Topic

## 1. Metadata

| Field | Value |
|---|---|
| source_id | F_SUP_001 |
| framework | superpowers |
| raw_path | raw/superpowers/a.md |
| file_type | markdown |
| topic | A Topic |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：测试。

## 3. File Summary

- Summary.

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
| M-SUP-001 | Scope | Keeps scope small. | E1 | medium |

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
| context_pollution | Limits reading. | E1 |

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| One file | Simpler | Traceable | Slower |

## 7. 5 Why Analysis

### Mechanism: Scope

- Why 1: A
- Why 2: B
- Why 3: C
- Why 4: D
- Why 5: E

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
| E1 | Short evidence summary. | raw/superpowers/a.md:1 | M-SUP-001 |

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
| Scope | Context Layer | docs/agent/FILE_SCOPE_RULES.md | v0_1 | rule |

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | Reason. |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| none | none | none |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
| none | none |

## 13. Clean Summary for Codex

Clean summary.
"""


class ValidateSourceCardsTests(unittest.TestCase):
    def test_valid_source_card_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            card_path = Path(tmp) / "card.md"
            card_path.write_text(VALID_CARD, encoding="utf-8")

            from validate_source_cards import validate_card

            result = validate_card(card_path)

            self.assertTrue(result.ok, result.errors)

    def test_missing_required_section_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            card_path = Path(tmp) / "card.md"
            card_path.write_text(VALID_CARD.replace("## 9. iOS Harness Mapping", "## 9. Mapping"), encoding="utf-8")

            from validate_source_cards import validate_card

            result = validate_card(card_path)

            self.assertFalse(result.ok)
            self.assertIn("missing section: ## 9. iOS Harness Mapping", result.errors)

    def test_discovery_ignores_appledouble_metadata_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            good_card = root / "card.md"
            bad_metadata = root / "._card.md"
            good_card.write_text(VALID_CARD, encoding="utf-8")
            bad_metadata.write_bytes(b"\xb0metadata")

            from validate_source_cards import discover_cards

            self.assertEqual(discover_cards(root), [good_card])

    def test_undefined_evidence_reference_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            card_path = Path(tmp) / "card.md"
            card_path.write_text(VALID_CARD.replace("| M-SUP-001 | Scope | Keeps scope small. | E1 | medium |", "| M-SUP-001 | Scope | Keeps scope small. | E2 | medium |"), encoding="utf-8")

            from validate_source_cards import validate_card

            result = validate_card(card_path)

            self.assertFalse(result.ok)
            self.assertIn("undefined evidence reference: E2", result.errors)

    def test_invalid_mapping_layer_and_version_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            card_path = Path(tmp) / "card.md"
            broken = VALID_CARD.replace("Context Layer", "Magic Layer").replace("v0_1", "v9")
            card_path.write_text(broken, encoding="utf-8")

            from validate_source_cards import validate_card

            result = validate_card(card_path)

            self.assertFalse(result.ok)
            self.assertIn("invalid iOS target layer: Magic Layer", result.errors)
            self.assertIn("invalid version priority: v9", result.errors)


if __name__ == "__main__":
    unittest.main()

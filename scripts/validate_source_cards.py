#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re


REQUIRED_SECTIONS = [
    "## 1. Metadata",
    "## 2. One-line Essence",
    "## 3. File Summary",
    "## 4. Core Mechanisms Extracted",
    "## 5. Failure Modes Addressed",
    "## 6. Design Logic",
    "## 7. 5 Why Analysis",
    "## 8. Evidence Snippets",
    "## 9. iOS Harness Mapping",
    "## 10. Transfer Decision",
    "## 11. Uncertainties",
    "## 12. Related Source Cards",
    "## 13. Clean Summary for Codex",
]


REQUIRED_METADATA_FIELDS = [
    "source_id",
    "framework",
    "raw_path",
    "file_type",
    "topic",
    "processed_at",
    "processor",
    "status",
    "confidence",
]


ALLOWED_TARGET_LAYERS = {
    "Goal Layer",
    "Context Layer",
    "Task Layer",
    "Action / ACI Layer",
    "Feedback / Verification Layer",
    "Memory / State Layer",
    "Role / Review Layer",
    "Risk / Release Layer",
    "Harness Maintenance Layer",
}


ALLOWED_VERSION_PRIORITIES = {"v0_1", "v0_5", "v1_0", "no_transfer"}


@dataclass(frozen=True)
class ValidationResult:
    path: Path
    errors: list[str]

    @property
    def ok(self) -> bool:
        return not self.errors


def table_field_present(text: str, field_name: str) -> bool:
    return f"| {field_name} |" in text


def section_text(text: str, heading: str) -> str:
    start = text.find(heading)
    if start == -1:
        return ""
    next_start = text.find("\n## ", start + len(heading))
    if next_start == -1:
        return text[start:]
    return text[start:next_start]


def parse_table_rows(markdown: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in markdown.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells or all(set(cell) <= {"-"} for cell in cells if cell):
            continue
        rows.append(cells)
    return rows


def evidence_ids(text: str) -> set[str]:
    rows = parse_table_rows(section_text(text, "## 8. Evidence Snippets"))
    ids: set[str] = set()
    for row in rows[1:]:
        if row and re.fullmatch(r"E\d+", row[0]):
            ids.add(row[0])
    return ids


def referenced_evidence_ids(text: str) -> set[str]:
    referenced: set[str] = set()
    for heading in ("## 4. Core Mechanisms Extracted", "## 5. Failure Modes Addressed"):
        referenced.update(re.findall(r"\bE\d+\b", section_text(text, heading)))
    return referenced


def validate_evidence_references(text: str, errors: list[str]) -> None:
    defined = evidence_ids(text)
    for evidence_id in sorted(referenced_evidence_ids(text) - defined):
        errors.append(f"undefined evidence reference: {evidence_id}")


def validate_ios_mapping(text: str, errors: list[str]) -> None:
    rows = parse_table_rows(section_text(text, "## 9. iOS Harness Mapping"))
    for row in rows[1:]:
        if len(row) < 5:
            errors.append("iOS Harness mapping row must have 5 columns")
            continue
        target_layer = row[1]
        version = row[3]
        if target_layer not in ALLOWED_TARGET_LAYERS:
            errors.append(f"invalid iOS target layer: {target_layer}")
        if version not in ALLOWED_VERSION_PRIORITIES:
            errors.append(f"invalid version priority: {version}")


def validate_card(path: Path) -> ValidationResult:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"missing section: {section}")

    for field in REQUIRED_METADATA_FIELDS:
        if not table_field_present(text, field):
            errors.append(f"missing metadata field: {field}")

    raw_path_rows = [line for line in text.splitlines() if line.strip().startswith("| raw_path |")]
    if len(raw_path_rows) != 1:
        errors.append("metadata must reference exactly one raw_path")

    if re.search(r"\b(TODO|TBD)\b", text):
        errors.append("card contains placeholder text")

    if "| extracted_mechanism | target_layer | target_file | version | transfer_method |" not in text:
        errors.append("iOS Harness mapping table is missing or malformed")
    else:
        validate_ios_mapping(text, errors)

    validate_evidence_references(text, errors)

    return ValidationResult(path=path, errors=errors)


def is_appledouble(path: Path) -> bool:
    return any(part.startswith("._") for part in path.parts)


def discover_cards(root: Path) -> list[Path]:
    if root.is_file():
        return [] if is_appledouble(root) else [root]
    return sorted(path for path in root.rglob("*.md") if not is_appledouble(path.relative_to(root)))


def main() -> int:
    harness_root = Path(__file__).resolve().parents[1]
    default_cards_root = harness_root / "output" / "source_cards"
    parser = argparse.ArgumentParser(description="Validate Source Card schema compliance.")
    parser.add_argument("paths", nargs="*", type=Path, default=[default_cards_root])
    args = parser.parse_args()

    results: list[ValidationResult] = []
    for path in args.paths:
        for card in discover_cards(path):
            results.append(validate_card(card))

    failed = [result for result in results if not result.ok]
    for result in failed:
        print(f"{result.path}:")
        for error in result.errors:
            print(f"  - {error}")

    print(f"validated {len(results)} source card(s), failures: {len(failed)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

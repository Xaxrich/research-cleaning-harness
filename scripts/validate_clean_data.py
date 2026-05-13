#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ValidationResult:
    errors: list[str]

    @property
    def ok(self) -> bool:
        return not self.errors


REQUIRED_MECHANISM_FIELDS = {
    "id",
    "name",
    "source_framework",
    "source_file_id",
    "source_card",
    "description",
    "failure_modes",
    "ios_harness_targets",
    "version_priority",
    "confidence",
    "evidence",
}


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def parse_source_index(path: Path) -> dict[str, dict[str, str]]:
    records: dict[str, dict[str, str]] = {}
    current: dict[str, str] | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if stripped.startswith("- source_id:"):
            source_id = stripped.split(":", 1)[1].strip().strip('"')
            current = {"source_id": source_id}
            records[source_id] = current
        elif current is not None and ":" in stripped:
            key, value = stripped.split(":", 1)
            current[key.strip()] = value.strip().strip('"')

    return records


def validate_mechanism_row(row: dict, source_ids: set[str], errors: list[str]) -> None:
    missing = REQUIRED_MECHANISM_FIELDS - set(row)
    if missing:
        errors.append(f"mechanism {row.get('id', '<unknown>')} missing fields: {', '.join(sorted(missing))}")

    source_file_id = row.get("source_file_id")
    if source_file_id not in source_ids:
        errors.append(f"mechanism {row.get('id', '<unknown>')} references unknown source_file_id: {source_file_id}")

    if not isinstance(row.get("failure_modes"), list) or not row.get("failure_modes"):
        errors.append(f"mechanism {row.get('id', '<unknown>')} must include at least one failure mode")

    if not isinstance(row.get("ios_harness_targets"), list) or not row.get("ios_harness_targets"):
        errors.append(f"mechanism {row.get('id', '<unknown>')} must include at least one iOS harness target")

    if not isinstance(row.get("evidence"), list) or not row.get("evidence"):
        errors.append(f"mechanism {row.get('id', '<unknown>')} must include evidence")


def validate_clean_data(root: Path) -> ValidationResult:
    errors: list[str] = []
    data_dir = root / "output" / "data"
    source_cards_path = data_dir / "source_cards.jsonl"
    mechanisms_path = data_dir / "mechanisms.jsonl"
    source_index_path = data_dir / "source_index.yaml"

    for rel_path, path in (
        ("output/data/source_cards.jsonl", source_cards_path),
        ("output/data/mechanisms.jsonl", mechanisms_path),
        ("output/data/source_index.yaml", source_index_path),
    ):
        if not path.exists():
            errors.append(f"missing data file: {rel_path}")

    if errors:
        return ValidationResult(errors)

    source_cards = read_jsonl(source_cards_path)
    mechanisms = read_jsonl(mechanisms_path)
    index_records = parse_source_index(source_index_path)

    source_ids = {row["source_id"] for row in source_cards}
    mechanism_ids = {row["id"] for row in mechanisms}

    for row in source_cards:
        source_id = row["source_id"]
        index_record = index_records.get(source_id)
        if index_record is None:
            errors.append(f"{source_id} missing from source_index.yaml")
        elif index_record.get("processing_status") != row.get("status"):
            errors.append(f"{source_id} status mismatch between source_cards.jsonl and source_index.yaml")

        for rel_field in ("source_card", "review"):
            rel_path = row.get(rel_field)
            if not rel_path or not (root / rel_path).exists():
                errors.append(f"{source_id} missing file referenced by {rel_field}: {rel_path}")

        for mechanism_id in row.get("mechanisms", []):
            if mechanism_id not in mechanism_ids:
                errors.append(f"mechanism {mechanism_id} referenced by {source_id} is missing from mechanisms.jsonl")

    for row in mechanisms:
        validate_mechanism_row(row, source_ids, errors)

    frameworks = {row.get("framework") for row in source_cards}
    expected_conflict_ledgers = {
        "superpowers": ("output/conflicts/superpowers_conflicts.md", "C-SUP"),
        "gsd2": ("output/conflicts/gsd2_conflicts.md", "C-GSD"),
        "aider": ("output/conflicts/aider_conflicts.md", "C-AID"),
        "gstack": ("output/conflicts/gstack_conflicts.md", "C-GST"),
        "swe-agent": ("output/conflicts/swe_agent_conflicts.md", "C-SWE"),
    }
    for framework, (rel_path, marker) in expected_conflict_ledgers.items():
        if framework not in frameworks:
            continue
        conflicts_path = root / rel_path
        if not conflicts_path.exists():
            errors.append(f"missing conflict file: {rel_path}")
        elif marker not in conflicts_path.read_text(encoding="utf-8"):
            errors.append(f"{framework} conflict file must include at least one {marker} conflict record")

    return ValidationResult(errors)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate cross-file clean data consistency.")
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    result = validate_clean_data(args.root)
    for error in result.errors:
        print(error)
    print(f"validated clean data, failures: {len(result.errors)}")
    return 1 if result.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

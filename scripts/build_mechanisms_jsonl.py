#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from validate_source_cards import parse_table_rows, section_text


def metadata(text: str) -> dict[str, str]:
    rows = parse_table_rows(section_text(text, "## 1. Metadata"))
    return {row[0]: row[1] for row in rows[1:] if len(row) >= 2}


def failure_modes(text: str) -> list[str]:
    rows = parse_table_rows(section_text(text, "## 5. Failure Modes Addressed"))
    return [row[0] for row in rows[1:] if row and row[0] != "none"]


def evidence_map(text: str) -> dict[str, dict[str, str]]:
    rows = parse_table_rows(section_text(text, "## 8. Evidence Snippets"))
    evidence: dict[str, dict[str, str]] = {}
    for row in rows[1:]:
        if len(row) < 4:
            continue
        evidence[row[0]] = {
            "evidence_id": row[0],
            "quote_or_summary": row[1],
            "source_location": row[2],
            "supports": row[3],
        }
    return evidence


def ios_targets(text: str) -> dict[str, list[dict[str, str]]]:
    rows = parse_table_rows(section_text(text, "## 9. iOS Harness Mapping"))
    targets: dict[str, list[dict[str, str]]] = {}
    for row in rows[1:]:
        if len(row) < 5:
            continue
        targets.setdefault(row[0], []).append(
            {
                "target_layer": row[1],
                "target_file": row[2],
                "version": row[3],
                "transfer_method": row[4],
            }
        )
    return targets


def mechanisms_from_card(card_path: Path, harness_root: Path) -> list[dict]:
    text = card_path.read_text(encoding="utf-8")
    meta = metadata(text)
    modes = failure_modes(text)
    evidence_by_id = evidence_map(text)
    targets_by_name = ios_targets(text)
    source_card = card_path.relative_to(harness_root).as_posix()

    rows = parse_table_rows(section_text(text, "## 4. Core Mechanisms Extracted"))
    mechanisms: list[dict] = []
    for row in rows[1:]:
        if len(row) < 5:
            continue
        mechanism_id, name, description, evidence_refs, confidence = row[:5]
        refs = re.findall(r"\bE\d+\b", evidence_refs)
        targets = targets_by_name.get(mechanism_id, targets_by_name.get(name, []))
        mechanisms.append(
            {
                "id": mechanism_id,
                "name": name,
                "source_framework": meta.get("framework", ""),
                "source_file_id": meta.get("source_id", ""),
                "source_card": source_card,
                "description": description,
                "failure_modes": modes,
                "ios_harness_targets": targets,
                "version_priority": targets[0]["version"] if targets else "no_transfer",
                "confidence": confidence,
                "evidence": [evidence_by_id[ref] for ref in refs if ref in evidence_by_id],
            }
        )

    return mechanisms


def build_mechanisms(harness_root: Path) -> list[dict]:
    cards_root = harness_root / "output" / "source_cards"
    mechanisms: list[dict] = []
    for card_path in sorted(cards_root.rglob("*.md")):
        if any(part.startswith("._") for part in card_path.relative_to(cards_root).parts):
            continue
        mechanisms.extend(mechanisms_from_card(card_path, harness_root))
    return mechanisms


def write_mechanisms_jsonl(harness_root: Path) -> Path:
    output_path = harness_root / "output" / "data" / "mechanisms.jsonl"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rows = build_mechanisms(harness_root)
    output_path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build normalized mechanism JSONL from reviewed Source Cards.")
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    output_path = write_mechanisms_jsonl(args.root)
    count = len(read_rows(output_path))
    print(f"wrote {count} mechanism record(s) to {output_path}")
    return 0


def read_rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import replace
from pathlib import Path

from inventory import SourceRecord, build_inventory, yaml_scalar


FRAMEWORKS = [
    ("superpowers", "F_SUP", "raw/Kimi_Agent_Superpowers 体系探究"),
    ("gsd2", "F_GSD", "raw/Kimi_Agent_多 Agent GSD2"),
    ("aider", "F_AID", "raw/Kimi_Agent_Aider 代码库方案"),
    ("gstack", "F_GST", "raw/Kimi_Agent_gstack 多 Agent 迁移"),
    ("swe-agent", "F_SWE", "raw/Kimi_Agent_SWE-agent 迁移研究"),
]


def parse_existing_statuses(source_index: Path) -> dict[str, str]:
    if not source_index.exists():
        return {}

    statuses: dict[str, str] = {}
    current_id: str | None = None
    for raw_line in source_index.read_text(encoding="utf-8").splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("- source_id:"):
            current_id = stripped.split(":", 1)[1].strip().strip('"')
        elif current_id and stripped.startswith("processing_status:"):
            statuses[current_id] = stripped.split(":", 1)[1].strip().strip('"')
    return statuses


def discover_all_records(project_root: Path, harness_root: Path) -> list[SourceRecord]:
    statuses = parse_existing_statuses(harness_root / "output" / "data" / "source_index.yaml")
    records: list[SourceRecord] = []
    for framework, prefix, raw_root in FRAMEWORKS:
        for record in build_inventory(project_root / raw_root, framework, prefix):
            status = statuses.get(record.source_id, record.processing_status)
            records.append(replace(record, processing_status=status))
    return records


def write_inventory(records: list[SourceRecord], harness_root: Path) -> None:
    data_dir = harness_root / "output" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    lines = [
        "# SOURCE INVENTORY",
        "",
        "Scope: indexed research framework files. AppleDouble `._*` metadata files are ignored, not modified.",
        "",
        "| source_id | framework | raw_path | file_type | estimated_topic | status | output_card |",
        "|---|---|---|---|---|---|---|",
    ]
    for record in records:
        lines.append(
            "| {source_id} | {framework} | {raw_path} | {file_type} | {estimated_topic} | {status} | {output_card} |".format(
                source_id=record.source_id,
                framework=record.framework,
                raw_path=record.raw_path,
                file_type=record.file_type,
                estimated_topic=record.estimated_topic.replace("|", "/"),
                status=record.processing_status,
                output_card=record.output_card,
            )
        )
    (harness_root / "SOURCE_INVENTORY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    yaml_lines = ["sources:"]
    for record in records:
        yaml_lines.extend(
            [
                f"  - source_id: {yaml_scalar(record.source_id)}",
                f"    framework: {yaml_scalar(record.framework)}",
                f"    raw_path: {yaml_scalar(record.raw_path)}",
                f"    relative_path: {yaml_scalar(record.relative_path)}",
                f"    file_type: {yaml_scalar(record.file_type)}",
                f"    estimated_topic: {yaml_scalar(record.estimated_topic)}",
                f"    processing_status: {yaml_scalar(record.processing_status)}",
                f"    output_card: {yaml_scalar(record.output_card)}",
            ]
        )
    (data_dir / "source_index.yaml").write_text("\n".join(yaml_lines) + "\n", encoding="utf-8")


def main() -> int:
    harness_root = Path(__file__).resolve().parents[1]
    project_root = harness_root.parent
    records = discover_all_records(project_root, harness_root)
    write_inventory(records, harness_root)
    counts: dict[str, int] = {}
    for record in records:
        counts[record.framework] = counts.get(record.framework, 0) + 1
    print("wrote framework inventory:", ", ".join(f"{key}={value}" for key, value in counts.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

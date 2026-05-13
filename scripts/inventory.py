#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


FILE_TYPES = {
    ".md": "markdown",
    ".markdown": "markdown",
    ".png": "image",
    ".jpg": "image",
    ".jpeg": "image",
    ".docx": "document",
    ".zip": "archive",
}


@dataclass(frozen=True)
class SourceRecord:
    source_id: str
    framework: str
    raw_path: str
    relative_path: str
    file_type: str
    estimated_topic: str
    processing_status: str
    output_card: str


def is_appledouble(path: Path) -> bool:
    return any(part.startswith("._") for part in path.parts)


def file_type_for(path: Path) -> str:
    return FILE_TYPES.get(path.suffix.lower(), "unknown")


def first_markdown_heading(path: Path) -> str | None:
    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            for _ in range(120):
                line = handle.readline()
                if not line:
                    break
                stripped = line.strip()
                if stripped.startswith("#"):
                    return stripped.lstrip("#").strip()
                if stripped.startswith("name:"):
                    return stripped.split(":", 1)[1].strip().strip("\"'")
    except OSError:
        return None
    return None


def estimated_topic_for(path: Path) -> str:
    file_type = file_type_for(path)
    if file_type == "markdown":
        heading = first_markdown_heading(path)
        if heading:
            return heading
    if file_type == "image":
        return "architecture diagram"
    return path.stem.replace("_", " ").replace("-", " ")


def slug_for(relative_path: str) -> str:
    without_suffix = Path(relative_path).with_suffix("").as_posix()
    slug = re.sub(r"[^\w]+", "_", without_suffix, flags=re.UNICODE).strip("_")
    return slug or "source"


def raw_display_path(raw_root: Path, path: Path) -> str:
    relative = path.relative_to(raw_root).as_posix()
    parts = raw_root.parts
    if "raw" in parts:
        raw_index = len(parts) - 1 - list(reversed(parts)).index("raw")
        display_root = Path(*parts[raw_index:]).as_posix()
    else:
        display_root = raw_root.name
    return f"{display_root}/{relative}"


def yaml_scalar(value: str) -> str:
    needs_quotes = (
        value == ""
        or value != value.strip()
        or ": " in value
        or " #" in value
        or value[0] in "-?:!&*#{}[],|>@`\"'"
    )
    if not needs_quotes:
        return value
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def build_inventory(raw_root: Path, framework: str, id_prefix: str) -> list[SourceRecord]:
    files = [
        path
        for path in raw_root.rglob("*")
        if path.is_file() and not is_appledouble(path.relative_to(raw_root))
    ]
    files.sort(key=lambda path: path.relative_to(raw_root).as_posix())

    records: list[SourceRecord] = []
    for index, path in enumerate(files, start=1):
        source_id = f"{id_prefix}_{index:03d}"
        relative_path = path.relative_to(raw_root).as_posix()
        slug = slug_for(relative_path)
        records.append(
            SourceRecord(
                source_id=source_id,
                framework=framework,
                raw_path=raw_display_path(raw_root, path),
                relative_path=relative_path,
                file_type=file_type_for(path),
                estimated_topic=estimated_topic_for(path),
                processing_status="queued",
                output_card=f"output/source_cards/{framework}/{source_id}_{slug}.md",
            )
        )
    return records


def write_inventory_files(records: list[SourceRecord], harness_root: Path) -> None:
    data_dir = harness_root / "output" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    inventory_lines = [
        "# SOURCE INVENTORY",
        "",
        "Scope: superpowers raw files only. AppleDouble `._*` metadata files are ignored, not modified.",
        "",
        "| source_id | framework | raw_path | file_type | estimated_topic | status | output_card |",
        "|---|---|---|---|---|---|---|",
    ]
    for record in records:
        inventory_lines.append(
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
    (harness_root / "SOURCE_INVENTORY.md").write_text("\n".join(inventory_lines) + "\n", encoding="utf-8")

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
    default_raw_root = harness_root.parent / "raw" / "Kimi_Agent_Superpowers 体系探究"
    parser = argparse.ArgumentParser(description="Build a source inventory for one research framework.")
    parser.add_argument("--raw-root", type=Path, default=default_raw_root)
    parser.add_argument("--harness-root", type=Path, default=harness_root)
    parser.add_argument("--framework", default="superpowers")
    parser.add_argument("--id-prefix", default="F_SUP")
    args = parser.parse_args()

    records = build_inventory(args.raw_root, args.framework, args.id_prefix)
    write_inventory_files(records, args.harness_root)
    print(f"wrote {len(records)} source records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ValidationResult:
    path: Path
    errors: list[str]

    @property
    def ok(self) -> bool:
        return not self.errors


def is_appledouble(path: Path) -> bool:
    return any(part.startswith("._") for part in path.parts)


def unquote_if_quoted(value: str) -> tuple[bool, str]:
    stripped = value.strip()
    if not stripped.startswith('"'):
        return False, stripped
    if len(stripped) < 2 or not stripped.endswith('"'):
        return True, ""
    return True, stripped[1:-1]


def validate_scalar(line_number: int, value: str) -> list[str]:
    errors: list[str] = []
    quoted, unquoted = unquote_if_quoted(value)
    if quoted:
        if value.strip() == '"' or not value.strip().endswith('"'):
            errors.append(f"line {line_number} has unterminated quoted scalar")
        return errors
    if ": " in unquoted:
        errors.append(f"line {line_number} has unsafe unquoted colon-space")
    return errors


def validate_harness_yaml(path: Path) -> ValidationResult:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    nonempty = [line for line in lines if line.strip()]
    if not nonempty:
        return ValidationResult(path, ["file is empty"])

    if nonempty[0] not in {"sources:", "mechanisms:", "failure_modes:", "ios_mapping:"}:
        errors.append("first non-empty line must be a known top-level collection")

    for line_number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped in {"sources:", "mechanisms:", "failure_modes:", "ios_mapping:"}:
            continue
        if line.startswith("  - "):
            item = line[4:]
            if ": " not in item:
                errors.append(f"line {line_number} list item must be key-value")
                continue
            _, value = item.split(":", 1)
            errors.extend(validate_scalar(line_number, value))
            continue
        if line.startswith("    "):
            item = line.strip()
            if ": " not in item:
                errors.append(f"line {line_number} mapping entry must be key-value")
                continue
            _, value = item.split(":", 1)
            errors.extend(validate_scalar(line_number, value))
            continue
        if stripped.startswith("- "):
            errors.append(f"line {line_number} must use two-space indentation before list item")
            continue
        errors.append(f"line {line_number} has unsupported indentation")

    return ValidationResult(path, errors)


def discover_yaml(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file():
            if path.suffix in {".yaml", ".yml"} and not is_appledouble(path):
                files.append(path)
            continue
        files.extend(
            candidate
            for candidate in sorted(path.rglob("*.y*ml"))
            if candidate.suffix in {".yaml", ".yml"} and not is_appledouble(candidate.relative_to(path))
        )
    return files


def main() -> int:
    harness_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Validate the strict YAML subset emitted by this harness.")
    parser.add_argument("paths", nargs="*", type=Path, default=[harness_root / "output" / "data"])
    args = parser.parse_args()

    results = [validate_harness_yaml(path) for path in discover_yaml(args.paths)]
    failed = [result for result in results if not result.ok]
    for result in failed:
        print(f"{result.path}:")
        for error in result.errors:
            print(f"  - {error}")
    print(f"validated {len(results)} yaml file(s), failures: {len(failed)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

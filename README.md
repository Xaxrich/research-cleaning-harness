# Research Cleaning Harness

Research Cleaning Harness is a file-by-file cleaning pipeline for turning raw framework research into traceable, reusable data assets for a future iOS App Harness.

The rule is simple: raw files are evidence, Source Cards are normalized assets, conflict ledgers record synthesis risks, and later Codex work should read clean outputs before raw material.

## Current Scope

As of 2026-05-13:

| framework | indexed files | reviewed source cards | status |
|---|---:|---:|---|
| superpowers | 14 | 14 | reviewed |
| gsd2 | 12 | 12 | reviewed |
| aider | 39 | 39 | reviewed |
| gstack | 40 | 40 | reviewed |
| swe-agent | 29 | 29 | reviewed |

Machine-readable outputs:

| data file | count |
|---|---:|
| `output/data/source_cards.jsonl` | 134 |
| `output/data/mechanisms.jsonl` | 625 |

## Repository Contents

| path | purpose |
|---|---|
| `STATE.md` | current phase, completed frameworks, next framework |
| `TASKS.md` | task history and acceptance notes |
| `SOURCE_INVENTORY.md` | indexed raw files and processing status |
| `EXTRACTION_SCHEMA.md` | required Source Card schema |
| `QUALITY_GATE.md` | validation rules for acceptable clean assets |
| `output/source_cards/` | reviewed Source Cards, one per raw file |
| `output/reviews/source_cards/` | review records for Source Cards |
| `output/conflicts/` | framework conflict ledgers |
| `output/data/` | JSONL/YAML machine-readable indexes |
| `scripts/` | inventory, generation and validation scripts |
| `tests/` | unit tests for validators and inventory logic |

## Validation

Fresh validation commands run during the latest confirmation:

```bash
python3 research_cleaning_harness/scripts/validate_source_cards.py
python3 research_cleaning_harness/scripts/validate_yaml.py
python3 research_cleaning_harness/scripts/validate_clean_data.py
python3 -m unittest discover research_cleaning_harness/tests
```

Expected current results:

```text
validated 134 source card(s), failures: 0
validated 1 yaml file(s), failures: 0
validated clean data, failures: 0
Ran 14 tests ... OK
```

If running from inside this directory, drop the `research_cleaning_harness/` prefix from script paths.

## Public Repository Boundary

This project intentionally publishes the cleaned harness assets, not the `raw/` research directory. The raw files stay outside this project directory and are treated as immutable evidence on the local machine.

AppleDouble metadata files named `._*` are ignored by validators and `.gitignore`.

## Next Work

Run one synthesis stage at a time:

1. Framework summaries.
2. Cross-framework mechanism synthesis.
3. iOS Harness mapping and Codex handoff pack.

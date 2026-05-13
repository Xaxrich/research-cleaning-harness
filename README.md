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
| `generated/ios_app_harness/data/mechanism_targets.jsonl` | 629 |
| `generated/ios_app_harness/data/source_to_harness_trace.jsonl` | 134 |

## Repository Contents

| path | purpose |
|---|---|
| `LEARNER_GUIDE.md` | from-zero guide for learning and applying the harness |
| `STATE.md` | current phase, completed frameworks, next framework |
| `TASKS.md` | task history and acceptance notes |
| `SOURCE_INVENTORY.md` | indexed raw files and processing status |
| `EXTRACTION_SCHEMA.md` | required Source Card schema |
| `QUALITY_GATE.md` | validation rules for acceptable clean assets |
| `output/source_cards/` | reviewed Source Cards, one per raw file |
| `output/reviews/source_cards/` | review records for Source Cards |
| `output/conflicts/` | framework conflict ledgers |
| `output/frameworks/` | framework summaries generated from reviewed Source Cards |
| `output/mechanisms/` | cross-framework mechanism group docs |
| `output/failure_modes/` | failure-mode guard docs |
| `output/ios_harness_mapping/` | file placement, scope and Codex handoff mapping |
| `generated/ios_app_harness/` | lightweight fused iOS App Harness v0.1 |
| `output/data/` | JSONL/YAML machine-readable indexes |
| `scripts/` | inventory, generation and validation scripts |
| `tests/` | unit tests for validators and inventory logic |

## Validation

Fresh validation commands run during the latest confirmation:

```bash
python3 research_cleaning_harness/generated/ios_app_harness/scripts/validate_harness.py
python3 research_cleaning_harness/scripts/validate_source_cards.py
python3 research_cleaning_harness/scripts/validate_yaml.py
python3 research_cleaning_harness/scripts/validate_clean_data.py
python3 -m unittest discover research_cleaning_harness/tests
```

Expected current results:

```text
validated ios_app_harness, failures: 0
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

Review and adapt the generated lightweight harness against a real iOS app repo:

1. Start at `LEARNER_GUIDE.md`.
2. Then read `generated/ios_app_harness/README.md`.
3. Use `output/ios_harness_mapping/source_to_harness_trace.md` to audit how each Source Card influenced the harness.
4. Copy/adapt v0.1 docs before enabling v0.5 scripts or v1.0 runtime ideas.

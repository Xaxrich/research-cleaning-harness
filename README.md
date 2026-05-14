# Research Cleaning Harness

Research Cleaning Harness is a file-by-file cleaning pipeline for turning raw framework research into traceable, reusable data assets for a future iOS App Harness.

The standalone, ready-to-use development framework is:

```text
ios_app_development_harness/
```

If your goal is to use the final iOS app development harness rather than study the research process, start there:

```text
ios_app_development_harness/README.md
ios_app_development_harness/FULL_TUTORIAL.md
ios_app_development_harness/FRAMEWORK_SPEC.md
ios_app_development_harness/START_HERE.md
ios_app_development_harness/CALL_GRAPH.md
```

The rule is simple: raw files are evidence, Source Cards are normalized assets, conflict ledgers record synthesis risks, and later Codex work should read clean outputs before raw material.

## Current Scope

As of 2026-05-14:

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
| `ios_app_development_harness/` | layered standalone iOS app development harness ready to copy into a real repo |
| `ios_app_development_harness/START_HERE.md` | human-facing entry point |
| `ios_app_development_harness/CALL_GRAPH.md` | layer call graph for humans and agents |
| `ios_app_development_harness/layers/` | 11-layer framework organized by goal, task, context, scope, review, ACI, verification, risk, memory, workflow and examples |
| `ios_app_development_harness/FULL_TUTORIAL.md` | detailed tutorial covering design, usage, task flow, and decisions |
| `ios_app_development_harness/FRAMEWORK_SPEC.md` | standalone framework design spec and rationale |
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
python3 research_cleaning_harness/ios_app_development_harness/scripts/validate_harness.py
python3 research_cleaning_harness/generated/ios_app_harness/scripts/validate_harness.py
python3 research_cleaning_harness/scripts/validate_source_cards.py
python3 research_cleaning_harness/scripts/validate_yaml.py
python3 research_cleaning_harness/scripts/validate_clean_data.py
python3 -m unittest discover research_cleaning_harness/tests
```

Expected current results:

```text
validated layered ios app development harness, failures: 0
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

Use the standalone harness in a real iOS app repo:

1. Copy `ios_app_development_harness/` into the target repo as `agent_harness/`.
2. Read `agent_harness/START_HERE.md`, then `agent_harness/CALL_GRAPH.md`.
3. Adapt `layers/00_goal/PRODUCT_SPEC.md`, `layers/02_context/CONTEXT_INDEX.md`, `layers/03_file_scope/FILE_SCOPE_RULES.md`, and `layers/06_verification/VERIFICATION_MATRIX.md`.
4. Create the first task in `layers/01_task/TASKS.md`.
5. Let Codex work through `AGENTS.md` and the task card.

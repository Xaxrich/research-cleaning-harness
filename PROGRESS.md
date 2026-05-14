# Progress

Last updated: 2026-05-13

## Status Snapshot

| framework | inventory | source cards | reviews | mechanism records | status |
|---|---:|---:|---:|---:|---|
| superpowers | 14 | 14 | 14 | 97 | reviewed |
| gsd2 | 12 | 12 | 12 | 96 | reviewed |
| aider | 39 | 39 | 39 | 156 | reviewed |
| gstack | 40 | 40 | 40 | 160 | reviewed |
| swe-agent | 29 | 29 | 29 | 116 | reviewed |

Total reviewed Source Cards: 134

Total mechanism records: 625

Generated iOS Harness target rows: 629

Standalone iOS App Development Harness: `ios_app_development_harness/`

## Completed

- Built the Research Cleaning Harness skeleton and schema.
- Indexed all five framework raw folders.
- Cleaned Superpowers into reviewed Source Cards, reviews, mechanism records and a conflict ledger.
- Cleaned GSD2 into reviewed Source Cards, reviews, mechanism records and a conflict ledger.
- Cleaned Aider into reviewed Source Cards, reviews, mechanism records and a conflict ledger.
- Cleaned gstack into reviewed Source Cards, reviews, mechanism records and a conflict ledger.
- Cleaned SWE-agent into reviewed Source Cards, reviews, mechanism records and a conflict ledger.
- Added validation scripts and unit tests for Source Card schema, YAML, clean-data consistency and inventory behavior.
- Generated a lightweight fused iOS App Harness from the clean mechanism index.
- Generated framework summaries, mechanism group docs, failure-mode docs and iOS Harness mapping docs.
- Generated a standalone iOS App Development Harness that can be copied directly into a real app repo.
- Published the project to public GitHub via SSH.

## Current Clean Outputs

| output | path |
|---|---|
| Source card index | `output/data/source_cards.jsonl` |
| Mechanism index | `output/data/mechanisms.jsonl` |
| Source inventory | `SOURCE_INVENTORY.md` |
| Source index | `output/data/source_index.yaml` |
| Superpowers conflicts | `output/conflicts/superpowers_conflicts.md` |
| GSD2 conflicts | `output/conflicts/gsd2_conflicts.md` |
| Aider conflicts | `output/conflicts/aider_conflicts.md` |
| gstack conflicts | `output/conflicts/gstack_conflicts.md` |
| SWE-agent conflicts | `output/conflicts/swe_agent_conflicts.md` |
| Generated iOS Harness | `generated/ios_app_harness/` |
| Standalone Development Harness | `ios_app_development_harness/` |
| Standalone Tutorial | `ios_app_development_harness/FULL_TUTORIAL.md` |
| Standalone Framework Spec | `ios_app_development_harness/FRAMEWORK_SPEC.md` |
| Source-to-harness trace | `generated/ios_app_harness/data/source_to_harness_trace.jsonl` |
| Harness mapping docs | `output/ios_harness_mapping/` |
| Framework summaries | `output/frameworks/` |
| Mechanism group docs | `output/mechanisms/` |
| Failure mode docs | `output/failure_modes/` |

## Validation Log

Latest fresh validation performed after lightweight iOS Harness generation:

| command | result |
|---|---|
| `python3 research_cleaning_harness/ios_app_development_harness/scripts/validate_harness.py` | `validated standalone ios app development harness, failures: 0` |
| `python3 research_cleaning_harness/generated/ios_app_harness/scripts/validate_harness.py` | `validated ios_app_harness, failures: 0` |
| `python3 research_cleaning_harness/scripts/validate_source_cards.py` | `validated 134 source card(s), failures: 0` |
| `python3 research_cleaning_harness/scripts/validate_yaml.py` | `validated 1 yaml file(s), failures: 0` |
| `python3 research_cleaning_harness/scripts/validate_clean_data.py` | `validated clean data, failures: 0` |
| `python3 -m unittest discover research_cleaning_harness/tests` | `Ran 14 tests ... OK` |

## Known Boundaries

- Runtime claims such as SQLite state backend, autonomous dispatch, worker lease, MCP runtime and automatic repo-map enforcement are not implemented. They remain future mapping candidates.
- GitHub CLI API auth still reports an invalid token for account `Xaxrich`; repository push currently uses SSH.

## GitHub

Public repository: `https://github.com/Xaxrich/research-cleaning-harness`

## Next Step

Copy `ios_app_development_harness/` into a real iOS app repo as `agent_harness/`, then follow `FULL_TUTORIAL.md`.

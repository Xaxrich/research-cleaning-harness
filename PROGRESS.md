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

## Completed

- Built the Research Cleaning Harness skeleton and schema.
- Indexed all five framework raw folders.
- Cleaned Superpowers into reviewed Source Cards, reviews, mechanism records and a conflict ledger.
- Cleaned GSD2 into reviewed Source Cards, reviews, mechanism records and a conflict ledger.
- Cleaned Aider into reviewed Source Cards, reviews, mechanism records and a conflict ledger.
- Cleaned gstack into reviewed Source Cards, reviews, mechanism records and a conflict ledger.
- Cleaned SWE-agent into reviewed Source Cards, reviews, mechanism records and a conflict ledger.
- Added validation scripts and unit tests for Source Card schema, YAML, clean-data consistency and inventory behavior.

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

## Validation Log

Latest fresh validation performed after SWE-agent cleaning:

| command | result |
|---|---|
| `python3 research_cleaning_harness/scripts/validate_source_cards.py` | `validated 134 source card(s), failures: 0` |
| `python3 research_cleaning_harness/scripts/validate_yaml.py` | `validated 1 yaml file(s), failures: 0` |
| `python3 research_cleaning_harness/scripts/validate_clean_data.py` | `validated clean data, failures: 0` |
| `python3 -m unittest discover research_cleaning_harness/tests` | `Ran 14 tests ... OK` |

## Known Boundaries

- Framework summaries are not generated yet.
- Cross-framework mechanism Markdown files are not generated yet.
- Runtime claims such as SQLite state backend, autonomous dispatch, worker lease, MCP runtime and automatic repo-map enforcement are not implemented. They remain future mapping candidates.
- The project is not currently uploaded to GitHub because local `gh auth status` reports an invalid token for account `Xaxrich`.

## Next Step

Run fresh validation, then begin framework summaries one framework at a time.

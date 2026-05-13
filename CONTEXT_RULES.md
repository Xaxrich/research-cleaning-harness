# CONTEXT RULES

## Default Rule

Process one source file at a time.

## Source Card Generation

Required reads:

- `STATE.md`
- `TASKS.md`
- `EXTRACTION_SCHEMA.md`
- `QUALITY_GATE.md`
- `templates/source_card_template.md`
- the single raw file assigned by the task

Forbidden reads:

- other framework folders
- other raw files
- framework summaries
- mechanism library files

Allowed writes:

- the assigned Source Card
- `output/data/source_cards.jsonl`
- task/state status updates after validation

## Source Card Review

Required reads:

- the assigned Source Card
- `QUALITY_GATE.md`
- `templates/review_template.md`
- the single referenced raw file only when checking fidelity

Forbidden:

- adding new conclusions
- rewriting the source card without an explicit fix task
- reviewing multiple source cards at once

## Framework Synthesis

Required reads:

- all reviewed Source Cards for one framework
- `templates/framework_summary_template.md`
- `templates/mechanism_card_template.md`

Forbidden reads:

- raw files, unless a reviewed Source Card has missing or contradictory evidence
- other frameworks, unless the task is cross-framework synthesis

## Mechanism and Failure Mode Synthesis

Required reads:

- reviewed Source Cards
- framework summaries

Forbidden:

- treating raw reports as direct execution rules
- merging a mechanism without source card IDs

## AppleDouble Files

Files or folders named `._*` are macOS metadata artifacts. They are excluded from inventory and processing. Do not delete them from `raw/`.

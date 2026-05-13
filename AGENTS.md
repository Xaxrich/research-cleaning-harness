# Research Cleaning Harness Agent Guide

## Purpose

This harness converts messy research files into traceable, reusable data assets for a later iOS App Harness build.

Current scope is `superpowers` only:

```text
raw/Kimi_Agent_Superpowers 体系探究/
```

Do not process `gsd2`, `gstack`, `aider`, or `swe-agent` until the user explicitly expands scope.

## Core Contract

1. Treat `raw/` as immutable evidence.
2. Process one source file at a time.
3. Every processed file produces exactly one Source Card.
4. Source Cards must follow `EXTRACTION_SCHEMA.md` and `templates/source_card_template.md`.
5. Evidence and interpretation must be separated.
6. Unsupported statements must be marked as `inferred`.
7. Framework summaries and mechanism libraries must read reviewed Source Cards first, not raw files.
8. All output must serve later iOS App Harness construction.

## Required Start Context

Before executing a task, read:

- `STATE.md`
- `TASKS.md`
- `CONTEXT_RULES.md`
- `EXTRACTION_SCHEMA.md`
- `QUALITY_GATE.md`

Then read only the raw file or clean output explicitly allowed by the current task.

## Roles

| Role | Reads | Writes | Forbidden |
|---|---|---|---|
| Inventory Agent | `raw/Kimi_Agent_Superpowers 体系探究/` file paths and headings | `SOURCE_INVENTORY.md`, `output/data/source_index.yaml` | content synthesis |
| Source Reader Agent | one assigned raw file, schema, template | one Source Card, optional JSONL record | other raw files |
| Reviewer Agent | one Source Card, its single raw file if needed | review note, status update | adding new conclusions |
| Synthesizer Agent | reviewed Source Cards | framework summary, mechanism/failure/mapping outputs | direct raw reads unless evidence is missing |

## Status Values

Use these status values consistently:

```text
queued
reading
source_card_done
review_needed
reviewed
merged
rejected
ignored
```

## Current Execution Rule

The next executable task is `TASK-004`, which processes `F_SUP_002`.

Do not start framework synthesis until all superpowers Source Cards are reviewed.

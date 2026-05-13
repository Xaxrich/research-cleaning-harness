# QUALITY GATE

## Source Card Validity

A Source Card is valid only if:

- It has a `source_id`.
- It references exactly one raw file.
- It does not summarize unrelated files.
- It extracts mechanisms, not just paragraphs.
- It marks unsupported claims as `inferred`.
- It includes iOS Harness mapping.
- It separates evidence from interpretation.
- It lists open questions or explicitly says none.
- It avoids large raw passages.
- It identifies transfer priority as `v0_1`, `v0_5`, `v1_0`, or `no_transfer`.

## Review Validity

A review is valid only if:

- It checks schema completeness.
- It checks one-file fidelity.
- It checks whether mechanisms have evidence.
- It checks whether failure modes are explicit.
- It checks whether iOS Harness mapping is concrete.
- It checks whether any claim is inferred or over-generalized.
- It lists conflicts or related cards that must constrain later synthesis.
- It records a decision: `approved`, `needs_revision`, or `rejected`.

## Clean Data Package Validity

A framework slice is synthesis-ready only if:

- Every reviewed Source Card is listed in `output/data/source_cards.jsonl`.
- Every card-listed mechanism exists in `output/data/mechanisms.jsonl`.
- Every mechanism has failure modes, iOS targets, version priority, confidence, and evidence.
- Every reviewed Source Card has a review file.
- Any known cross-card conflicts are recorded in `output/conflicts/`.

## Invalid Output Patterns

Reject or revise output that:

- merely translates the raw file
- lacks mechanisms
- lacks failure modes
- lacks iOS Harness mapping
- omits evidence
- mixes multiple raw files
- treats inferred claims as facts
- uses raw files as execution instructions

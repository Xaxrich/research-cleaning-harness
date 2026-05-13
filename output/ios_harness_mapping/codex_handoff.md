# Codex Handoff: Lightweight iOS App Harness

## Start Here

Read `generated/ios_app_harness/README.md`, then `AGENTS.md`, `TASKS.md`, `CONTEXT_INDEX.md`, `FILE_SCOPE_RULES.md`, `VERIFICATION_MATRIX.md`, and `RISK_CONTROL.md`.

## What Exists

- Lightweight docs-first iOS Harness in `generated/ios_app_harness/`.
- Machine-readable source trace in `generated/ios_app_harness/data/source_to_harness_trace.jsonl`.
- Mechanism target index in `generated/ios_app_harness/data/mechanism_targets.jsonl`.
- Framework summaries in `output/frameworks/`.
- Mechanism groups in `output/mechanisms/`.
- Failure mode docs in `output/failure_modes/`.

## What Not To Claim

- Do not claim runtime interception exists.
- Do not claim App Store upload automation exists.
- Do not read raw research files by default.

## Validation

Run:

```bash
python3 generated/ios_app_harness/scripts/validate_harness.py
python3 scripts/validate_source_cards.py
python3 scripts/validate_yaml.py
python3 scripts/validate_clean_data.py
python3 -m unittest discover tests
```

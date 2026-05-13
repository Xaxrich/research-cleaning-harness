# Validation Log

## 2026-05-13 Aider Completion Check

Fresh commands executed from `/Volumes/xtaxrich/03-TEMPLATES/xtaxharness`:

```bash
python3 research_cleaning_harness/scripts/validate_source_cards.py
python3 research_cleaning_harness/scripts/validate_yaml.py
python3 research_cleaning_harness/scripts/validate_clean_data.py
python3 -m unittest discover research_cleaning_harness/tests
```

Observed output:

```text
validated 65 source card(s), failures: 0
validated 1 yaml file(s), failures: 0
validated clean data, failures: 0
Ran 14 tests in 0.032s
OK
```

Additional audit:

```text
source_cards_jsonl 65 {'superpowers': 14, 'gsd2': 12, 'aider': 39}
mechanisms_jsonl 349 {'aider': 156, 'gsd2': 96, 'superpowers': 97}
inventory_status {
  ('superpowers', 'reviewed'): 14,
  ('gsd2', 'reviewed'): 12,
  ('aider', 'reviewed'): 39,
  ('gstack', 'queued'): 40,
  ('swe-agent', 'queued'): 29
}
```

## 2026-05-13 gstack Completion Check

Fresh commands executed from `/Volumes/xtaxrich/03-TEMPLATES/xtaxharness`:

```bash
python3 research_cleaning_harness/scripts/validate_source_cards.py
python3 research_cleaning_harness/scripts/validate_yaml.py
python3 research_cleaning_harness/scripts/validate_clean_data.py
python3 -m unittest discover research_cleaning_harness/tests
```

Observed output:

```text
validated 105 source card(s), failures: 0
validated 1 yaml file(s), failures: 0
validated clean data, failures: 0
Ran 14 tests in 0.035s
OK
```

Additional audit:

```text
source_cards_jsonl 105 {'superpowers': 14, 'gsd2': 12, 'aider': 39, 'gstack': 40}
mechanisms_jsonl 509 {'aider': 156, 'gsd2': 96, 'gstack': 160, 'superpowers': 97}
inventory_status {
  ('superpowers', 'reviewed'): 14,
  ('gsd2', 'reviewed'): 12,
  ('aider', 'reviewed'): 39,
  ('gstack', 'reviewed'): 40,
  ('swe-agent', 'queued'): 29
}
```

## 2026-05-13 SWE-agent Completion Check

Fresh commands executed from `/Volumes/xtaxrich/03-TEMPLATES/xtaxharness`:

```bash
python3 research_cleaning_harness/scripts/validate_source_cards.py
python3 research_cleaning_harness/scripts/validate_yaml.py
python3 research_cleaning_harness/scripts/validate_clean_data.py
python3 -m unittest discover research_cleaning_harness/tests
```

Observed output:

```text
validated 134 source card(s), failures: 0
validated 1 yaml file(s), failures: 0
validated clean data, failures: 0
Ran 14 tests in 0.055s
OK
```

Additional audit:

```text
source_cards_jsonl 134 {'aider': 39, 'gsd2': 12, 'gstack': 40, 'superpowers': 14, 'swe-agent': 29}
mechanisms_jsonl 625 {'aider': 156, 'gsd2': 96, 'gstack': 160, 'superpowers': 97, 'swe-agent': 116}
source_card_files 134
review_files 134
inventory_status {
  ('superpowers', 'reviewed'): 14,
  ('gsd2', 'reviewed'): 12,
  ('aider', 'reviewed'): 39,
  ('gstack', 'reviewed'): 40,
  ('swe-agent', 'reviewed'): 29
}
```

## 2026-05-13 Lightweight iOS Harness Generation Check

Fresh commands executed from `/Volumes/xtaxrich/03-TEMPLATES/xtaxharness`:

```bash
python3 research_cleaning_harness/generated/ios_app_harness/scripts/validate_harness.py
python3 research_cleaning_harness/scripts/validate_source_cards.py
python3 research_cleaning_harness/scripts/validate_yaml.py
python3 research_cleaning_harness/scripts/validate_clean_data.py
python3 -m unittest discover research_cleaning_harness/tests
```

Observed output:

```text
validated ios_app_harness, failures: 0
validated 134 source card(s), failures: 0
validated 1 yaml file(s), failures: 0
validated clean data, failures: 0
Ran 14 tests in 0.045s
OK
```

Additional audit:

```text
source_traces 134 {'gstack': 40, 'aider': 39, 'swe-agent': 29, 'superpowers': 14, 'gsd2': 12}
mechanism_target_rows 629 {'gstack': 160, 'aider': 156, 'swe-agent': 116, 'superpowers': 101, 'gsd2': 96}
generated_harness_files 41
mapped_harness_files 94
framework_summaries 5
mechanism_group_docs 7
failure_mode_docs 25
```

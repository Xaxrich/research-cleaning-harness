# GitHub Publishing Notes

Target: publish `research_cleaning_harness/` as a public GitHub repository.

## Intended Repository Scope

Publish this directory:

```text
research_cleaning_harness/
```

Do not publish the sibling `raw/` directory by default.

Reason: `raw/` is immutable evidence and may include unreviewed research material. The public project should expose cleaned assets, schemas, validators and progress state.

## Published Repository

Public repository:

```text
https://github.com/Xaxrich/research-cleaning-harness
```

Remote:

```text
git@github.com:Xaxrich/research-cleaning-harness.git
```

The repository was created with `gh repo create` and pushed with SSH because HTTPS push failed and `gh auth status` still reports an invalid API token.

## Local Project Status

The local Git project is prepared:

```text
repository: research_cleaning_harness/
initial project commit: 30eb9a7 Add research cleaning harness
publish commit: a3957a7 Generate lightweight iOS app harness
published to GitHub: yes
```

## Push Command

From the parent workspace:

```bash
cd research_cleaning_harness
git status --short
GIT_SSH_COMMAND='ssh -i ~/.ssh/id_ed25519_xtaxharness_github -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new' git push
```

## Pre-Publish Checks

Run before creating the public repository:

```bash
python3 scripts/validate_source_cards.py
python3 scripts/validate_yaml.py
python3 scripts/validate_clean_data.py
python3 -m unittest discover tests
```

Expected current result:

```text
validated 134 source card(s), failures: 0
validated 1 yaml file(s), failures: 0
validated clean data, failures: 0
Ran 14 tests ... OK
```

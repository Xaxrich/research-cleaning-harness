# GitHub Publishing Notes

Target: publish `research_cleaning_harness/` as a public GitHub repository.

## Intended Repository Scope

Publish this directory:

```text
research_cleaning_harness/
```

Do not publish the sibling `raw/` directory by default.

Reason: `raw/` is immutable evidence and may include unreviewed research material. The public project should expose cleaned assets, schemas, validators and progress state.

## Current Blocker

`gh` is installed, but authentication is not currently valid:

```text
gh auth status
github.com
  X Failed to log in to github.com account Xaxrich (default)
  - The token in default is invalid.
  - To re-authenticate, run: gh auth login -h github.com
```

Until GitHub authentication is refreshed, this agent cannot create or push a public repository from the local machine.

## Publish Commands After Auth

From the parent workspace:

```bash
cd research_cleaning_harness
git init
git add .
git commit -m "Add research cleaning harness"
gh repo create research-cleaning-harness --public --source=. --remote=origin --push
```

If the repository should belong to an organization, use:

```bash
gh repo create ORG/research-cleaning-harness --public --source=. --remote=origin --push
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

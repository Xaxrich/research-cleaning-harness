# FILE SCOPE RULES

## Required Fields

Every task must define:

- `allowed_files`
- `read_only_files`
- `forbidden_files`

## Defaults By Task Type

| task_type | allowed examples | read-only examples | forbidden/high-risk examples |
|---|---|---|---|
| docs | `agent_harness/layers/**/*.md`, docs | app config | secrets, signing |
| flutter_ui | `lib/**`, targeted `test/**` | `pubspec.yaml`, design docs | `ios/**`, Firebase production config |
| swift_bridge | `ios/**`, bridge caller files | Flutter callers, docs | signing files, production credentials |
| firebase_rules | `firestore.rules`, `storage.rules`, tests | schema docs | service account keys |
| tests | `test/**`, `integration_test/**` | source under test | release/signing |
| release | checklist, release notes | build logs | upload/signing without approval |

## Rule

If a file is not explicitly allowed, do not edit it.

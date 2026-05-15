# FILE SCOPE RULES

## Required Fields

Every task must define:

- `allowed_files`
- `read_only_files`
- `forbidden_files`

## Defaults By Task Type

| task_type | allowed examples | read-only examples | forbidden/high-risk examples |
|---|---|---|---|
| discovery | `agent_harness/layers/00_goal/*.md` | app source, config | secrets, signing |
| planning | `agent_harness/layers/01_planning/**/*.md`, task drafts | app source, config | secrets, signing |
| docs | `agent_harness/layers/**/*.md`, docs | app config | secrets, signing |
| flutter_ui | `lib/**`, targeted `test/**` | `pubspec.yaml`, design docs | `ios/**`, Firebase production config |
| swiftui_ui | targeted SwiftUI view, preview, UI test | project settings, Info.plist | signing, entitlements without approval |
| local_data | model/store files, targeted tests | UI screens using the store | destructive migrations without approval |
| swift_bridge | `ios/**`, bridge caller files | Flutter callers, docs | signing files, production credentials |
| firebase_rules | `firestore.rules`, `storage.rules`, tests | schema docs | service account keys |
| tests | `test/**`, `integration_test/**` | source under test | release/signing |
| release | checklist, release notes | build logs | upload/signing without approval |

## Rule

If a file is not explicitly allowed, do not edit it.

For implementation tasks, `allowed_files` should be narrower than the default examples. Defaults are starting points, not permission to edit broad directories.

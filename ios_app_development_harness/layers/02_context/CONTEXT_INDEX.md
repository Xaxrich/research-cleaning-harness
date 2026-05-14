# CONTEXT INDEX

This file tells agents what to read for each task type.

## Always Read

- `agent_harness/layers/08_memory_state/STATE.md`
- Current task in `agent_harness/layers/01_task/TASKS.md`
- `agent_harness/layers/03_file_scope/FILE_SCOPE_RULES.md`
- `agent_harness/layers/06_verification/VERIFICATION_MATRIX.md`

## Task Context

| task_type | required context | optional context |
|---|---|---|
| docs | `PRODUCT_SPEC.md`, relevant docs | repo README |
| flutter_ui | target widget file, target test, `pubspec.yaml` | design docs |
| swift_bridge | target Swift/ObjC file, Flutter caller, Info.plist if relevant | Xcode build settings |
| firebase_rules | rules file, rules tests, schema docs | emulator docs |
| tests | failing test, source under test | test helpers |
| bugfix | reproduction evidence, failing test/log | related code search |
| release | `IOS_RELEASE_CHECKLIST.md`, build/test evidence | App Store metadata |

## Do Not Load By Default

- signing secrets
- production credentials
- unrelated generated files
- entire large files when line windows are enough

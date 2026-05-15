# CONTEXT INDEX

This file tells agents what to read for each task type.

## Always Read

- `agent_harness/layers/08_memory_state/STATE.md`
- Current task in `agent_harness/layers/01_task/TASKS.md`
- `agent_harness/layers/00_goal/DISCOVERY_GATE.md`
- `agent_harness/layers/00_goal/PRODUCT_BRIEF.md`
- `agent_harness/layers/01_planning/SOLUTION_PLAN.md`
- `agent_harness/layers/01_planning/TASK_BREAKDOWN.md`
- `agent_harness/layers/01_planning/USER_CONFIRMATION.md`
- `agent_harness/layers/03_file_scope/FILE_SCOPE_RULES.md`
- `agent_harness/layers/06_verification/VERIFICATION_MATRIX.md`
- `agent_harness/layers/06_verification/MODULE_VERIFICATION_POLICY.md`
- `agent_harness/layers/06_verification/SIMULATOR_TEST_POLICY.md`

## Task Context

| task_type | required context | optional context |
|---|---|---|
| discovery | `DISCOVERY_GATE.md`, `PRODUCT_BRIEF.md`, user request | repo README |
| planning | confirmed product brief, `SOLUTION_PLAN.md`, `TASK_BREAKDOWN.md` | architecture docs |
| docs | `PRODUCT_SPEC.md`, relevant docs | repo README |
| flutter_ui | target widget file, target test, `pubspec.yaml` | design docs |
| swift_bridge | target Swift/ObjC file, Flutter caller, Info.plist if relevant | Xcode build settings |
| swiftui_ui | target SwiftUI view, preview/test, app navigation entry | design docs |
| local_data | model/store file, persistence tests | schema docs |
| firebase_rules | rules file, rules tests, schema docs | emulator docs |
| tests | failing test, source under test | test helpers |
| bugfix | reproduction evidence, failing test/log | related code search |
| release | `IOS_RELEASE_CHECKLIST.md`, build/test evidence | App Store metadata |

## Do Not Load By Default

- signing secrets
- production credentials
- unrelated generated files
- entire large files when line windows are enough
- raw research files unless the active task explicitly asks for framework research evidence

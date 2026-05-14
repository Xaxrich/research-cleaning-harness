# VERIFICATION MATRIX

| task_type | minimum verification | stronger verification |
|---|---|---|
| docs | `git diff -- <docs>` | link/schema check |
| flutter_ui | `flutter analyze`, targeted `flutter test` | screenshot/golden/manual simulator |
| swift_bridge | `xcodebuild build` or targeted test | simulator flow |
| firebase_rules | emulator/rules tests | staging dry run |
| tests | failing test now passes | related suite |
| bugfix | reproduce then fix | regression test |
| release | checklist + build/test evidence | manual approval |

## Completion Rule

Final response must include command, result, and remaining risk.

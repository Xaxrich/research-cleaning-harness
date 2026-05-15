# VERIFICATION MATRIX

| task_type | minimum verification | stronger verification |
|---|---|---|
| discovery | product brief diff + user confirmation status | review against `DISCOVERY_GATE.md` |
| planning | solution plan/task breakdown diff + user confirmation status | review against module verification policy |
| docs | `git diff -- <docs>` | link/schema check |
| pure_logic | targeted unit test | related suite |
| local_data | unit/persistence test | migration/serialization test |
| swiftui_ui | build + simulator smoke evidence | XCUITest or screenshot evidence |
| flutter_ui | `flutter analyze`, targeted `flutter test` | screenshot/golden/manual simulator |
| swift_bridge | `xcodebuild build` or targeted test | simulator flow |
| firebase_rules | emulator/rules tests | staging dry run |
| tests | failing test now passes | related suite |
| bugfix | reproduce then fix | regression test |
| release | checklist + build/test evidence | manual approval |

## Verification Levels

Use `MODULE_VERIFICATION_POLICY.md` to choose:

```text
diff
unit
build
simulator
device
manual
```

Use `SIMULATOR_TEST_POLICY.md` to decide when simulator/device evidence is mandatory.

## Completion Rule

Final response must include command, result, verification level met, simulator/device evidence when required, and remaining risk.

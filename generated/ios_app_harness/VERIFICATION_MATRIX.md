# VERIFICATION MATRIX

| task_type | minimum checks | stronger checks |
|---|---|---|
| flutter_ui | `flutter analyze`, targeted widget/unit tests | golden/screenshot/manual simulator check |
| firebase_rules | emulator rules tests | staging dry-run |
| swift_bridge | iOS build or targeted native tests | simulator flow |
| bugfix | failing test reproduced then passing | regression test |
| release | checklist, privacy check, build evidence | TestFlight/release dry run with approval |
| docs-only | link/schema validation | reviewer pass |

## Completion Rule

Do not claim completion unless the final answer includes commands run, exit status and unresolved risk.

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-AID-021 | aider | F_AID_006 | v0_1 | Lint Command Gate |
| M-AID-022 | aider | F_AID_006 | v0_1 | Test Command Gate |
| M-AID-057 | aider | F_AID_015 | v0_1 | Lint Command Gate |
| M-AID-058 | aider | F_AID_015 | v0_1 | Test Command Gate |
| M-AID-097 | aider | F_AID_025 | v0_1 | Lint Command Gate |
| M-AID-098 | aider | F_AID_025 | v0_1 | Test Command Gate |
| M-GSD-045 | gsd2 | F_GSD_006 | v0_1 | Verification Gate Completion |
| M-GSD-049 | gsd2 | F_GSD_007 | v0_1 | Verification and Recovery Binding |
| M-GSD-062 | gsd2 | F_GSD_008 | v0_1 | Verification Evidence Gate |
| M-GSD-082 | gsd2 | F_GSD_011 | v0_1 | Artifact Missing Path Detection |
| M-GST-037 | gstack | F_GST_010 | v0_1 | Continue Check Template |
| M-GST-041 | gstack | F_GST_011 | v0_1 | Continue Check Template |
| M-GST-045 | gstack | F_GST_012 | v0_1 | Continue Check Template |
| M-GST-071 | gstack | F_GST_018 | v0_1 | Stepwise Execution Protocol |
| M-GST-074 | gstack | F_GST_019 | v0_1 | Typed Workflow Gate |
| M-GST-078 | gstack | F_GST_020 | v0_1 | Typed Workflow Gate |
| M-GST-082 | gstack | F_GST_021 | v0_1 | Typed Workflow Gate |
| M-GST-086 | gstack | F_GST_022 | v0_1 | Typed Workflow Gate |
| M-GST-090 | gstack | F_GST_023 | v0_1 | Typed Workflow Gate |
| M-GST-094 | gstack | F_GST_024 | v0_1 | Typed Workflow Gate |
| M-GST-114 | gstack | F_GST_029 | v0_1 | Typed Workflow Gate |
| M-SWE-051 | swe-agent | F_SWE_013 | v0_1 | Environment Feedback Reliance |
| M-SWE-059 | swe-agent | F_SWE_015 | v0_1 | Environment Feedback Reliance |
| M-SWE-078 | swe-agent | F_SWE_020 | v0_1 | Verification Command Matrix |

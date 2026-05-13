# REVIEW MATRIX

| change_type | required review | blocking checks |
|---|---|---|
| docs-only | orchestrator | source trace and no unsupported claims |
| Flutter UI | flutter_ui + mobile_qa | analyze/test evidence |
| Firebase rules | firebase_backend + security_privacy | emulator/rules test evidence |
| Swift bridge | swift_interop + mobile_qa | build/test evidence |
| privacy/capabilities | security_privacy | privacy checklist |
| release | app_store_release + security_privacy + mobile_qa | release checklist and manual approval |

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-GST-057 | gstack | F_GST_015 | v0_1 | Review Matrix by Change Type |
| M-GST-126 | gstack | F_GST_032 | v0_1 | Design Review Gate |
| M-AID-048 | aider | F_AID_012 | v0_5 | Rule Drift Review |
| M-AID-080 | aider | F_AID_020 | v0_5 | Rule Drift Review |
| M-AID-084 | aider | F_AID_021 | v0_5 | Rule Drift Review |
| M-AID-088 | aider | F_AID_022 | v0_5 | Rule Drift Review |
| M-AID-092 | aider | F_AID_023 | v0_5 | Rule Drift Review |
| M-GSD-061 | gsd2 | F_GSD_008 | v0_5 | Weak-Model Branch and Strong-Model Review |

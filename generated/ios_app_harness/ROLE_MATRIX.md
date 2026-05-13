# ROLE MATRIX

| role | owns | can approve | must escalate |
|---|---|---|---|
| orchestrator | task framing, scope, state | low-risk task plan | ambiguous or cross-domain tasks |
| flutter_ui | Flutter UI and widget tests | local UI changes | native bridge or release changes |
| firebase_backend | Firebase rules/functions/config | emulator-tested backend changes | production credentials |
| swift_interop | iOS native bridge, entitlements review | native code with tests | signing, privacy, release |
| mobile_qa | verification matrix and test evidence | test evidence sufficiency | missing device/simulator evidence |
| security_privacy | secrets, privacy, permissions | privacy/risk gate | external upload or credential access |
| app_store_release | release checklist and metadata | release readiness docs | upload/submission actions |

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-GST-005 | gstack | F_GST_002 | v0_1 | Specialized Agent Role Card |
| M-GST-009 | gstack | F_GST_003 | v0_1 | Specialized Agent Role Card |
| M-GST-013 | gstack | F_GST_004 | v0_1 | Specialized Agent Role Card |
| M-GST-017 | gstack | F_GST_005 | v0_1 | Specialized Agent Role Card |
| M-GST-021 | gstack | F_GST_006 | v0_1 | Specialized Agent Role Card |
| M-GST-025 | gstack | F_GST_007 | v0_1 | Specialized Agent Role Card |
| M-GST-029 | gstack | F_GST_008 | v0_1 | Specialized Agent Role Card |
| M-GST-033 | gstack | F_GST_009 | v0_1 | Specialized Agent Role Card |
| M-GST-054 | gstack | F_GST_014 | v0_1 | Release Role Collaboration |
| M-GST-065 | gstack | F_GST_017 | v0_1 | Role Matrix Governance |
| M-GST-097 | gstack | F_GST_025 | v0_1 | Virtual Engineering Team Model |
| M-GST-101 | gstack | F_GST_026 | v0_1 | Virtual Engineering Team Model |
| M-GST-105 | gstack | F_GST_027 | v0_1 | Virtual Engineering Team Model |
| M-GST-109 | gstack | F_GST_028 | v0_1 | Virtual Engineering Team Model |
| M-GST-149 | gstack | F_GST_038 | v0_1 | Role Matrix Governance |
| M-AID-067 | aider | F_AID_017 | v0_5 | Four-Framework Role Composition |
| M-AID-075 | aider | F_AID_019 | v0_5 | Four-Framework Role Composition |
| M-AID-139 | aider | F_AID_035 | v0_5 | Four-Framework Role Composition |

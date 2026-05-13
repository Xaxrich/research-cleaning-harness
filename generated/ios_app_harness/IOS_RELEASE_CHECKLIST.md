# IOS RELEASE CHECKLIST

Release work is high-risk. Preparation can be agent-assisted; submission/upload requires manual approval.

| area | check |
|---|---|
| build | clean release build evidence |
| tests | required tests passed |
| privacy | Info.plist, privacy manifest and permissions reviewed |
| Firebase | rules/config reviewed and tested |
| signing | certificates/profiles handled manually |
| App Store | metadata, screenshots, version, compliance reviewed |
| rollback | rollback or hotfix plan exists |

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-AID-034 | aider | F_AID_009 | v0_1 | iOS-Specific Risk Review |
| M-AID-047 | aider | F_AID_012 | v0_1 | Platform-Specific Risk Rules |
| M-AID-079 | aider | F_AID_020 | v0_1 | Platform-Specific Risk Rules |
| M-AID-083 | aider | F_AID_021 | v0_1 | Platform-Specific Risk Rules |
| M-AID-087 | aider | F_AID_022 | v0_1 | Platform-Specific Risk Rules |
| M-AID-091 | aider | F_AID_023 | v0_1 | Platform-Specific Risk Rules |
| M-GST-038 | gstack | F_GST_010 | v0_1 | Domain-Specific Gate |
| M-GST-042 | gstack | F_GST_011 | v0_1 | Domain-Specific Gate |
| M-GST-046 | gstack | F_GST_012 | v0_1 | Domain-Specific Gate |
| M-GST-053 | gstack | F_GST_014 | v0_1 | App Store Release Gate |
| M-GST-055 | gstack | F_GST_014 | v0_1 | Release Flow Visualization |
| M-SUP-067 | superpowers | F_SUP_011 | v0_5 | Release Checklist Gate |

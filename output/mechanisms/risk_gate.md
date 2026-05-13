# Mechanism: Risk Gate

## Essence

This mechanism group is synthesized from reviewed Source Cards and materialized into the lightweight iOS Harness.

## Target Files

| harness_file | mechanism_targets |
| --- | --- |
| RISK_CONTROL.md | 34 |
| IOS_RELEASE_CHECKLIST.md | 12 |
| HIGH_RISK_FILES.md | 6 |
| docs/agent/RISK_GATE.md | 6 |

## Source Framework Contributions

| framework | mechanism_targets |
| --- | --- |
| gstack | 28 |
| swe-agent | 14 |
| aider | 9 |
| superpowers | 7 |

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-AID-034 | aider | F_AID_009 | v0_1 | iOS-Specific Risk Review |
| M-AID-047 | aider | F_AID_012 | v0_1 | Platform-Specific Risk Rules |
| M-AID-051 | aider | F_AID_013 | v0_1 | Forbidden Files Guard |
| M-AID-079 | aider | F_AID_020 | v0_1 | Platform-Specific Risk Rules |
| M-AID-083 | aider | F_AID_021 | v0_1 | Platform-Specific Risk Rules |
| M-AID-087 | aider | F_AID_022 | v0_1 | Platform-Specific Risk Rules |
| M-AID-091 | aider | F_AID_023 | v0_1 | Platform-Specific Risk Rules |
| M-AID-111 | aider | F_AID_028 | v0_1 | Forbidden Files Guard |
| M-AID-155 | aider | F_AID_039 | v0_1 | Forbidden Files Guard |
| M-GST-008 | gstack | F_GST_002 | v0_1 | Role Escalation Boundary |
| M-GST-012 | gstack | F_GST_003 | v0_1 | Role Escalation Boundary |
| M-GST-016 | gstack | F_GST_004 | v0_1 | Role Escalation Boundary |
| M-GST-020 | gstack | F_GST_005 | v0_1 | Role Escalation Boundary |
| M-GST-024 | gstack | F_GST_006 | v0_1 | Role Escalation Boundary |
| M-GST-028 | gstack | F_GST_007 | v0_1 | Role Escalation Boundary |
| M-GST-032 | gstack | F_GST_008 | v0_1 | Role Escalation Boundary |
| M-GST-036 | gstack | F_GST_009 | v0_1 | Role Escalation Boundary |
| M-GST-038 | gstack | F_GST_010 | v0_1 | Domain-Specific Gate |
| M-GST-042 | gstack | F_GST_011 | v0_1 | Domain-Specific Gate |
| M-GST-046 | gstack | F_GST_012 | v0_1 | Domain-Specific Gate |
| M-GST-053 | gstack | F_GST_014 | v0_1 | App Store Release Gate |
| M-GST-055 | gstack | F_GST_014 | v0_1 | Release Flow Visualization |
| M-GST-056 | gstack | F_GST_014 | v0_1 | Release Blocker Policy |
| M-GST-059 | gstack | F_GST_015 | v0_1 | Severity and Confidence Reporting |
| M-GST-063 | gstack | F_GST_016 | v0_1 | Risk Matrix for Commands |
| M-GST-066 | gstack | F_GST_017 | v0_1 | Decision and Blocking Rights |
| M-GST-075 | gstack | F_GST_019 | v0_1 | Escalation Path per Workflow |
| M-GST-079 | gstack | F_GST_020 | v0_1 | Escalation Path per Workflow |
| M-GST-083 | gstack | F_GST_021 | v0_1 | Escalation Path per Workflow |
| M-GST-087 | gstack | F_GST_022 | v0_1 | Escalation Path per Workflow |
| M-GST-091 | gstack | F_GST_023 | v0_1 | Escalation Path per Workflow |
| M-GST-095 | gstack | F_GST_024 | v0_1 | Escalation Path per Workflow |

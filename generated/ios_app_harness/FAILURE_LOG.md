# FAILURE LOG

Record failures here instead of retrying silently.

| time | task_id | command/action | failure_class | next_action | owner |
|---|---|---|---|---|---|

## Failure Classes

- context_pollution
- wrong_file_edit
- no_test_completion
- stuck_loop
- unsafe_command
- weak_model_overreach
- release_risk
- privacy_leak

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-AID-064 | aider | F_AID_016 | v0_1 | Escalation on Scope Breach |
| M-AID-104 | aider | F_AID_026 | v0_1 | Escalation on Scope Breach |
| M-GSD-055 | gsd2 | F_GSD_008 | v0_1 | Stuck Loop Taxonomy |
| M-GSD-057 | gsd2 | F_GSD_008 | v0_1 | Failure Root Cause Classification |
| M-GSD-084 | gsd2 | F_GSD_011 | v0_1 | Retry Cap Policy |
| M-GST-072 | gstack | F_GST_018 | v0_1 | Failure Escalation Rule |
| M-SWE-100 | swe-agent | F_SWE_025 | v0_1 | Escalation Decision Tree |
| M-AID-023 | aider | F_AID_006 | v0_5 | Reflection Fix Loop |
| M-AID-059 | aider | F_AID_015 | v0_5 | Reflection Fix Loop |
| M-AID-099 | aider | F_AID_025 | v0_5 | Reflection Fix Loop |
| M-GSD-043 | gsd2 | F_GSD_006 | v0_5 | Auto Mode and Recovery Loop |
| M-GSD-054 | gsd2 | F_GSD_007 | v0_5 | Progressive Routing |
| M-GSD-064 | gsd2 | F_GSD_008 | v0_5 | Auto-Fix Retry Bound |
| M-GSD-095 | gsd2 | F_GSD_012 | v0_5 | Failure Escalation with Context Policy |
| M-SWE-019 | swe-agent | F_SWE_005 | v0_5 | Tool-Level Error Semantics |
| M-SWE-035 | swe-agent | F_SWE_009 | v0_5 | Loop Termination Criteria |
| M-SWE-043 | swe-agent | F_SWE_011 | v0_5 | Loop Termination Criteria |
| M-SWE-047 | swe-agent | F_SWE_012 | v0_5 | Loop Termination Criteria |

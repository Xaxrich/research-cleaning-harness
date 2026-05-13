# RISK CONTROL

## Risk Levels

| level | examples | action |
|---|---|---|
| low | local docs, small UI copy, tests | proceed with task card |
| medium | code edits, refactors, dependency changes | require verification evidence |
| high | Firebase rules, native bridge, privacy metadata | require role review |
| release_blocking | signing, upload, App Store submission, production data | manual approval |

## Command Policy

- Allowed: read-only search, bounded file view, local tests, analyze commands.
- Ask first: dependency installs, networked commands, signing, release builds.
- Deny by default: credential reads, destructive file operations, production upload.

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-GST-008 | gstack | F_GST_002 | v0_1 | Role Escalation Boundary |
| M-GST-012 | gstack | F_GST_003 | v0_1 | Role Escalation Boundary |
| M-GST-016 | gstack | F_GST_004 | v0_1 | Role Escalation Boundary |
| M-GST-020 | gstack | F_GST_005 | v0_1 | Role Escalation Boundary |
| M-GST-024 | gstack | F_GST_006 | v0_1 | Role Escalation Boundary |
| M-GST-028 | gstack | F_GST_007 | v0_1 | Role Escalation Boundary |
| M-GST-032 | gstack | F_GST_008 | v0_1 | Role Escalation Boundary |
| M-GST-036 | gstack | F_GST_009 | v0_1 | Role Escalation Boundary |
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
| M-GST-115 | gstack | F_GST_029 | v0_1 | Escalation Path per Workflow |
| M-GST-143 | gstack | F_GST_036 | v0_1 | Risk Matrix for Commands |
| M-GST-150 | gstack | F_GST_038 | v0_1 | Decision and Blocking Rights |
| M-SWE-004 | swe-agent | F_SWE_001 | v0_1 | Duplicate Report Warning |
| M-SWE-020 | swe-agent | F_SWE_005 | v0_1 | ACI Security Envelope |
| M-SWE-028 | swe-agent | F_SWE_007 | v0_1 | Privacy-Aware Logging |

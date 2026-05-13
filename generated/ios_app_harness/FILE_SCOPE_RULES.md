# FILE SCOPE RULES

## File Sets

| set | meaning | behavior |
|---|---|---|
| allowed_files | files the agent may edit | edit only after inspection |
| read_only_files | files the agent may read but not modify | context only |
| forbidden_files | files the agent may neither read broadly nor edit | require escalation |

## iOS Defaults

| task_type | editable examples | read-only examples | forbidden or high-risk examples |
|---|---|---|---|
| flutter_ui | `lib/**`, related tests | `pubspec.yaml`, design docs | signing, secrets, release metadata |
| firebase_rules | `firebase.rules`, tests | Firebase docs, schema docs | production credentials |
| swift_bridge | `ios/**`, platform channel files | Flutter caller files | entitlements without approval |
| tests | `test/**`, `integration_test/**` | source under test | production config |
| release | metadata/checklists only | build logs, privacy docs | upload/signing without manual approval |

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-AID-051 | aider | F_AID_013 | v0_1 | Forbidden Files Guard |
| M-AID-052 | aider | F_AID_013 | v0_1 | Task-Type File Scope Table |
| M-AID-111 | aider | F_AID_028 | v0_1 | Forbidden Files Guard |
| M-AID-112 | aider | F_AID_028 | v0_1 | Task-Type File Scope Table |
| M-AID-155 | aider | F_AID_039 | v0_1 | Forbidden Files Guard |
| M-AID-156 | aider | F_AID_039 | v0_1 | Task-Type File Scope Table |
| M-SWE-072 | swe-agent | F_SWE_018 | v0_1 | Search Scope Guard |
| M-SWE-075 | swe-agent | F_SWE_019 | v0_1 | Forbidden and High-Risk Files Matrix |
| M-GST-062 | gstack | F_GST_016 | v0_5 | Directory Freeze |
| M-GST-142 | gstack | F_GST_036 | v0_5 | Directory Freeze |

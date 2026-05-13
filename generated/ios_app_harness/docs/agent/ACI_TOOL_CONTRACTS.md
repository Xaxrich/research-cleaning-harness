# ACI TOOL CONTRACTS

Each tool must define input, output, failure modes, safety level and trajectory event.

| tool | purpose | risk | output |
|---|---|---|---|
| `view_file.sh` | bounded line-window file read | low | line-numbered content |
| `search_code.sh` | scoped text/path search | low | path:line matches |
| `safe_edit_check.sh` | pre-edit path/risk check | medium | allow/ask/deny |
| `run_safe_command.sh` | allowlisted verification commands | medium/high | command result |
| `context_pack.sh` | task context manifest | low | context list |

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-AID-042 | aider | F_AID_011 | v0_5 | Task-Type Context Pack |
| M-AID-106 | aider | F_AID_027 | v0_5 | Task-Type Context Pack |
| M-AID-150 | aider | F_AID_038 | v0_5 | Task-Type Context Pack |
| M-GSD-025 | gsd2 | F_GSD_004 | v0_5 | Skills and Scripts as Executable Surface |
| M-GSD-032 | gsd2 | F_GSD_005 | v0_5 | Validation Script Suite |
| M-GSD-063 | gsd2 | F_GSD_008 | v0_5 | iOS Verification Script Matrix |
| M-GSD-071 | gsd2 | F_GSD_009 | v1_0 | CLI/Headless/MCP Surfaces |
| M-GST-061 | gstack | F_GST_016 | v0_5 | Command Guardrail Mode |
| M-GST-076 | gstack | F_GST_019 | v0_5 | Completion Criteria Script |
| M-GST-080 | gstack | F_GST_020 | v0_5 | Completion Criteria Script |
| M-GST-084 | gstack | F_GST_021 | v0_5 | Completion Criteria Script |
| M-GST-088 | gstack | F_GST_022 | v0_5 | Completion Criteria Script |
| M-GST-092 | gstack | F_GST_023 | v0_5 | Completion Criteria Script |
| M-GST-096 | gstack | F_GST_024 | v0_5 | Completion Criteria Script |
| M-GST-116 | gstack | F_GST_029 | v0_5 | Completion Criteria Script |
| M-GST-118 | gstack | F_GST_030 | v0_5 | Command-Skill-Hook Layers |
| M-GST-141 | gstack | F_GST_036 | v0_5 | Command Guardrail Mode |
| M-GST-158 | gstack | F_GST_040 | v0_5 | Command-Skill-Hook Layers |
| M-SUP-029 | superpowers | F_SUP_004 | v0_5 | File-convention Tool Compatibility |
| M-SWE-002 | swe-agent | F_SWE_001 | v0_5 | ACI Runtime Migration Thesis |
| M-SWE-006 | swe-agent | F_SWE_002 | v0_5 | Tool-First Transfer Agenda |
| M-SWE-010 | swe-agent | F_SWE_003 | v0_5 | SWE Owns Action Runtime |
| M-SWE-013 | swe-agent | F_SWE_004 | v0_5 | iOS ACI Tool Suite |
| M-SWE-014 | swe-agent | F_SWE_004 | v0_5 | Tool Contract Schema |

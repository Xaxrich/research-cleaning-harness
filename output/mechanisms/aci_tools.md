# Mechanism: Aci Tools

## Essence

This mechanism group is synthesized from reviewed Source Cards and materialized into the lightweight iOS Harness.

## Target Files

| harness_file | mechanism_targets |
| --- | --- |
| docs/agent/ACI_TOOL_CONTRACTS.md | 34 |
| scripts/agent/view_file.sh | 1 |
| scripts/agent/search_code.sh | 1 |
| scripts/agent/safe_edit_check.sh | 1 |
| scripts/agent/run_safe_command.sh | 1 |

## Source Framework Contributions

| framework | mechanism_targets |
| --- | --- |
| swe-agent | 22 |
| gstack | 11 |
| gsd2 | 4 |
| superpowers | 1 |

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
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
| M-SWE-017 | swe-agent | F_SWE_005 | v0_5 | Agent-Computer Interface Boundary |
| M-SWE-030 | swe-agent | F_SWE_008 | v0_5 | ACI Runtime Migration Thesis |
| M-SWE-034 | swe-agent | F_SWE_009 | v0_5 | Small Tool Surface |
| M-SWE-038 | swe-agent | F_SWE_010 | v0_5 | ACI Runtime Migration Thesis |
| M-SWE-042 | swe-agent | F_SWE_011 | v0_5 | Small Tool Surface |
| M-SWE-046 | swe-agent | F_SWE_012 | v0_5 | Small Tool Surface |
| M-SWE-061 | swe-agent | F_SWE_016 | v0_5 | Agent-Computer Interface Boundary |
| M-SWE-065 | swe-agent | F_SWE_017 | v0_5 | Bounded File Viewer |
| M-SWE-069 | swe-agent | F_SWE_018 | v0_5 | Search Command Interface |
| M-SWE-073 | swe-agent | F_SWE_019 | v0_5 | Safe Edit Check |
| M-SWE-077 | swe-agent | F_SWE_020 | v0_5 | Safe Command Runner |

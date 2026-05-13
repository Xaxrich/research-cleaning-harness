# Failure Mode: state_loss

## Why It Matters

This failure mode appears in 24 mechanism records and must be explicitly guarded in the iOS Harness.

## Primary Guard Files

| harness_file | mechanism_count |
| --- | --- |
| docs/agent/STATE.md | 7 |
| docs/agent/TASKS.md | 2 |
| docs/agent/CONTEXT_RULES.md | 2 |
| docs/agent/ESCALATION_RULES.md | 2 |
| docs/agent/STATE_SCHEMA.md | 1 |
| docs/agent/AUTO_MODE.md | 1 |
| docs/agent/RECOVERY.md | 1 |
| docs/agent/MODEL_ROUTING.md | 1 |
| docs/agent/VERIFICATION_MATRIX.md | 1 |
| AGENTS.md | 1 |
| docs/agent/FILE_PLACEMENT_MAP.md | 1 |
| SKILL.md | 1 |

## Source Evidence

| mechanism | framework | source | summary |
| --- | --- | --- | --- |
| M-GSD-001 | gsd2 | F_GSD_001 | Database-backed Runtime State |
| M-GSD-002 | gsd2 | F_GSD_001 | Milestone Slice Task Hierarchy |
| M-GSD-003 | gsd2 | F_GSD_001 | Fresh Session Execution |
| M-GSD-004 | gsd2 | F_GSD_001 | Orchestrator-controlled Context Injection |
| M-GSD-005 | gsd2 | F_GSD_001 | Auto Mode Dispatch Loop |
| M-GSD-006 | gsd2 | F_GSD_001 | Stuck Loop Detection |
| M-GSD-007 | gsd2 | F_GSD_001 | Crash Recovery With Session Forensics |
| M-GSD-008 | gsd2 | F_GSD_001 | Dynamic Model Routing |
| M-GSD-009 | gsd2 | F_GSD_001 | Verification Gate And Completion Criteria |
| M-GSD-010 | gsd2 | F_GSD_001 | Markdown Projection |
| M-SUP-022 | superpowers | F_SUP_004 | Weak-model Lightweight Migration |
| M-SUP-023 | superpowers | F_SUP_004 | iOS Harness Target Layout |
| M-SUP-024 | superpowers | F_SUP_004 | Mobile Skill Set |
| M-SUP-025 | superpowers | F_SUP_004 | Live Agent Documents |
| M-SUP-026 | superpowers | F_SUP_004 | Shared Verification Scripts |
| M-SUP-027 | superpowers | F_SUP_004 | Task Capability Matrix |
| M-SUP-028 | superpowers | F_SUP_004 | Two-failure Escalation |
| M-SUP-029 | superpowers | F_SUP_004 | File-convention Tool Compatibility |
| M-SUP-050 | superpowers | F_SUP_008 | Persistent Project State Snapshot |
| M-SUP-051 | superpowers | F_SUP_008 | Structured Update Log |
| M-SUP-052 | superpowers | F_SUP_008 | Technical Health Dashboard |
| M-SUP-053 | superpowers | F_SUP_008 | Issue Severity Split |
| M-SUP-054 | superpowers | F_SUP_008 | Release State Tracking |
| M-SUP-055 | superpowers | F_SUP_008 | Dependency State Registry |

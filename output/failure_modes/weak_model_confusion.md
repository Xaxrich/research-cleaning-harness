# Failure Mode: weak_model_confusion

## Why It Matters

This failure mode appears in 33 mechanism records and must be explicitly guarded in the iOS Harness.

## Primary Guard Files

| harness_file | mechanism_count |
| --- | --- |
| MODEL_ROUTING.md | 7 |
| TASKS.md | 5 |
| CONTEXT_RULES.md | 5 |
| CONTEXT_INDEX.md | 4 |
| FAILURE_LOG.md | 4 |
| VERIFICATION_MATRIX.md | 2 |
| docs/agent/WEAK_MODEL_CONTEXT.md | 1 |
| docs/agent/CONTEXT_ROT.md | 1 |
| AGENTS.md | 1 |
| STATE.md | 1 |
| docs/agent/IOS_CONTEXT_PRIORITY.md | 1 |
| scripts/agent/view_file.sh | 1 |

## Source Evidence

| mechanism | framework | source | summary |
| --- | --- | --- | --- |
| M-AID-061 | aider | F_AID_016 | Weak Model File Cap |
| M-AID-062 | aider | F_AID_016 | Weak Model Task Downgrade |
| M-AID-063 | aider | F_AID_016 | Simplified Context Pack |
| M-AID-064 | aider | F_AID_016 | Escalation on Scope Breach |
| M-AID-101 | aider | F_AID_026 | Weak Model File Cap |
| M-AID-102 | aider | F_AID_026 | Weak Model Task Downgrade |
| M-AID-103 | aider | F_AID_026 | Simplified Context Pack |
| M-AID-104 | aider | F_AID_026 | Escalation on Scope Breach |
| M-GSD-046 | gsd2 | F_GSD_007 | Task Card Schema |
| M-GSD-047 | gsd2 | F_GSD_007 | Context Window Binding |
| M-GSD-048 | gsd2 | F_GSD_007 | Model Routing Binding |
| M-GSD-049 | gsd2 | F_GSD_007 | Verification and Recovery Binding |
| M-GSD-050 | gsd2 | F_GSD_007 | Context Priority Bands |
| M-GSD-051 | gsd2 | F_GSD_007 | Excluded Content Rule |
| M-GSD-052 | gsd2 | F_GSD_007 | Weak Model Minimal Context |
| M-GSD-053 | gsd2 | F_GSD_007 | Capability and Budget Routing |
| M-GSD-054 | gsd2 | F_GSD_007 | Progressive Routing |
| M-GSD-073 | gsd2 | F_GSD_010 | Context Rot Failure Taxonomy |
| M-GSD-074 | gsd2 | F_GSD_010 | One Task per Context Window |
| M-GSD-075 | gsd2 | F_GSD_010 | Fresh Session and Context Reset |
| M-GSD-076 | gsd2 | F_GSD_010 | Pre-Inlined Context Injection |
| M-GSD-077 | gsd2 | F_GSD_010 | Excluded Contexts |
| M-GSD-078 | gsd2 | F_GSD_010 | Summary Projection over Chat History |
| M-GSD-079 | gsd2 | F_GSD_010 | Token Profiles |

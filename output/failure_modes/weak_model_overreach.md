# Failure Mode: weak_model_overreach

## Why It Matters

This failure mode appears in 59 mechanism records and must be explicitly guarded in the iOS Harness.

## Primary Guard Files

| harness_file | mechanism_count |
| --- | --- |
| MODEL_ROUTING.md | 9 |
| TASKS.md | 8 |
| docs/agent/TASKS.md | 7 |
| FAILURE_LOG.md | 5 |
| AGENTS.md | 5 |
| CONTEXT_RULES.md | 3 |
| HIGH_RISK_FILES.md | 3 |
| FILE_SCOPE_RULES.md | 3 |
| CONTEXT_INDEX.md | 2 |
| docs/agent/CONTEXT_RULES.md | 2 |
| docs/agent/RISK_GATE.md | 2 |
| docs/agent/STATE_SCHEMA.md | 1 |

## Source Evidence

| mechanism | framework | source | summary |
| --- | --- | --- | --- |
| M-AID-049 | aider | F_AID_013 | Allowed Files Contract |
| M-AID-050 | aider | F_AID_013 | Read-Only Files Contract |
| M-AID-051 | aider | F_AID_013 | Forbidden Files Guard |
| M-AID-052 | aider | F_AID_013 | Task-Type File Scope Table |
| M-AID-061 | aider | F_AID_016 | Weak Model File Cap |
| M-AID-062 | aider | F_AID_016 | Weak Model Task Downgrade |
| M-AID-063 | aider | F_AID_016 | Simplified Context Pack |
| M-AID-064 | aider | F_AID_016 | Escalation on Scope Breach |
| M-AID-101 | aider | F_AID_026 | Weak Model File Cap |
| M-AID-102 | aider | F_AID_026 | Weak Model Task Downgrade |
| M-AID-103 | aider | F_AID_026 | Simplified Context Pack |
| M-AID-104 | aider | F_AID_026 | Escalation on Scope Breach |
| M-AID-109 | aider | F_AID_028 | Allowed Files Contract |
| M-AID-110 | aider | F_AID_028 | Read-Only Files Contract |
| M-AID-111 | aider | F_AID_028 | Forbidden Files Guard |
| M-AID-112 | aider | F_AID_028 | Task-Type File Scope Table |
| M-AID-153 | aider | F_AID_039 | Allowed Files Contract |
| M-AID-154 | aider | F_AID_039 | Read-Only Files Contract |
| M-AID-155 | aider | F_AID_039 | Forbidden Files Guard |
| M-AID-156 | aider | F_AID_039 | Task-Type File Scope Table |
| M-GSD-001 | gsd2 | F_GSD_001 | Database-backed Runtime State |
| M-GSD-002 | gsd2 | F_GSD_001 | Milestone Slice Task Hierarchy |
| M-GSD-003 | gsd2 | F_GSD_001 | Fresh Session Execution |
| M-GSD-004 | gsd2 | F_GSD_001 | Orchestrator-controlled Context Injection |

# Failure Mode: fake_verification

## Why It Matters

This failure mode appears in 29 mechanism records and must be explicitly guarded in the iOS Harness.

## Primary Guard Files

| harness_file | mechanism_count |
| --- | --- |
| VERIFICATION_MATRIX.md | 6 |
| FAILURE_LOG.md | 3 |
| STATE.md | 3 |
| docs/agent/TASKS.md | 2 |
| docs/agent/CONTEXT_RULES.md | 2 |
| docs/agent/STATE.md | 2 |
| docs/agent/STATE_SCHEMA.md | 1 |
| docs/agent/AUTO_MODE.md | 1 |
| docs/agent/ESCALATION_RULES.md | 1 |
| docs/agent/RECOVERY.md | 1 |
| docs/agent/MODEL_ROUTING.md | 1 |
| docs/agent/VERIFICATION_MATRIX.md | 1 |

## Source Evidence

| mechanism | framework | source | summary |
| --- | --- | --- | --- |
| M-AID-021 | aider | F_AID_006 | Lint Command Gate |
| M-AID-022 | aider | F_AID_006 | Test Command Gate |
| M-AID-023 | aider | F_AID_006 | Reflection Fix Loop |
| M-AID-024 | aider | F_AID_006 | Verification Evidence Record |
| M-AID-057 | aider | F_AID_015 | Lint Command Gate |
| M-AID-058 | aider | F_AID_015 | Test Command Gate |
| M-AID-059 | aider | F_AID_015 | Reflection Fix Loop |
| M-AID-060 | aider | F_AID_015 | Verification Evidence Record |
| M-AID-097 | aider | F_AID_025 | Lint Command Gate |
| M-AID-098 | aider | F_AID_025 | Test Command Gate |
| M-AID-099 | aider | F_AID_025 | Reflection Fix Loop |
| M-AID-100 | aider | F_AID_025 | Verification Evidence Record |
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
| M-SUP-030 | superpowers | F_SUP_005 | Selective Principle Extraction |
| M-SUP-031 | superpowers | F_SUP_005 | Explicit Non-transfer List |

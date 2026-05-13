# Failure Mode: stuck_loop

## Why It Matters

This failure mode appears in 73 mechanism records and must be explicitly guarded in the iOS Harness.

## Primary Guard Files

| harness_file | mechanism_count |
| --- | --- |
| FAILURE_LOG.md | 11 |
| STATE.md | 5 |
| VERIFICATION_MATRIX.md | 5 |
| docs/agent/ACI_TOOL_CONTRACTS.md | 5 |
| DECISIONS.md | 5 |
| TASKS.md | 4 |
| MODEL_ROUTING.md | 4 |
| docs/agent/MINI_SWE_LOOP.md | 4 |
| RISK_CONTROL.md | 3 |
| docs/agent/CONTEXT_RULES.md | 2 |
| scripts/agent/stuck_detector.sh | 2 |
| GIT_WORKFLOW.md | 2 |

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
| M-GSD-037 | gsd2 | F_GSD_006 | Research Question Framing |
| M-GSD-038 | gsd2 | F_GSD_006 | GSD2 Runtime Overview |
| M-GSD-039 | gsd2 | F_GSD_006 | Milestone-Slice-Task Hierarchy |
| M-GSD-040 | gsd2 | F_GSD_006 | Fresh Session per Task |
| M-GSD-041 | gsd2 | F_GSD_006 | Context Injection Instead of Chat History |
| M-GSD-042 | gsd2 | F_GSD_006 | Database Truth with Markdown Projection |
| M-GSD-043 | gsd2 | F_GSD_006 | Auto Mode and Recovery Loop |
| M-GSD-044 | gsd2 | F_GSD_006 | Dynamic Model Routing and Token Control |
| M-GSD-045 | gsd2 | F_GSD_006 | Verification Gate Completion |
| M-GSD-055 | gsd2 | F_GSD_008 | Stuck Loop Taxonomy |
| M-GSD-056 | gsd2 | F_GSD_008 | Repeated Try Detection |
| M-GSD-057 | gsd2 | F_GSD_008 | Failure Root Cause Classification |
| M-GSD-058 | gsd2 | F_GSD_008 | Two-Failure Escalation and Blocker Card |
| M-GSD-059 | gsd2 | F_GSD_008 | Work Unit Git Isolation |

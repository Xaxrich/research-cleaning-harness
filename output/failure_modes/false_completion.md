# Failure Mode: false_completion

## Why It Matters

This failure mode appears in 27 mechanism records and must be explicitly guarded in the iOS Harness.

## Primary Guard Files

| harness_file | mechanism_count |
| --- | --- |
| FAILURE_LOG.md | 5 |
| STATE.md | 3 |
| VERIFICATION_MATRIX.md | 3 |
| TASKS.md | 2 |
| scripts/agent/stuck_detector.sh | 2 |
| GIT_WORKFLOW.md | 2 |
| PRODUCT_SPEC.md | 1 |
| ARCHITECTURE.md | 1 |
| CONTEXT_RULES.md | 1 |
| CONTEXT_INDEX.md | 1 |
| MODEL_ROUTING.md | 1 |
| BLOCKERS.md | 1 |

## Source Evidence

| mechanism | framework | source | summary |
| --- | --- | --- | --- |
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
| M-GSD-060 | gsd2 | F_GSD_008 | Task-Level Commit and Rollback |
| M-GSD-061 | gsd2 | F_GSD_008 | Weak-Model Branch and Strong-Model Review |
| M-GSD-062 | gsd2 | F_GSD_008 | Verification Evidence Gate |
| M-GSD-063 | gsd2 | F_GSD_008 | iOS Verification Script Matrix |
| M-GSD-064 | gsd2 | F_GSD_008 | Auto-Fix Retry Bound |
| M-GSD-081 | gsd2 | F_GSD_011 | Multi-Level Stuck Detection |
| M-GSD-082 | gsd2 | F_GSD_011 | Artifact Missing Path Detection |
| M-GSD-083 | gsd2 | F_GSD_011 | Drift Detection |
| M-GSD-084 | gsd2 | F_GSD_011 | Retry Cap Policy |
| M-GSD-085 | gsd2 | F_GSD_011 | Crash Recovery Boundary |

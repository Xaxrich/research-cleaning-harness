# Failure Mode: context_pollution

## Why It Matters

This failure mode appears in 99 mechanism records and must be explicitly guarded in the iOS Harness.

## Primary Guard Files

| harness_file | mechanism_count |
| --- | --- |
| CONTEXT_INDEX.md | 14 |
| TASKS.md | 11 |
| docs/agent/REPO_CONTEXT.md | 7 |
| docs/agent/EDIT_FORMATS.md | 7 |
| MODEL_ROUTING.md | 5 |
| STATE.md | 5 |
| AGENTS.md | 5 |
| CONTEXT_RULES.md | 4 |
| scripts/agent/context_pack.sh | 3 |
| docs/agent/CONTEXT_RULES.md | 3 |
| VERIFICATION_MATRIX.md | 3 |
| docs/agent/WORKFLOW_CHAIN.md | 3 |

## Source Evidence

| mechanism | framework | source | summary |
| --- | --- | --- | --- |
| M-AID-005 | aider | F_AID_002 | Repo-Aware Editing Loop |
| M-AID-006 | aider | F_AID_002 | Explicit Added Files |
| M-AID-007 | aider | F_AID_002 | Read-Only Rule Context |
| M-AID-008 | aider | F_AID_002 | Edit Format Discipline |
| M-AID-009 | aider | F_AID_003 | Repo-Aware Editing Loop |
| M-AID-010 | aider | F_AID_003 | Explicit Added Files |
| M-AID-011 | aider | F_AID_003 | Read-Only Rule Context |
| M-AID-012 | aider | F_AID_003 | Edit Format Discipline |
| M-AID-013 | aider | F_AID_004 | Repo-Aware Editing Loop |
| M-AID-014 | aider | F_AID_004 | Explicit Added Files |
| M-AID-015 | aider | F_AID_004 | Read-Only Rule Context |
| M-AID-016 | aider | F_AID_004 | Edit Format Discipline |
| M-AID-025 | aider | F_AID_007 | Repo-Aware Editing Loop |
| M-AID-026 | aider | F_AID_007 | Explicit Added Files |
| M-AID-027 | aider | F_AID_007 | Read-Only Rule Context |
| M-AID-028 | aider | F_AID_007 | Edit Format Discipline |
| M-AID-029 | aider | F_AID_008 | Repo Map Ranking |
| M-AID-030 | aider | F_AID_008 | Token-Budgeted Repository Context |
| M-AID-031 | aider | F_AID_008 | Dependency Surfacing |
| M-AID-032 | aider | F_AID_008 | Repo Map Boundary |
| M-AID-037 | aider | F_AID_010 | Repo-Aware Editing Loop |
| M-AID-038 | aider | F_AID_010 | Explicit Added Files |
| M-AID-039 | aider | F_AID_010 | Read-Only Rule Context |
| M-AID-040 | aider | F_AID_010 | Edit Format Discipline |

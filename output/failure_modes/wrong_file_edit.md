# Failure Mode: wrong_file_edit

## Why It Matters

This failure mode appears in 98 mechanism records and must be explicitly guarded in the iOS Harness.

## Primary Guard Files

| harness_file | mechanism_count |
| --- | --- |
| TASKS.md | 20 |
| RISK_CONTROL.md | 10 |
| STATE.md | 9 |
| docs/agent/EDIT_FORMATS.md | 8 |
| ROLE_MATRIX.md | 8 |
| docs/agent/REPO_CONTEXT.md | 7 |
| CONTEXT_INDEX.md | 7 |
| HIGH_RISK_FILES.md | 6 |
| CONTEXT_RULES.md | 4 |
| FILE_SCOPE_RULES.md | 3 |
| FAILURE_LOG.md | 3 |
| docs/agent/ACI_TOOL_CONTRACTS.md | 3 |

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
| M-AID-037 | aider | F_AID_010 | Repo-Aware Editing Loop |
| M-AID-038 | aider | F_AID_010 | Explicit Added Files |
| M-AID-039 | aider | F_AID_010 | Read-Only Rule Context |
| M-AID-040 | aider | F_AID_010 | Edit Format Discipline |
| M-AID-049 | aider | F_AID_013 | Allowed Files Contract |
| M-AID-050 | aider | F_AID_013 | Read-Only Files Contract |
| M-AID-051 | aider | F_AID_013 | Forbidden Files Guard |
| M-AID-052 | aider | F_AID_013 | Task-Type File Scope Table |

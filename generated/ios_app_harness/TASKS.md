# TASKS

Use one task card per bounded change.

## Task Card Template

```yaml
task_id:
status: ready
task_type: flutter_ui | firebase_rules | swift_bridge | tests | bugfix | release | docs
owner_role:
risk_level: low | medium | high | release_blocking
goal:
allowed_files: []
read_only_files: []
forbidden_files: []
required_context: []
required_tools: []
verification_commands: []
completion_evidence: []
rollback_plan:
```

## v0.1 Rules

- No task starts without `allowed_files`, `read_only_files` and `forbidden_files`.
- Any high-risk file needs a review gate from `REVIEW_MATRIX.md`.
- Release, privacy, signing, Firebase rules and native bridge work require explicit risk review.
- Failed verification updates `FAILURE_LOG.md` before another attempt.

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-AID-001 | aider | F_AID_001 | v0_1 | Aider Research Pipeline |
| M-AID-006 | aider | F_AID_002 | v0_1 | Explicit Added Files |
| M-AID-010 | aider | F_AID_003 | v0_1 | Explicit Added Files |
| M-AID-014 | aider | F_AID_004 | v0_1 | Explicit Added Files |
| M-AID-018 | aider | F_AID_005 | v0_1 | Atomic Commit Boundary |
| M-AID-026 | aider | F_AID_007 | v0_1 | Explicit Added Files |
| M-AID-038 | aider | F_AID_010 | v0_1 | Explicit Added Files |
| M-AID-049 | aider | F_AID_013 | v0_1 | Allowed Files Contract |
| M-AID-054 | aider | F_AID_014 | v0_1 | Atomic Commit Boundary |
| M-AID-061 | aider | F_AID_016 | v0_1 | Weak Model File Cap |
| M-AID-094 | aider | F_AID_024 | v0_1 | Atomic Commit Boundary |
| M-AID-101 | aider | F_AID_026 | v0_1 | Weak Model File Cap |
| M-AID-109 | aider | F_AID_028 | v0_1 | Allowed Files Contract |
| M-AID-114 | aider | F_AID_029 | v0_1 | Atomic Commit Boundary |
| M-AID-118 | aider | F_AID_030 | v0_1 | Explicit Added Files |
| M-AID-122 | aider | F_AID_031 | v0_1 | Atomic Commit Boundary |
| M-AID-126 | aider | F_AID_032 | v0_1 | Explicit Added Files |
| M-AID-134 | aider | F_AID_034 | v0_1 | Atomic Commit Boundary |
| M-AID-153 | aider | F_AID_039 | v0_1 | Allowed Files Contract |
| M-GSD-016 | gsd2 | F_GSD_003 | v0_1 | Staged Research Pipeline |
| M-GSD-039 | gsd2 | F_GSD_006 | v0_1 | Milestone-Slice-Task Hierarchy |
| M-GSD-046 | gsd2 | F_GSD_007 | v0_1 | Task Card Schema |
| M-GSD-060 | gsd2 | F_GSD_008 | v0_1 | Task-Level Commit and Rollback |
| M-GST-006 | gstack | F_GST_002 | v0_1 | Role-Specific File Ownership |

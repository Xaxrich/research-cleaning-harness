# STATE

phase: ready_for_task_execution
current_task: none
current_role: none
last_updated: 2026-05-13

active_files:
  editable: []
  read_only: []
  forbidden: []

verification:
  required: []
  completed: []
  blocked: []

trajectory:
  enabled: manual
  output: data/trajectory.jsonl

blocked:
  - none

next:
  - create a task card in TASKS.md
  - build context pack from CONTEXT_INDEX.md
  - define allowed/read-only/forbidden files before editing

## Update Rules

- Update before changing task phase.
- Record owner role and verification commands.
- Record failures instead of retrying silently.
- Keep raw research files out of runtime context.

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-GSD-013 | gsd2 | F_GSD_002 | v0_1 | End-to-End Harness Control Stack |
| M-GSD-024 | gsd2 | F_GSD_004 | v0_1 | Model/Failure/Git/Verification Control Files |
| M-GSD-030 | gsd2 | F_GSD_005 | v0_1 | State and Task Templates |
| M-GSD-031 | gsd2 | F_GSD_005 | v0_1 | Routing and Failure Templates |
| M-GSD-042 | gsd2 | F_GSD_006 | v0_1 | Database Truth with Markdown Projection |
| M-GSD-078 | gsd2 | F_GSD_010 | v0_1 | Summary Projection over Chat History |
| M-GST-051 | gstack | F_GST_013 | v0_1 | Long-Running Task Persistence |
| M-GST-123 | gstack | F_GST_031 | v0_1 | Long-Running Task Persistence |
| M-GST-131 | gstack | F_GST_033 | v0_1 | Long-Running Task Persistence |
| M-GST-135 | gstack | F_GST_034 | v0_1 | Long-Running Task Persistence |
| M-GST-139 | gstack | F_GST_035 | v0_1 | Long-Running Task Persistence |
| M-SWE-007 | swe-agent | F_SWE_002 | v0_1 | Evidence-Bound Migration Plan |
| M-AID-024 | aider | F_AID_006 | v0_5 | Verification Evidence Record |
| M-AID-044 | aider | F_AID_011 | v0_5 | Context Pack Audit Header |
| M-AID-060 | aider | F_AID_015 | v0_5 | Verification Evidence Record |
| M-AID-100 | aider | F_AID_025 | v0_5 | Verification Evidence Record |
| M-AID-108 | aider | F_AID_027 | v0_5 | Context Pack Audit Header |
| M-AID-152 | aider | F_AID_038 | v0_5 | Context Pack Audit Header |

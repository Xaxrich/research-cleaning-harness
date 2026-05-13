# AGENTS

## Prime Directive

You are operating inside a lightweight iOS App Harness. Your job is not to be clever with a large context; your job is to move one bounded iOS task through scope, action, verification and handoff with traceable evidence.

## Framework Fusion

| framework | what to use | what not to over-import |
| --- | --- | --- |
| Superpowers | planning, TDD, debugging, review, completion verification | do not turn every small task into a heavy ceremony |
| GSD2 | STATE/TASKS discipline, recovery, routing, model limits | do not build a full runtime before v0.5 |
| Aider | repo context, explicit editable files, read-only rules, Git hygiene | do not use repo map as a substitute for tests |
| gstack | role ownership, review matrix, workflow gates, risk blocking | do not run a multi-agent org for trivial changes |
| SWE-agent | ACI tools, action/observation, safe commands, trajectory | do not claim runtime interception until implemented |

## Mandatory Task Flow

1. Read `STATE.md`, `TASKS.md`, `CONTEXT_INDEX.md`, `FILE_SCOPE_RULES.md`, and the task card.
2. Declare task type, owner role, allowed files, read-only files, forbidden files and verification commands.
3. Inspect before editing. Search before broad reading. Use line-bounded views for large files.
4. Before editing, run or mentally apply `scripts/agent/safe_edit_check.sh`.
5. After editing, run the smallest meaningful checks first, then broaden if risk requires it.
6. Record failures in `FAILURE_LOG.md`; do not loop silently.
7. Do not mark complete without fresh verification evidence.

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-GSD-012 | gsd2 | F_GSD_002 | v0_1 | Runtime Mechanism Transfer Boundary |
| M-GSD-019 | gsd2 | F_GSD_003 | v0_1 | Skill Loading Plan |
| M-GSD-026 | gsd2 | F_GSD_004 | v0_1 | Superpowers-GSD2 Role Split |
| M-GSD-075 | gsd2 | F_GSD_010 | v0_1 | Fresh Session and Context Reset |
| M-GST-050 | gstack | F_GST_013 | v0_1 | User Sovereignty |
| M-GST-122 | gstack | F_GST_031 | v0_1 | User Sovereignty |
| M-GST-130 | gstack | F_GST_033 | v0_1 | User Sovereignty |
| M-GST-134 | gstack | F_GST_034 | v0_1 | User Sovereignty |
| M-GST-138 | gstack | F_GST_035 | v0_1 | User Sovereignty |
| M-SUP-001 | superpowers | F_SUP_001 | v0_1 | Engineering Discipline System |
| M-SUP-010 | superpowers | F_SUP_002 | v0_1 | Single Source Alias |
| M-SUP-014 | superpowers | F_SUP_003 | v0_1 | Three-layer Process Constraint |
| M-SUP-022 | superpowers | F_SUP_004 | v0_1 | Weak-model Lightweight Migration |
| M-SUP-030 | superpowers | F_SUP_005 | v0_1 | Selective Principle Extraction |
| M-SUP-043 | superpowers | F_SUP_007 | v0_1 | Project Entry Contract |
| M-SUP-044 | superpowers | F_SUP_007 | v0_1 | Assistant Behavior Contract |
| M-SUP-045 | superpowers | F_SUP_007 | v0_1 | Skill Navigation Table |
| M-SUP-047 | superpowers | F_SUP_007 | v0_1 | Document Navigation Index |
| M-SUP-048 | superpowers | F_SUP_007 | v0_1 | Verification Command Index |
| M-SUP-064 | superpowers | F_SUP_010 | v0_1 | Constraint-first Migration Scope |

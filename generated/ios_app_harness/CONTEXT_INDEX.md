# CONTEXT INDEX

## Load Order

| tier | files | purpose |
|---|---|---|
| P0 | `STATE.md`, current task in `TASKS.md`, `FILE_SCOPE_RULES.md` | task state and edit boundary |
| P1 | `PRODUCT_SPEC.md`, `CONTEXT_RULES.md`, `ROLE_MATRIX.md`, `VERIFICATION_MATRIX.md` | normal task context |
| P2 | `docs/agent/REPO_CONTEXT.md`, platform convention files, relevant source cards | deeper context when needed |
| P3 | raw research files | avoid by default; use only if clean evidence is missing |

## Context Pack Rule

The context pack should list task id, task type, owner role, files loaded, reason loaded and token/risk estimate.

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-AID-007 | aider | F_AID_002 | v0_1 | Read-Only Rule Context |
| M-AID-011 | aider | F_AID_003 | v0_1 | Read-Only Rule Context |
| M-AID-015 | aider | F_AID_004 | v0_1 | Read-Only Rule Context |
| M-AID-027 | aider | F_AID_007 | v0_1 | Read-Only Rule Context |
| M-AID-039 | aider | F_AID_010 | v0_1 | Read-Only Rule Context |
| M-AID-041 | aider | F_AID_011 | v0_1 | Context Index Layering |
| M-AID-045 | aider | F_AID_012 | v0_1 | Layered Conventions Files |
| M-AID-065 | aider | F_AID_017 | v0_1 | Aider Context Layer Transfer |
| M-AID-073 | aider | F_AID_019 | v0_1 | Aider Context Layer Transfer |
| M-AID-077 | aider | F_AID_020 | v0_1 | Layered Conventions Files |
| M-AID-081 | aider | F_AID_021 | v0_1 | Layered Conventions Files |
| M-AID-085 | aider | F_AID_022 | v0_1 | Layered Conventions Files |
| M-AID-089 | aider | F_AID_023 | v0_1 | Layered Conventions Files |
| M-AID-105 | aider | F_AID_027 | v0_1 | Context Index Layering |
| M-AID-119 | aider | F_AID_030 | v0_1 | Read-Only Rule Context |
| M-AID-127 | aider | F_AID_032 | v0_1 | Read-Only Rule Context |
| M-AID-137 | aider | F_AID_035 | v0_1 | Aider Context Layer Transfer |
| M-AID-141 | aider | F_AID_036 | v0_1 | Aider Context Layer Transfer |
| M-AID-145 | aider | F_AID_037 | v0_1 | Aider Context Layer Transfer |
| M-AID-149 | aider | F_AID_038 | v0_1 | Context Index Layering |
| M-GSD-023 | gsd2 | F_GSD_004 | v0_1 | Agent Document Responsibility Split |
| M-GSD-041 | gsd2 | F_GSD_006 | v0_1 | Context Injection Instead of Chat History |
| M-GSD-050 | gsd2 | F_GSD_007 | v0_1 | Context Priority Bands |
| M-GSD-076 | gsd2 | F_GSD_010 | v0_1 | Pre-Inlined Context Injection |

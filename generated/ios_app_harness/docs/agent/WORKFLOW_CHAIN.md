# WORKFLOW CHAIN

| workflow | phases |
|---|---|
| feature | task card -> context pack -> edit -> tests -> review -> state update |
| bugfix | reproduce -> isolate -> fix -> regression test -> failure log update |
| Firebase | scope -> local/emulator validation -> security review -> evidence |
| Swift interop | scope -> native edit -> build/test -> QA review |
| release | checklist -> risk review -> manual approval -> handoff |

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-SUP-011 | superpowers | F_SUP_002 | v0_1 | Process And Implementation Skill Split |
| M-SUP-020 | superpowers | F_SUP_003 | v0_5 | Process Orchestration Layer |
| M-SUP-062 | superpowers | F_SUP_010 | v0_5 | Staged Research-to-Harness Pipeline |
| M-SUP-093 | superpowers | F_SUP_014 | v0_5 | Layered Workflow Diagram |

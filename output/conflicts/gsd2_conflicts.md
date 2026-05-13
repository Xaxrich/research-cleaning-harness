# GSD2 Conflict Ledger

Scope: reviewed GSD2 Source Cards `F_GSD_001` through `F_GSD_012`.

This file records cross-card tensions that must be resolved before GSD2 mechanisms are merged with Superpowers or transferred into the iOS App Harness.

## Conflict Summary

| conflict_id | conflict | source_cards | synthesis_resolution | iOS Harness implication |
|---|---|---|---|---|
| C-GSD-001 | Full GSD2 runtime vs lightweight iOS Harness v0.1 | F_GSD_001, F_GSD_004, F_GSD_009 | Transfer runtime concepts as Markdown/JSONL controls first; defer SQLite, worker leases and command queue to v1.0. | v0.1 uses `STATE.md`, `TASKS.md`, `VERIFICATION_MATRIX.md`; no DB runtime required. |
| C-GSD-002 | Database truth source vs Markdown projection | F_GSD_001, F_GSD_006, F_GSD_009, F_GSD_010 | Preserve the distinction semantically: Markdown can be the v0.1 truth file, but must be labeled as a future projection candidate. | Avoid pretending v0.1 has DB-backed recovery; write recovery limits explicitly. |
| C-GSD-003 | Worktree isolation vs iOS/Xcode path fragility | F_GSD_008, F_GSD_011, F_SUP_005 | Use branch/worktree/none as risk-based policy, not default worktree. | v0.1 defaults to branch or in-place with diff review; worktree is opt-in for isolated high-risk work. |
| C-GSD-004 | Auto mode and worker orchestration vs single Codex session | F_GSD_001, F_GSD_005, F_GSD_009 | Keep auto mode as design target; implement only manual task state transitions and verification evidence now. | Do not claim autonomous dispatch until runtime scripts and locks exist. |
| C-GSD-005 | Concrete model routing tables vs fast-changing model/provider availability | F_GSD_007, F_GSD_012 | Keep routing structure and capability dimensions; refresh provider/model names before implementation. | `MODEL_ROUTING.md` v0.1 should describe decision rules, not freeze provider SKUs. |
| C-GSD-006 | Comprehensive report duplication vs stage-specific evidence | F_GSD_001, F_GSD_002, F_GSD_006, F_GSD_007, F_GSD_008 | Use comprehensive cards as overview/cross-check; use stage and research cards as primary mechanism evidence. | Framework summary must deduplicate repeated mechanisms. |
| C-GSD-007 | Verification script design vs implemented verification scripts | F_GSD_005, F_GSD_008, F_GSD_011 | Treat script names as target assets until implemented and tested. | v0.5 may create scripts; v0.1 requires command evidence fields only. |

## Precedence Rules

1. Specialized research cards `F_GSD_009` through `F_GSD_012` override overview cards when they provide more precise evidence.
2. Stage cards `F_GSD_004`, `F_GSD_005`, `F_GSD_007`, and `F_GSD_008` are primary sources for iOS file placement and v0.1/v0.5/v1.0 scope.
3. `F_GSD_002` is a delivery cross-check, not a separate source of unique mechanisms unless a diff later proves otherwise.
4. GSD2 runtime-heavy mechanisms must be version-gated; no v0.1 output should imply autonomous dispatch, leases, SQLite, or MCP runtime unless implemented.
5. When GSD2 and Superpowers conflict, keep Superpowers as task-internal engineering method and GSD2 as task/state/context/verification orchestration.

## Required Follow-up During Synthesis

| output | required handling |
|---|---|
| `output/frameworks/gsd2_summary.md` | Include a conflicts section and cite this ledger. |
| `output/mechanisms/task_state_machine.md` | Distinguish v0.1 Markdown task state from v1.0 DB-backed runtime state. |
| `output/mechanisms/repo_context.md` | Merge GSD2 context priority with later Aider repo map evidence. |
| `output/mechanisms/verification.md` | Separate evidence fields from future executable iOS scripts. |
| `output/ios_harness_mapping/v0_1_scope.md` | Exclude full auto mode, SQLite, worker leases and MCP runtime. |


# Aider Conflict Ledger

Scope: reviewed Aider Source Cards `F_AID_001` through `F_AID_039`.

This file records cross-card tensions that must be resolved before Aider mechanisms are merged with Superpowers, GSD2, gstack or SWE-agent.

## Conflict Summary

| conflict_id | conflict | source_cards | synthesis_resolution | iOS Harness implication |
|---|---|---|---|---|
| C-AID-001 | Repo map usefulness vs false confidence | F_AID_008, F_AID_033, F_AID_010 | Keep repo map as context discovery aid, not correctness proof. | Verification gate remains mandatory. |
| C-AID-002 | Added files editing freedom vs strict file scope | F_AID_004, F_AID_013, F_AID_039 | `allowed_files` is authoritative; repo map suggestions stay read-only until admitted. | Task cards must separate related files from editable files. |
| C-AID-003 | Auto-commit convenience vs user dirty worktree safety | F_AID_005, F_AID_014, F_AID_024, F_AID_034 | No automatic commit unless dirty state is recorded and verification evidence exists. | v0.1 uses diff summary; v0.5 can add commit templates. |
| C-AID-004 | Weak model productivity vs weak model overreach | F_AID_016, F_AID_026, F_AID_028 | Weak models receive file caps and escalation triggers. | Cross-layer, release and security work require strong-model review. |
| C-AID-005 | Conventions as context vs conventions drift | F_AID_012, F_AID_020, F_AID_021, F_AID_022, F_AID_023 | Conventions are read-only task context; changing them is high-risk. | Rule changes need review and decision records. |
| C-AID-006 | Script design vs implemented tool enforcement | F_AID_027, F_AID_025, F_AID_015 | Treat context pack and validation scripts as v0.5 targets until implemented and tested. | v0.1 relies on manual evidence fields. |
| C-AID-007 | Four-framework composition vs Aider-only context layer | F_AID_017, F_AID_036, F_GSD_004, F_SUP_004 | Aider owns repo context/file scope/Git ergonomics; GSD2 owns state/context freshness; Superpowers owns engineering discipline. | Framework summary must avoid giving Aider state-machine or runtime authority. |

## Precedence Rules

1. File scope cards `F_AID_013` and `F_AID_039` override repo map suggestions when deciding editable files.
2. Verification cards `F_AID_015` and `F_AID_025` constrain Git/commit cards: no completion or commit without evidence.
3. Weak model cards `F_AID_016`, `F_AID_026`, and `F_AID_028` constrain all Aider mechanisms for small-model execution.
4. Template deliverables should be treated as implementation targets, not proof that scripts or files already exist.
5. Aider mechanisms should be merged as Context/File/Git/Verification layer assets, not as a full orchestration runtime.

## Required Follow-up During Synthesis

| output | required handling |
|---|---|
| `output/frameworks/aider_summary.md` | Include conflict section and cite this ledger. |
| `output/mechanisms/repo_context.md` | Merge repo map with GSD2 context priority and later SWE/gstack tool context. |
| `output/mechanisms/risk_gate.md` | Include weak model overreach and auto-commit safeguards. |
| `output/ios_harness_mapping/v0_1_scope.md` | Include `CONTEXT_INDEX.md`, `FILE_SCOPE_RULES.md`, `GIT_WORKFLOW.md`, `VERIFICATION_MATRIX.md`; exclude automatic repo map runtime. |

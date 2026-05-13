# Framework Summary: gsd2

## 1. One-line Essence

gsd2 的可迁移价值是：状态与恢复：task state machine、context isolation、failure recovery、model routing。

## 2. Source Coverage

| source_id | status | source_card |
| --- | --- | --- |
| F_GSD_001 | reviewed | output/source_cards/gsd2/F_GSD_001_GSD2_深度研究_iOS_Harness_迁移报告.md |
| F_GSD_002 | reviewed | output/source_cards/gsd2/F_GSD_002_GSD2深度研究_iOS_Harness迁移方案.md |
| F_GSD_003 | reviewed | output/source_cards/gsd2/F_GSD_003_plan.md |
| F_GSD_004 | reviewed | output/source_cards/gsd2/F_GSD_004_report_stages_10_11.md |
| F_GSD_005 | reviewed | output/source_cards/gsd2/F_GSD_005_report_stages_12_13_14.md |
| F_GSD_006 | reviewed | output/source_cards/gsd2/F_GSD_006_report_stages_1_2_3.md |
| F_GSD_007 | reviewed | output/source_cards/gsd2/F_GSD_007_report_stages_4_5_6.md |
| F_GSD_008 | reviewed | output/source_cards/gsd2/F_GSD_008_report_stages_7_8_9.md |
| F_GSD_009 | reviewed | output/source_cards/gsd2/F_GSD_009_research_architecture.md |
| F_GSD_010 | reviewed | output/source_cards/gsd2/F_GSD_010_research_context.md |
| F_GSD_011 | reviewed | output/source_cards/gsd2/F_GSD_011_research_failure_recovery.md |
| F_GSD_012 | reviewed | output/source_cards/gsd2/F_GSD_012_research_model_routing.md |

## 3. Core Mechanism Targets

| layer | count |
| --- | --- |
| Action / ACI Layer | 6 |
| Context Layer | 16 |
| Feedback / Verification Layer | 19 |
| Goal Layer | 4 |
| Harness Maintenance Layer | 11 |
| Memory / State Layer | 15 |
| Risk / Release Layer | 7 |
| Role / Review Layer | 12 |
| Task Layer | 6 |

## 4. Highest-Impact Harness Files

| harness_file | mechanism_targets |
| --- | --- |
| STATE.md | 11 |
| MODEL_ROUTING.md | 8 |
| FAILURE_LOG.md | 7 |
| TASKS.md | 6 |
| CONTEXT_RULES.md | 6 |
| VERIFICATION_MATRIX.md | 5 |
| AGENTS.md | 4 |
| CONTEXT_INDEX.md | 4 |
| docs/agent/ACI_TOOL_CONTRACTS.md | 4 |
| QUALITY_GATE.md | 3 |
| DECISIONS.md | 3 |
| README.md | 3 |
| docs/agent/CONTEXT_RULES.md | 2 |
| ROADMAP.md | 2 |
| PRODUCT_SPEC.md | 2 |

## 5. Failure Modes Addressed

| failure_mode | mechanism_count |
| --- | --- |
| stuck_loop | 37 |
| context_pollution | 27 |
| false_completion | 27 |
| context_rot | 19 |
| weak_model_overreach | 18 |
| weak_model_confusion | 17 |
| model_overkill | 17 |
| model_underfit | 17 |
| state_loss | 10 |
| vague_large_task | 10 |
| crash_progress_loss | 10 |
| model_cost_overrun | 10 |
| fake_verification | 10 |
| wrong_tool_for_job | 10 |
| blind_retry | 10 |

## 6. Transferable Parts

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-GSD-002 | gsd2 | F_GSD_001 | v0_1 | Milestone Slice Task Hierarchy |
| M-GSD-003 | gsd2 | F_GSD_001 | v0_1 | Fresh Session Execution |
| M-GSD-009 | gsd2 | F_GSD_001 | v0_1 | Verification Gate And Completion Criteria |
| M-GSD-010 | gsd2 | F_GSD_001 | v0_1 | Markdown Projection |
| M-GSD-012 | gsd2 | F_GSD_002 | v0_1 | Runtime Mechanism Transfer Boundary |
| M-GSD-013 | gsd2 | F_GSD_002 | v0_1 | End-to-End Harness Control Stack |
| M-GSD-014 | gsd2 | F_GSD_002 | v0_1 | Versioned Migration Scope |
| M-GSD-016 | gsd2 | F_GSD_003 | v0_1 | Staged Research Pipeline |
| M-GSD-017 | gsd2 | F_GSD_003 | v0_1 | Research Topic Partition |
| M-GSD-019 | gsd2 | F_GSD_003 | v0_1 | Skill Loading Plan |
| M-GSD-020 | gsd2 | F_GSD_003 | v0_1 | Quality Criteria Before Migration |
| M-GSD-021 | gsd2 | F_GSD_004 | v0_1 | Backward iOS Harness Design |
| M-GSD-022 | gsd2 | F_GSD_004 | v0_1 | Target File Tree as Architecture |
| M-GSD-023 | gsd2 | F_GSD_004 | v0_1 | Agent Document Responsibility Split |
| M-GSD-024 | gsd2 | F_GSD_004 | v0_1 | Model/Failure/Git/Verification Control Files |
| M-GSD-026 | gsd2 | F_GSD_004 | v0_1 | Superpowers-GSD2 Role Split |
| M-GSD-027 | gsd2 | F_GSD_004 | v0_1 | Conflict Resolution Policy |
| M-GSD-028 | gsd2 | F_GSD_004 | v0_1 | Versioned Combination Strategy |
| M-GSD-030 | gsd2 | F_GSD_005 | v0_1 | State and Task Templates |
| M-GSD-031 | gsd2 | F_GSD_005 | v0_1 | Routing and Failure Templates |
| M-GSD-033 | gsd2 | F_GSD_005 | v0_1 | Deliverable Catalog |
| M-GSD-034 | gsd2 | F_GSD_005 | v0_1 | Evidence-Aware Output Standards |
| M-GSD-036 | gsd2 | F_GSD_005 | v0_1 | Handoff-Oriented Packaging |
| M-GSD-037 | gsd2 | F_GSD_006 | v0_1 | Research Question Framing |

## 7. Non-transferable Parts

- Runtime interception is not transferred unless a tested script/runtime exists.
- Duplicate reports are not copied wholesale; section-level Source Cards have priority.
- Raw files remain evidence, not default context.

## 8. Conflicts

See `output/conflicts/gsd2_conflicts.md`.

## 9. Final Judgment

Use this framework as one layer in the fused iOS Harness. Do not let it override stronger evidence from another layer.

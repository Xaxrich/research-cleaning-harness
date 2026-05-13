# Framework Summary: aider

## 1. One-line Essence

aider 的可迁移价值是：仓库上下文：repo map、explicit file scope、read-only context、Git/verification loop。

## 2. Source Coverage

| source_id | status | source_card |
| --- | --- | --- |
| F_AID_001 | reviewed | output/source_cards/aider/F_AID_001_plan.md |
| F_AID_002 | reviewed | output/source_cards/aider/F_AID_002_stage1_aider_overview.md |
| F_AID_003 | reviewed | output/source_cards/aider/F_AID_003_stage1_docs_analysis.md |
| F_AID_004 | reviewed | output/source_cards/aider/F_AID_004_stage1_file_selection.md |
| F_AID_005 | reviewed | output/source_cards/aider/F_AID_005_stage1_git_integration.md |
| F_AID_006 | reviewed | output/source_cards/aider/F_AID_006_stage1_lint_test_loop.md |
| F_AID_007 | reviewed | output/source_cards/aider/F_AID_007_stage1_repo_structure.md |
| F_AID_008 | reviewed | output/source_cards/aider/F_AID_008_stage1_repopmap_deep.md |
| F_AID_009 | reviewed | output/source_cards/aider/F_AID_009_stage1_skeptic_analysis.md |
| F_AID_010 | reviewed | output/source_cards/aider/F_AID_010_stage2_concepts_analysis.md |
| F_AID_011 | reviewed | output/source_cards/aider/F_AID_011_stage2_context_index.md |
| F_AID_012 | reviewed | output/source_cards/aider/F_AID_012_stage2_conventions.md |
| F_AID_013 | reviewed | output/source_cards/aider/F_AID_013_stage2_file_scope_rules.md |
| F_AID_014 | reviewed | output/source_cards/aider/F_AID_014_stage2_git_atomic_commit.md |
| F_AID_015 | reviewed | output/source_cards/aider/F_AID_015_stage2_lint_test_loop.md |
| F_AID_016 | reviewed | output/source_cards/aider/F_AID_016_stage2_weak_model_rules.md |
| F_AID_017 | reviewed | output/source_cards/aider/F_AID_017_stage3_integration_design.md |
| F_AID_018 | reviewed | output/source_cards/aider/F_AID_018_stage3_learning_path.md |
| F_AID_019 | reviewed | output/source_cards/aider/F_AID_019_stage3_migration_design.md |
| F_AID_020 | reviewed | output/source_cards/aider/F_AID_020_交付物10_CONVENTIONS_md模板.md |
| F_AID_021 | reviewed | output/source_cards/aider/F_AID_021_交付物11_FLUTTER_CONVENTIONS_md模板.md |
| F_AID_022 | reviewed | output/source_cards/aider/F_AID_022_交付物12_FIREBASE_CONVENTIONS_md模板.md |
| F_AID_023 | reviewed | output/source_cards/aider/F_AID_023_交付物13_IOS_NATIVE_CONVENTIONS_md模板.md |
| F_AID_024 | reviewed | output/source_cards/aider/F_AID_024_交付物14_GIT_ATOMIC_COMMIT_md模板.md |
| F_AID_025 | reviewed | output/source_cards/aider/F_AID_025_交付物15_LINT_TEST_LOOP_md模板.md |
| F_AID_026 | reviewed | output/source_cards/aider/F_AID_026_交付物16_WEAK_MODEL_RULES_md模板.md |
| F_AID_027 | reviewed | output/source_cards/aider/F_AID_027_交付物17_context_pack_sh设计说明.md |
| F_AID_028 | reviewed | output/source_cards/aider/F_AID_028_交付物18_弱模型文件范围任务卡模板.md |
| F_AID_029 | reviewed | output/source_cards/aider/F_AID_029_交付物19_Git_commit_message模板.md |
| F_AID_030 | reviewed | output/source_cards/aider/F_AID_030_交付物1_Aider框架解剖报告.md |
| F_AID_031 | reviewed | output/source_cards/aider/F_AID_031_交付物20_PR_description模板.md |
| F_AID_032 | reviewed | output/source_cards/aider/F_AID_032_交付物2_Aider_5Why设计逻辑.md |
| F_AID_033 | reviewed | output/source_cards/aider/F_AID_033_交付物3_Aider_repo_map机制拆解.md |
| F_AID_034 | reviewed | output/source_cards/aider/F_AID_034_交付物4_Aider_Git原子提交机制拆解.md |
| F_AID_035 | reviewed | output/source_cards/aider/F_AID_035_交付物5_Aider到iOS_Harness迁移方案.md |
| F_AID_036 | reviewed | output/source_cards/aider/F_AID_036_交付物6_四框架组合方案.md |
| F_AID_037 | reviewed | output/source_cards/aider/F_AID_037_交付物7_iOS_Harness_v0_1文件结构.md |
| F_AID_038 | reviewed | output/source_cards/aider/F_AID_038_交付物8_CONTEXT_INDEX_md模板.md |
| F_AID_039 | reviewed | output/source_cards/aider/F_AID_039_交付物9_FILE_SCOPE_RULES_md模板.md |

## 3. Core Mechanism Targets

| layer | count |
| --- | --- |
| Action / ACI Layer | 10 |
| Context Layer | 41 |
| Feedback / Verification Layer | 18 |
| Goal Layer | 1 |
| Harness Maintenance Layer | 16 |
| Memory / State Layer | 12 |
| Risk / Release Layer | 26 |
| Role / Review Layer | 16 |
| Task Layer | 16 |

## 4. Highest-Impact Harness Files

| harness_file | mechanism_targets |
| --- | --- |
| CONTEXT_INDEX.md | 24 |
| TASKS.md | 22 |
| GIT_WORKFLOW.md | 12 |
| README.md | 11 |
| CONTEXT_RULES.md | 8 |
| docs/agent/REPO_CONTEXT.md | 7 |
| docs/agent/EDIT_FORMATS.md | 7 |
| VERIFICATION_MATRIX.md | 7 |
| templates/pr_description.md | 6 |
| STATE.md | 6 |
| IOS_RELEASE_CHECKLIST.md | 6 |
| MODEL_ROUTING.md | 6 |
| FAILURE_LOG.md | 5 |
| REVIEW_MATRIX.md | 5 |
| ROLE_MATRIX.md | 5 |

## 5. Failure Modes Addressed

| failure_mode | mechanism_count |
| --- | --- |
| context_pollution | 48 |
| wrong_file_edit | 40 |
| bad_patch_format | 28 |
| dirty_tree_overwrite | 24 |
| unreviewable_diff | 24 |
| rollback_gap | 24 |
| release_risk | 24 |
| handoff_loss | 24 |
| rule_drift | 20 |
| platform_inconsistency | 20 |
| weak_model_overreach | 20 |
| unclear_transfer_scope | 20 |
| framework_role_conflict | 20 |
| fake_verification | 12 |
| stuck_fix_loop | 12 |

## 6. Transferable Parts

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-AID-001 | aider | F_AID_001 | v0_1 | Aider Research Pipeline |
| M-AID-002 | aider | F_AID_001 | v0_1 | Deliverable-Driven Cleaning |
| M-AID-004 | aider | F_AID_001 | v0_1 | Quality Gate Before Synthesis |
| M-AID-005 | aider | F_AID_002 | v0_1 | Repo-Aware Editing Loop |
| M-AID-006 | aider | F_AID_002 | v0_1 | Explicit Added Files |
| M-AID-007 | aider | F_AID_002 | v0_1 | Read-Only Rule Context |
| M-AID-009 | aider | F_AID_003 | v0_1 | Repo-Aware Editing Loop |
| M-AID-010 | aider | F_AID_003 | v0_1 | Explicit Added Files |
| M-AID-011 | aider | F_AID_003 | v0_1 | Read-Only Rule Context |
| M-AID-013 | aider | F_AID_004 | v0_1 | Repo-Aware Editing Loop |
| M-AID-014 | aider | F_AID_004 | v0_1 | Explicit Added Files |
| M-AID-015 | aider | F_AID_004 | v0_1 | Read-Only Rule Context |
| M-AID-017 | aider | F_AID_005 | v0_1 | Dirty Tree Awareness |
| M-AID-018 | aider | F_AID_005 | v0_1 | Atomic Commit Boundary |
| M-AID-020 | aider | F_AID_005 | v0_1 | PR/Commit Message Evidence |
| M-AID-021 | aider | F_AID_006 | v0_1 | Lint Command Gate |
| M-AID-022 | aider | F_AID_006 | v0_1 | Test Command Gate |
| M-AID-025 | aider | F_AID_007 | v0_1 | Repo-Aware Editing Loop |
| M-AID-026 | aider | F_AID_007 | v0_1 | Explicit Added Files |
| M-AID-027 | aider | F_AID_007 | v0_1 | Read-Only Rule Context |
| M-AID-032 | aider | F_AID_008 | v0_1 | Repo Map Boundary |
| M-AID-033 | aider | F_AID_009 | v0_1 | Aider Suitability Boundary |
| M-AID-034 | aider | F_AID_009 | v0_1 | iOS-Specific Risk Review |
| M-AID-035 | aider | F_AID_009 | v0_1 | Weak Model Overreach Warning |

## 7. Non-transferable Parts

- Runtime interception is not transferred unless a tested script/runtime exists.
- Duplicate reports are not copied wholesale; section-level Source Cards have priority.
- Raw files remain evidence, not default context.

## 8. Conflicts

See `output/conflicts/aider_conflicts.md`.

## 9. Final Judgment

Use this framework as one layer in the fused iOS Harness. Do not let it override stronger evidence from another layer.

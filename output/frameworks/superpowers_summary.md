# Framework Summary: superpowers

## 1. One-line Essence

superpowers 的可迁移价值是：工程纪律：planning、TDD、debugging、review、verification-before-completion。

## 2. Source Coverage

| source_id | status | source_card |
| --- | --- | --- |
| F_SUP_001 | reviewed | output/source_cards/superpowers/F_SUP_001_00_final_report.md |
| F_SUP_002 | reviewed | output/source_cards/superpowers/F_SUP_002_01_superpowers_anatomy_report.md |
| F_SUP_003 | reviewed | output/source_cards/superpowers/F_SUP_003_02_superpowers_design_logic.md |
| F_SUP_004 | reviewed | output/source_cards/superpowers/F_SUP_004_03_ios_harness_migration.md |
| F_SUP_005 | reviewed | output/source_cards/superpowers/F_SUP_005_04_skeptic_review.md |
| F_SUP_006 | reviewed | output/source_cards/superpowers/F_SUP_006_05_learning_path.md |
| F_SUP_007 | reviewed | output/source_cards/superpowers/F_SUP_007_AGENTS.md |
| F_SUP_008 | reviewed | output/source_cards/superpowers/F_SUP_008_docs_agent_STATE.md |
| F_SUP_009 | reviewed | output/source_cards/superpowers/F_SUP_009_docs_agent_TASKS.md |
| F_SUP_010 | reviewed | output/source_cards/superpowers/F_SUP_010_plan.md |
| F_SUP_011 | reviewed | output/source_cards/superpowers/F_SUP_011_skills_app_store_release_SKILL.md |
| F_SUP_012 | reviewed | output/source_cards/superpowers/F_SUP_012_skills_mobile_tdd_SKILL.md |
| F_SUP_013 | reviewed | output/source_cards/superpowers/F_SUP_013_skills_root_cause_debugging_SKILL.md |
| F_SUP_014 | reviewed | output/source_cards/superpowers/F_SUP_014_superpowers_architecture.md |

## 3. Core Mechanism Targets

| layer | count |
| --- | --- |
| Action / ACI Layer | 5 |
| Context Layer | 13 |
| Feedback / Verification Layer | 23 |
| Goal Layer | 10 |
| Harness Maintenance Layer | 10 |
| Memory / State Layer | 9 |
| Risk / Release Layer | 11 |
| Role / Review Layer | 7 |
| Task Layer | 13 |

## 4. Highest-Impact Harness Files

| harness_file | mechanism_targets |
| --- | --- |
| AGENTS.md | 13 |
| docs/agent/TASKS.md | 12 |
| docs/agent/STATE.md | 9 |
| docs/agent/RISK_GATE.md | 6 |
| scripts/agent/verify-tests-pass.sh | 4 |
| SKILL.md | 4 |
| docs/agent/WORKFLOW_CHAIN.md | 4 |
| docs/agent/TESTING_GUIDE.md | 4 |
| docs/agent/DEBUG_GUIDE.md | 3 |
| scripts/agent/verify-ios-build.sh | 2 |
| docs/agent/FILE_PLACEMENT_MAP.md | 2 |
| QUALITY_GATE.md | 2 |
| templates/review_template.md | 2 |
| scripts/agent/verify-app-store-ready.sh | 2 |
| docs/agent/ESCALATION_RULES.md | 2 |

## 5. Failure Modes Addressed

| failure_mode | mechanism_count |
| --- | --- |
| no_test_completion | 39 |
| context_pollution | 20 |
| state_loss | 14 |
| release_risk | 14 |
| subagent_orchestration_failure | 13 |
| ios_build_gap | 13 |
| worktree_ios_path_breakage | 13 |
| weak_model_overreach | 13 |
| tests_after_implementation | 9 |
| pseudo_test_coverage | 9 |
| widget_behavior_unverified | 9 |
| native_bridge_unverified | 9 |
| bad_mobile_tests | 9 |
| firebase_live_dependency | 9 |
| random_fix_loop | 9 |

## 6. Transferable Parts

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-SUP-001 | superpowers | F_SUP_001 | v0_1 | Engineering Discipline System |
| M-SUP-002 | superpowers | F_SUP_001 | v0_1 | Weak-model Adaptation By Assumption Reduction |
| M-SUP-004 | superpowers | F_SUP_001 | v0_1 | Progressive Adoption Path |
| M-SUP-005 | superpowers | F_SUP_001 | v0_1 | iOS Harness File Placement Blueprint |
| M-SUP-006 | superpowers | F_SUP_001 | v0_1 | Risk Escalation And Human Gate |
| M-SUP-007 | superpowers | F_SUP_002 | v0_1 | Skill As Behavior Code |
| M-SUP-008 | superpowers | F_SUP_002 | v0_1 | Session Bootstrap Hook |
| M-SUP-010 | superpowers | F_SUP_002 | v0_1 | Single Source Alias |
| M-SUP-011 | superpowers | F_SUP_002 | v0_1 | Process And Implementation Skill Split |
| M-SUP-012 | superpowers | F_SUP_002 | v0_1 | Convention Path Memory |
| M-SUP-014 | superpowers | F_SUP_003 | v0_1 | Three-layer Process Constraint |
| M-SUP-015 | superpowers | F_SUP_003 | v0_1 | Plan Task Step Decomposition |
| M-SUP-016 | superpowers | F_SUP_003 | v0_1 | Triple Isolation Strategy |
| M-SUP-017 | superpowers | F_SUP_003 | v0_1 | Three-level Verification Chain |
| M-SUP-019 | superpowers | F_SUP_003 | v0_1 | Reviewer Implementer Separation |
| M-SUP-022 | superpowers | F_SUP_004 | v0_1 | Weak-model Lightweight Migration |
| M-SUP-023 | superpowers | F_SUP_004 | v0_1 | iOS Harness Target Layout |
| M-SUP-025 | superpowers | F_SUP_004 | v0_1 | Live Agent Documents |
| M-SUP-027 | superpowers | F_SUP_004 | v0_1 | Task Capability Matrix |
| M-SUP-028 | superpowers | F_SUP_004 | v0_1 | Two-failure Escalation |
| M-SUP-030 | superpowers | F_SUP_005 | v0_1 | Selective Principle Extraction |
| M-SUP-031 | superpowers | F_SUP_005 | v0_1 | Explicit Non-transfer List |
| M-SUP-032 | superpowers | F_SUP_005 | v0_1 | Weak-model Checkpoint Simplification |
| M-SUP-035 | superpowers | F_SUP_005 | v0_1 | Human Gate For High-risk Work |

## 7. Non-transferable Parts

- Runtime interception is not transferred unless a tested script/runtime exists.
- Duplicate reports are not copied wholesale; section-level Source Cards have priority.
- Raw files remain evidence, not default context.

## 8. Conflicts

See `output/conflicts/superpowers_conflicts.md`.

## 9. Final Judgment

Use this framework as one layer in the fused iOS Harness. Do not let it override stronger evidence from another layer.

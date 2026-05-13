# iOS Harness v0_5 Scope

## Summary

v0_5 contains 262 mechanism target rows.

## Target Files

| harness_file | mechanism_targets |
| --- | --- |
| docs/agent/ACI_TOOL_CONTRACTS.md | 33 |
| STATE.md | 26 |
| README.md | 18 |
| MODEL_ROUTING.md | 14 |
| FAILURE_LOG.md | 13 |
| VERIFICATION_MATRIX.md | 12 |
| TASKS.md | 10 |
| ROLE_MATRIX.md | 10 |
| docs/agent/EDIT_FORMATS.md | 8 |
| GIT_WORKFLOW.md | 6 |
| REVIEW_MATRIX.md | 6 |
| AGENTS.md | 5 |
| CONTEXT_INDEX.md | 4 |
| scripts/agent/verify-tests-pass.sh | 4 |
| docs/agent/TESTING_GUIDE.md | 4 |
| CONFIG.md | 4 |
| docs/agent/MINI_SWE_LOOP.md | 4 |
| scripts/agent/context_pack.sh | 3 |
| templates/check_template.md | 3 |
| docs/agent/WORKFLOW_CHAIN.md | 3 |
| SKILL.md | 3 |
| docs/agent/STATE.md | 3 |
| docs/agent/TASKS.md | 3 |
| docs/agent/DEBUG_GUIDE.md | 3 |
| docs/agent/REPO_MAP.md | 2 |
| scripts/agent/stuck_detector.sh | 2 |
| DECISIONS.md | 2 |
| HIGH_RISK_FILES.md | 2 |
| scripts/agent/verify-ios-build.sh | 2 |
| scripts/agent/verify-app-store-ready.sh | 2 |
| docs/agent/REVIEW_GUIDE.md | 2 |
| docs/agent/checklists/release-vX.Y.Z.md | 2 |
| RISK_CONTROL.md | 2 |
| docs/agent/ENVIRONMENT_ABSTRACTION.md | 2 |
| PRODUCT_SPEC.md | 1 |
| docs/agent/AIDER_LEARNING_PATH.md | 1 |
| docs/agent/STATE_SCHEMA.md | 1 |
| docs/agent/CONTEXT_RULES.md | 1 |
| docs/agent/ESCALATION_RULES.md | 1 |
| docs/agent/RECOVERY.md | 1 |
| docs/agent/MODEL_ROUTING.md | 1 |
| gsd2_delivery_index.md | 1 |
| source_crosscheck.md | 1 |
| docs/agent/LEARNING_PATH.md | 1 |
| scripts/agent/verification_runner.sh | 1 |
| docs/agent/WEAK_MODEL_CONTEXT.md | 1 |
| docs/agent/CONTEXT_ROT.md | 1 |
| docs/agent/IOS_CONTEXT_PRIORITY.md | 1 |
| docs/agent/IOS_MODEL_ROUTING_TABLE.md | 1 |
| docs/agent/PACKAGE_MANIFEST.md | 1 |
| templates/skill_template.md | 1 |
| scripts/agent/check-bootstrap.sh | 1 |
| docs/agent/HOST_ADAPTERS.md | 1 |
| scripts/agent/verify-harness-output.sh | 1 |
| docs/agent/RISK_GATE.md | 1 |
| docs/agent/ONBOARDING.md | 1 |
| templates/training_task_template.md | 1 |
| docs/agent/SKILL_AUTHORING.md | 1 |
| templates/review_template.md | 1 |
| docs/agent/REVIEW_MATRIX.md | 1 |
| CONTEXT_RULES.md | 1 |
| IOS_RELEASE_CHECKLIST.md | 1 |
| scripts/agent/verify-firebase-config.sh | 1 |
| docs/agent/checklists/rejection-vX.Y.Z.md | 1 |
| docs/agent/debug/debug-YYYY-MM-DD-issue.md | 1 |
| templates/debug_session_template.md | 1 |
| QUALITY_GATE.md | 1 |
| scripts/agent/view_file.sh | 1 |
| scripts/agent/search_code.sh | 1 |
| scripts/agent/safe_edit_check.sh | 1 |
| scripts/agent/run_safe_command.sh | 1 |
| scripts/agent/classify_failure.sh | 1 |
| templates/manual_approval.md | 1 |
| docs/agent/SWE_LEARNING_PATH.md | 1 |

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-AID-003 | aider | F_AID_001 | v0_5 | Aider-to-iOS Transfer Agenda |
| M-AID-008 | aider | F_AID_002 | v0_5 | Edit Format Discipline |
| M-AID-012 | aider | F_AID_003 | v0_5 | Edit Format Discipline |
| M-AID-016 | aider | F_AID_004 | v0_5 | Edit Format Discipline |
| M-AID-019 | aider | F_AID_005 | v0_5 | Auto-Commit With Undo Semantics |
| M-AID-023 | aider | F_AID_006 | v0_5 | Reflection Fix Loop |
| M-AID-024 | aider | F_AID_006 | v0_5 | Verification Evidence Record |
| M-AID-028 | aider | F_AID_007 | v0_5 | Edit Format Discipline |
| M-AID-029 | aider | F_AID_008 | v0_5 | Repo Map Ranking |
| M-AID-030 | aider | F_AID_008 | v0_5 | Token-Budgeted Repository Context |
| M-AID-031 | aider | F_AID_008 | v0_5 | Dependency Surfacing |
| M-AID-040 | aider | F_AID_010 | v0_5 | Edit Format Discipline |
| M-AID-042 | aider | F_AID_011 | v0_5 | Task-Type Context Pack |
| M-AID-043 | aider | F_AID_011 | v0_5 | Weak/Strong Context Modes |
| M-AID-044 | aider | F_AID_011 | v0_5 | Context Pack Audit Header |
| M-AID-048 | aider | F_AID_012 | v0_5 | Rule Drift Review |
| M-AID-055 | aider | F_AID_014 | v0_5 | Auto-Commit With Undo Semantics |
| M-AID-059 | aider | F_AID_015 | v0_5 | Reflection Fix Loop |
| M-AID-060 | aider | F_AID_015 | v0_5 | Verification Evidence Record |
| M-AID-062 | aider | F_AID_016 | v0_5 | Weak Model Task Downgrade |
| M-AID-063 | aider | F_AID_016 | v0_5 | Simplified Context Pack |
| M-AID-067 | aider | F_AID_017 | v0_5 | Four-Framework Role Composition |
| M-AID-069 | aider | F_AID_018 | v0_5 | Three-Day Aider Learning Path |
| M-AID-070 | aider | F_AID_018 | v0_5 | Concept-to-Practice Progression |
| M-AID-071 | aider | F_AID_018 | v0_5 | iOS Scenario Exercises |
| M-AID-072 | aider | F_AID_018 | v0_5 | Knowledge Handoff Summary |
| M-AID-075 | aider | F_AID_019 | v0_5 | Four-Framework Role Composition |
| M-AID-080 | aider | F_AID_020 | v0_5 | Rule Drift Review |
| M-AID-084 | aider | F_AID_021 | v0_5 | Rule Drift Review |
| M-AID-088 | aider | F_AID_022 | v0_5 | Rule Drift Review |
| M-AID-092 | aider | F_AID_023 | v0_5 | Rule Drift Review |
| M-AID-095 | aider | F_AID_024 | v0_5 | Auto-Commit With Undo Semantics |
| M-AID-099 | aider | F_AID_025 | v0_5 | Reflection Fix Loop |
| M-AID-100 | aider | F_AID_025 | v0_5 | Verification Evidence Record |
| M-AID-102 | aider | F_AID_026 | v0_5 | Weak Model Task Downgrade |
| M-AID-103 | aider | F_AID_026 | v0_5 | Simplified Context Pack |
| M-AID-106 | aider | F_AID_027 | v0_5 | Task-Type Context Pack |
| M-AID-107 | aider | F_AID_027 | v0_5 | Weak/Strong Context Modes |
| M-AID-108 | aider | F_AID_027 | v0_5 | Context Pack Audit Header |
| M-AID-115 | aider | F_AID_029 | v0_5 | Auto-Commit With Undo Semantics |

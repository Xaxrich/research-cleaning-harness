# TASKS

Use one task card per bounded change.

## TASK-002: Add product planning and verification gates

status: review_needed
task_type: docs
owner_role: orchestrator
risk_level: low
goal:
  Upgrade the harness from a safe execution skeleton into a full product-development loop with discovery, product confirmation, solution planning, task breakdown, module verification, simulator policy, and run retrospectives.

allowed_files:
  - AGENTS.md
  - CALL_GRAPH.md
  - FRAMEWORK_SPEC.md
  - FULL_TUTORIAL.md
  - README.md
  - START_HERE.md
  - docs/superpowers/plans/2026-05-14-harness-vnext.md
  - layers/00_goal/DISCOVERY_GATE.md
  - layers/00_goal/PRODUCT_BRIEF.md
  - layers/01_planning/README.md
  - layers/01_planning/SOLUTION_PLAN.md
  - layers/01_planning/TASK_BREAKDOWN.md
  - layers/01_planning/USER_CONFIRMATION.md
  - layers/01_planning/GATE_OUTPUT_PROTOCOL.md
  - layers/01_planning/templates/module_plan.md
  - layers/01_task/TASKS.md
  - layers/01_task/templates/task_card.md
  - layers/02_context/CONTEXT_INDEX.md
  - layers/02_context/CONTEXT_RULES.md
  - layers/03_file_scope/FILE_SCOPE_RULES.md
  - layers/06_verification/VERIFICATION_MATRIX.md
  - layers/06_verification/MODULE_VERIFICATION_POLICY.md
  - layers/06_verification/SIMULATOR_TEST_POLICY.md
  - layers/06_verification/ACCEPTANCE_CHECKLIST.md
  - layers/08_memory_state/STATE.md
  - layers/08_memory_state/RUN_TRACE.md
  - layers/08_memory_state/RETROSPECTIVE.md
  - layers/09_workflows/WORKFLOW_CHAIN.md
  - layers/10_examples/codex_prompts.md
  - scripts/validate_harness.py

read_only_files:
  - ../output/frameworks/superpowers_summary.md
  - ../output/frameworks/gstack_summary.md
  - ../output/frameworks/aider_summary.md
  - ../output/frameworks/gsd2_summary.md
  - ../output/frameworks/swe_agent_summary.md
  - ../output/mechanisms/skills_and_process.md
  - ../output/mechanisms/task_state_machine.md
  - ../output/mechanisms/verification.md
  - ../output/mechanisms/repo_context.md
  - ../output/mechanisms/agent_roles.md
  - ../output/mechanisms/aci_tools.md
  - ../output/mechanisms/risk_gate.md

forbidden_files:
  - .env*
  - "**/*.p12"
  - "**/*.mobileprovision"
  - raw/**

verification_commands:
  - python3 scripts/validate_harness.py
  - git diff -- ios_app_development_harness

rollback_plan:
  Revert TASK-002 changes in the listed allowed files.

completion_evidence:
  - python3 scripts/validate_harness.py: pass
  - git diff --stat -- ios_app_development_harness: harness-only diff reviewed
  - user feedback: confirmation nodes were not clear enough; add gate output protocol
  - user feedback: decision request should appear at the end; update gate protocol
  - user feedback: confirmation prompts must name current stage, review document, decision target, and exact item
  - user request: add standard gate reply example for Cursor/Codex prompts

## TASK-001: Fill project-specific harness setup

status: ready
task_type: docs
owner_role: orchestrator
risk_level: low
goal:
  Adapt PRODUCT_SPEC.md, CONTEXT_INDEX.md, FILE_SCOPE_RULES.md, and VERIFICATION_MATRIX.md to the real iOS project.

allowed_files:
  - agent_harness/layers/00_goal/PRODUCT_SPEC.md
  - agent_harness/layers/02_context/CONTEXT_INDEX.md
  - agent_harness/layers/03_file_scope/FILE_SCOPE_RULES.md
  - agent_harness/layers/06_verification/VERIFICATION_MATRIX.md

read_only_files:
  - README.md
  - pubspec.yaml
  - Package.swift
  - ios/Runner/Info.plist

forbidden_files:
  - .env*
  - "**/*.p12"
  - "**/*.mobileprovision"

verification_commands:
  - python3 agent_harness/scripts/validate_harness.py
  - git diff -- agent_harness

rollback_plan:
  Revert the edited harness docs.

## New Task Template

```yaml
task_id:
status: ready
task_type: discovery | planning | docs | pure_logic | local_data | swiftui_ui | flutter_ui | swift_bridge | firebase_rules | tests | bugfix | release
module:
depends_on: []
product_brief_status: draft | needs_user_confirmation | confirmed | superseded
solution_plan_status: draft | needs_user_confirmation | confirmed | superseded
user_confirmed_plan: false
owner_role:
risk_level: low | medium | high | release_blocking
goal:
acceptance_criteria: []
verification_level: diff | unit | build | simulator | device | manual
simulator_required: false
device_required: false
review_required: false
allowed_files: []
read_only_files: []
forbidden_files: []
required_context: []
required_tools: []
verification_commands: []
rollback_plan:
trace_file:
completion_evidence: []
```

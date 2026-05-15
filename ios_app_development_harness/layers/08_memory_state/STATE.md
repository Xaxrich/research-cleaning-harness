# STATE

phase: review_needed
current_task: TASK-002
current_role: orchestrator
last_updated: 2026-05-15

active_files:
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

verification:
  required:
    - python3 scripts/validate_harness.py
    - git diff -- ios_app_development_harness
  completed:
    - python3 scripts/validate_harness.py
    - git diff --check
    - git diff -- ios_app_development_harness
    - git diff --stat -- ios_app_development_harness
    - git diff --name-only -- ios_app_development_harness
    - git status --short
  blocked: []

blocked:
  - none

next:
  - review TASK-002 diff
  - use revised Chinese gate protocol in the next live user decision

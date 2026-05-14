# TASKS

Use one task card per bounded change.

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
task_type: docs | flutter_ui | swift_bridge | firebase_rules | tests | bugfix | release
owner_role:
risk_level: low | medium | high | release_blocking
goal:
allowed_files: []
read_only_files: []
forbidden_files: []
required_context: []
required_tools: []
verification_commands: []
rollback_plan:
completion_evidence: []
```

# Example Task: Docs-only Harness Setup

```yaml
task_id: TASK-001
status: ready
task_type: docs
owner_role: orchestrator
risk_level: low
goal: Adapt PRODUCT_SPEC.md for the real app.
allowed_files:
  - agent_harness/PRODUCT_SPEC.md
read_only_files:
  - README.md
  - pubspec.yaml
forbidden_files:
  - .env*
verification_commands:
  - git diff -- agent_harness/PRODUCT_SPEC.md
rollback_plan: revert PRODUCT_SPEC.md
```

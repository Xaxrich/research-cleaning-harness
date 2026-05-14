# Example Task: Release Preparation

```yaml
task_id: TASK-005
status: ready
task_type: release
owner_role: app_store_release
risk_level: release_blocking
goal: Prepare release readiness checklist for version 1.2.0.
allowed_files:
  - agent_harness/layers/07_risk_release/IOS_RELEASE_CHECKLIST.md
  - docs/release/1.2.0.md
read_only_files:
  - pubspec.yaml
  - ios/Runner/Info.plist
forbidden_files:
  - ios/**/*.p12
  - ios/**/*.mobileprovision
  - .env*
verification_commands:
  - git diff -- docs/release/1.2.0.md agent_harness/layers/07_risk_release/IOS_RELEASE_CHECKLIST.md
rollback_plan: revert release docs
manual_approval_required: true
```

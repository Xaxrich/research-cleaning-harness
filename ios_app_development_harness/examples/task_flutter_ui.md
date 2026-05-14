# Example Task: Flutter UI

```yaml
task_id: TASK-002
status: ready
task_type: flutter_ui
owner_role: flutter_ui
risk_level: low
goal: Update empty-state copy on Home screen.
allowed_files:
  - lib/features/home/home_empty_state.dart
  - test/features/home/home_empty_state_test.dart
read_only_files:
  - agent_harness/PRODUCT_SPEC.md
  - pubspec.yaml
forbidden_files:
  - ios/
  - .env*
verification_commands:
  - flutter analyze
  - flutter test test/features/home/home_empty_state_test.dart
rollback_plan: revert allowed files
```

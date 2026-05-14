# Example Task: Swift Bridge

```yaml
task_id: TASK-004
status: ready
task_type: swift_bridge
owner_role: swift_interop
risk_level: high
goal: Add a MethodChannel handler for local notification permission status.
allowed_files:
  - ios/Runner/AppDelegate.swift
  - lib/platform/notification_channel.dart
  - test/platform/notification_channel_test.dart
read_only_files:
  - ios/Runner/Info.plist
forbidden_files:
  - ios/**/*.p12
  - ios/**/*.mobileprovision
verification_commands:
  - flutter test test/platform/notification_channel_test.dart
  - xcodebuild -scheme Runner -destination 'platform=iOS Simulator,name=iPhone 16' build
rollback_plan: revert bridge and Dart caller files
```

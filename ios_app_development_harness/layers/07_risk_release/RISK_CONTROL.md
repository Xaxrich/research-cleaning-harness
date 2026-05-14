# RISK CONTROL

## Risk Levels

| level | examples | action |
|---|---|---|
| low | docs, small UI text, tests | proceed with task card |
| medium | multi-file UI/code change | verification required |
| high | native bridge, Firebase rules, privacy | role review required |
| release_blocking | signing, upload, production | manual approval required |

## Manual Approval Required

- App Store upload
- TestFlight submission
- signing certificate/profile changes
- production Firebase changes
- destructive commands
- credential access

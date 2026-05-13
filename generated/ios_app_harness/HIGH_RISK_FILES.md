# HIGH RISK FILES

High-risk files require explicit review and, for release/signing/upload actions, manual approval.

| pattern | risk | default action |
|---|---|---|
| `**/*.p12`, `**/*.mobileprovision` | signing secrets | deny |
| `.env*`, `GoogleService-Info.plist`, `firebase_options.*` | credentials/config | ask |
| `ios/**/Entitlements.plist` | capabilities | ask |
| `ios/**/Info.plist` | privacy/release metadata | ask |
| `firebase.rules`, `firestore.rules`, `storage.rules` | backend access control | ask |
| release/upload scripts | external side effects | manual approval |

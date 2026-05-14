# HIGH RISK FILES

| pattern | risk | default action |
|---|---|---|
| `.env*` | secrets | deny |
| `**/*.p12` | signing secret | deny |
| `**/*.mobileprovision` | provisioning | deny |
| `**/*.pem`, `**/*.key` | private key | deny |
| `GoogleService-Info.plist` | backend config | ask |
| `firebase_options.*` | backend config | ask |
| `ios/**/Info.plist` | privacy/release metadata | ask |
| `ios/**/Entitlements.plist` | capabilities | ask |
| `firestore.rules`, `storage.rules`, `firebase.rules` | data access | ask |
| release/upload scripts | external side effects | manual approval |

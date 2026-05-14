# Example Task: Firebase Rules

```yaml
task_id: TASK-003
status: ready
task_type: firebase_rules
owner_role: firebase_backend
risk_level: high
goal: Add read rule for a new collection.
allowed_files:
  - firestore.rules
  - test/firestore_rules.test.js
read_only_files:
  - docs/schema.md
forbidden_files:
  - .env*
  - serviceAccount*.json
verification_commands:
  - firebase emulators:exec --only firestore 'npm test'
rollback_plan: revert rules and tests
```

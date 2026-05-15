# MODULE VERIFICATION POLICY

Every task must declare a verification level. The level is based on the kind of module being changed, not on how confident the agent feels.

## Verification Levels

| level | meaning | minimum evidence |
|---|---|---|
| diff | documentation or metadata only | scoped `git diff` review |
| unit | pure logic or deterministic transformation | targeted unit tests |
| build | code compiles and links | app/package build command |
| simulator | user-visible iOS flow works in simulator | simulator launch or UI smoke evidence |
| device | behavior depends on real hardware or OS behavior | manual or automated device evidence |
| manual | cannot be automated safely | explicit checklist and user/manual approval |

## Module Defaults

| module type | minimum level | notes |
|---|---|---|
| product_docs | diff | link/schema check when available |
| pure_logic | unit | no simulator required unless UI consumes it in the same task |
| data_storage | unit | include serialization, migration, or persistence checks |
| ui_screen | simulator | build alone is not enough for user-visible UI |
| permission_system | simulator | device may be required when simulator cannot model the permission accurately |
| native_bridge | build | add simulator or device evidence when behavior crosses native boundaries |
| backend | unit | use emulator/staging before production |
| release | manual | release/signing/upload requires approval |

## Completion Rule

A task is incomplete if its required verification level is missing, blocked without explanation, or replaced by a weaker check without explicit user confirmation.

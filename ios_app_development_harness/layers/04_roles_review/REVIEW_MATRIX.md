# REVIEW MATRIX

| change_type | required review | block if |
|---|---|---|
| docs | orchestrator | unsupported claims or stale instructions |
| flutter_ui | flutter_ui, mobile_qa | no analyze/test evidence |
| swift_bridge | swift_interop, mobile_qa | no build/test evidence |
| firebase_rules | firebase_backend, security_privacy | no emulator/rules evidence |
| privacy | security_privacy | no privacy review |
| release | app_store_release, mobile_qa, security_privacy | no manual approval |

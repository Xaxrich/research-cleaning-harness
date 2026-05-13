# MODEL ROUTING

| task/risk | weak model | strong model | human approval |
|---|---|---|---|
| docs cleanup | yes | optional | no |
| small UI/test task | yes, if file scope is tiny | optional | no |
| multi-file refactor | no | yes | maybe |
| Firebase/security/privacy | no | yes | for high-risk actions |
| release/signing/upload | no | yes for preparation only | required |

## Weak Model Rules

- Max 1-3 editable files.
- No high-risk files.
- Must use task template and explicit verification.
- Escalate on failed verification, scope growth or uncertainty.

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-AID-035 | aider | F_AID_009 | v0_1 | Weak Model Overreach Warning |
| M-GSD-089 | gsd2 | F_GSD_012 | v0_1 | Routing Rationale |
| M-AID-043 | aider | F_AID_011 | v0_5 | Weak/Strong Context Modes |
| M-AID-062 | aider | F_AID_016 | v0_5 | Weak Model Task Downgrade |
| M-AID-102 | aider | F_AID_026 | v0_5 | Weak Model Task Downgrade |
| M-AID-107 | aider | F_AID_027 | v0_5 | Weak/Strong Context Modes |
| M-AID-151 | aider | F_AID_038 | v0_5 | Weak/Strong Context Modes |
| M-GSD-044 | gsd2 | F_GSD_006 | v0_5 | Dynamic Model Routing and Token Control |
| M-GSD-048 | gsd2 | F_GSD_007 | v0_5 | Model Routing Binding |
| M-GSD-053 | gsd2 | F_GSD_007 | v0_5 | Capability and Budget Routing |
| M-GSD-079 | gsd2 | F_GSD_010 | v0_5 | Token Profiles |
| M-GSD-091 | gsd2 | F_GSD_012 | v0_5 | Tiered Model Defaults |
| M-GSD-092 | gsd2 | F_GSD_012 | v0_5 | Budget Pressure Adjustment |
| M-GSD-094 | gsd2 | F_GSD_012 | v1_0 | Capability Scoring |
| M-GST-070 | gstack | F_GST_018 | v0_5 | Model-to-Role Matching |
| M-SWE-097 | swe-agent | F_SWE_025 | v0_5 | Weak Model ACI Permission Table |
| M-SWE-099 | swe-agent | F_SWE_025 | v0_5 | Capability Comparison Matrix |

# gstack Conflict Ledger

Scope: reviewed gstack Source Cards `F_GST_001` through `F_GST_040`.

This file records cross-card tensions that must be resolved before gstack mechanisms are merged with Superpowers, GSD2, Aider or SWE-agent.

## Conflict Summary

| conflict_id | conflict | source_cards | synthesis_resolution | iOS Harness implication |
|---|---|---|---|---|
| C-GST-001 | Virtual engineering team breadth vs v0.1 harness simplicity | F_GST_013, F_GST_017, F_GST_025, F_GST_026, F_GST_027 | Keep role matrix and review boundaries first; defer full multi-agent runtime. | v0.1 uses documents, not autonomous agent cluster dispatch. |
| C-GST-002 | Guardrail hook enforcement vs current document-only project | F_GST_016, F_GST_036, F_GST_026 | Treat hooks and command guards as v0.5/v1.0 targets until scripts exist and pass tests. | Do not claim command interception in v0.1. |
| C-GST-003 | Role specialization vs task overhead | F_GST_002-F_GST_009, F_GST_017, F_GST_038 | Use role ownership only for medium/high-risk work; small tasks can use a single owner plus review checklist. | Avoid over-routing trivial iOS tasks. |
| C-GST-004 | Review matrix depth vs delivery speed | F_GST_015, F_GST_020-F_GST_024, F_GST_027 | Keep typed review gates for high-risk domains; use lightweight checks for low-risk docs/UI changes. | Review burden must scale with risk. |
| C-GST-005 | Weak model participation vs release/security risk | F_GST_018, F_GST_027, F_GSD_012, F_AID_026 | Weak models can do bounded tasks only; release/security/native bridge require strong review. | Add model-to-role restrictions to `MODEL_ROUTING.md`. |
| C-GST-006 | Packaged ios-harness artifact vs clean asset authority | F_GST_001, F_GST_013-F_GST_024 | Treat package as delivery snapshot; source cards and reviewed templates are synthesis authority. | Do not merge packaged files blindly. |
| C-GST-007 | gstack framework comparison vs cross-framework final synthesis | F_GST_037, F_SUP_004, F_GSD_004, F_AID_036 | Use gstack comparison as one input, not final arbitration. | Final mechanism library decides precedence. |

## Precedence Rules

1. Specific role/workflow/checklist cards override broad reports for concrete iOS file placement.
2. Broad reports define architecture and learning path, but must be deduplicated against role cards and workflow templates.
3. Guardrail/hook mechanisms are version-gated; v0.1 keeps risk rules as documents.
4. Review depth scales with change risk; release, privacy, security, native bridge and Firebase rules get stronger gates.
5. gstack owns role/review/workflow governance; it does not replace GSD2 state management or Aider repo/file scope controls.

## Required Follow-up During Synthesis

| output | required handling |
|---|---|
| `output/frameworks/gstack_summary.md` | Include conflict section and cite this ledger. |
| `output/mechanisms/agent_roles.md` | Merge gstack role matrix with Superpowers reviewer roles and GSD2 model routing. |
| `output/mechanisms/risk_gate.md` | Include gstack guardrails, freeze/careful/guard concepts and version-gating. |
| `output/ios_harness_mapping/v0_1_scope.md` | Include role/review/risk/workflow docs; exclude hook enforcement runtime. |

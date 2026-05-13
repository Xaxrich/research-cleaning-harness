# SWE-agent Conflict Ledger

Scope: reviewed SWE-agent Source Cards `F_SWE_001` through `F_SWE_029`.

This file records cross-card tensions that must be resolved before SWE-agent mechanisms are merged with Superpowers, GSD2, Aider and gstack.

## Conflict Summary

| conflict_id | conflict | source_cards | synthesis_resolution | iOS Harness implication |
|---|---|---|---|---|
| C-SWE-001 | ACI tool contracts vs current document-only harness | F_SWE_004, F_SWE_005, F_SWE_023 | Treat tool contracts as v0.5 targets until scripts and tests exist. | v0.1 may define contracts, not claim runtime execution. |
| C-SWE-002 | Trajectory completeness vs privacy and log volume | F_SWE_007, F_SWE_021, F_SWE_026 | Log action/observation metadata and summaries; redact secrets and avoid full-source logging. | Add privacy-aware trajectory rules before implementation. |
| C-SWE-003 | Line-oriented edit safety vs Aider file-scope governance | F_SWE_017, F_SWE_019, F_AID_039 | SWE edit checks must consume Aider allowed/read-only/forbidden file rules. | `safe_edit_check.sh` should enforce both line context and file scope. |
| C-SWE-004 | Safe command runner power vs release/security risk | F_SWE_020, F_SWE_026, F_SUP_011 | Keep high-risk commands in ask/deny mode until review and approval are present. | Upload, signing, deletion and release commands need manual gate. |
| C-SWE-005 | mini-SWE simplicity vs full iOS App Store workflow needs | F_SWE_022, F_SWE_024, F_SWE_029 | Use mini-SWE as prototype loop; use workflow library for production scope. | Do not let minimal runtime define release readiness. |
| C-SWE-006 | Weak model ACI permissions vs productivity | F_SWE_025, F_GSD_012, F_AID_026 | Weak models get narrow tools and low-risk files; high-risk work escalates. | `MODEL_ROUTING.md` must bind model capability to tool permissions. |
| C-SWE-007 | Duplicate full reports, converted reports and section files | F_SWE_001, F_SWE_008, F_SWE_009, F_SWE_010, F_SWE_011, F_SWE_012-F_SWE_029 | Prefer section cards for specific mechanisms; use full reports for architecture and coverage. | Framework summary must deduplicate repeated claims. |
| C-SWE-008 | Runtime replay ambition vs v0.1 handoff timeline | F_SWE_007, F_SWE_021, F_SWE_029 | Keep replay as v1.0; v0.5 can store structured trajectory. | Avoid building replay before basic tool evidence is stable. |

## Precedence Rules

1. Specific section cards override full-report cards for tool behavior, security, workflow and trajectory details.
2. Full reports define migration thesis and coverage, but duplicate evidence must be collapsed during synthesis.
3. SWE-agent owns Action / ACI, environment feedback and trajectory; it does not replace Aider file scope, GSD2 state machine, gstack role governance or Superpowers engineering discipline.
4. All high-risk tools are version-gated and require security policy before runtime implementation.
5. Trajectory data is useful only if it remains privacy-aware, bounded and tied to verification evidence.

## Required Follow-up During Synthesis

| output | required handling |
|---|---|
| `output/frameworks/swe_agent_summary.md` | Include conflict section and cite this ledger. |
| `output/mechanisms/aci_tools.md` | Use SWE-agent as primary source for tool contracts and action/observation loop. |
| `output/mechanisms/verification.md` | Merge SWE run/verify/failure classification with Superpowers and GSD2 gates. |
| `output/ios_harness_mapping/v0_5_scope.md` | Add view/search/edit/run/trajectory scripts as v0.5 targets, not v0.1 claims. |
| `output/ios_harness_mapping/v1_0_scope.md` | Put replay, runtime interception and permission enforcement into v1.0 unless already implemented. |

# Framework Summary: swe-agent

## 1. One-line Essence

swe-agent 的可迁移价值是：执行接口：ACI tools、action/observation、safe command、trajectory/replay。

## 2. Source Coverage

| source_id | status | source_card |
| --- | --- | --- |
| F_SWE_001 | reviewed | output/source_cards/swe-agent/F_SWE_001_SWE_agent到iOS_Harness_ACI迁移_技术调研文档.md |
| F_SWE_002 | reviewed | output/source_cards/swe-agent/F_SWE_002_plan.md |
| F_SWE_003 | reviewed | output/source_cards/swe-agent/F_SWE_003_research_framework_comparison.md |
| F_SWE_004 | reviewed | output/source_cards/swe-agent/F_SWE_004_research_ios_harness_design.md |
| F_SWE_005 | reviewed | output/source_cards/swe-agent/F_SWE_005_research_swe_aci_mechanisms.md |
| F_SWE_006 | reviewed | output/source_cards/swe-agent/F_SWE_006_research_swe_repo_structure.md |
| F_SWE_007 | reviewed | output/source_cards/swe-agent/F_SWE_007_research_swe_trajectory_config.md |
| F_SWE_008 | reviewed | output/source_cards/swe-agent/F_SWE_008_swe_agent_ios_harness_agent_final_base.md |
| F_SWE_009 | reviewed | output/source_cards/swe-agent/F_SWE_009_swe_agent_ios_harness_agent_final_converted.md |
| F_SWE_010 | reviewed | output/source_cards/swe-agent/F_SWE_010_swe_agent_ios_harness_agent_final_footnote.md |
| F_SWE_011 | reviewed | output/source_cards/swe-agent/F_SWE_011_swe_agent_ios_harness_agent_final.md |
| F_SWE_012 | reviewed | output/source_cards/swe-agent/F_SWE_012_swe_agent_ios_harness_agent_outline.md |
| F_SWE_013 | reviewed | output/source_cards/swe-agent/F_SWE_013_swe_agent_ios_harness_sec01.md |
| F_SWE_014 | reviewed | output/source_cards/swe-agent/F_SWE_014_swe_agent_ios_harness_sec02.md |
| F_SWE_015 | reviewed | output/source_cards/swe-agent/F_SWE_015_swe_agent_ios_harness_sec03.md |
| F_SWE_016 | reviewed | output/source_cards/swe-agent/F_SWE_016_swe_agent_ios_harness_sec04.md |
| F_SWE_017 | reviewed | output/source_cards/swe-agent/F_SWE_017_swe_agent_ios_harness_sec05.md |
| F_SWE_018 | reviewed | output/source_cards/swe-agent/F_SWE_018_swe_agent_ios_harness_sec06.md |
| F_SWE_019 | reviewed | output/source_cards/swe-agent/F_SWE_019_swe_agent_ios_harness_sec07.md |
| F_SWE_020 | reviewed | output/source_cards/swe-agent/F_SWE_020_swe_agent_ios_harness_sec08.md |
| F_SWE_021 | reviewed | output/source_cards/swe-agent/F_SWE_021_swe_agent_ios_harness_sec09.md |
| F_SWE_022 | reviewed | output/source_cards/swe-agent/F_SWE_022_swe_agent_ios_harness_sec10.md |
| F_SWE_023 | reviewed | output/source_cards/swe-agent/F_SWE_023_swe_agent_ios_harness_sec11.md |
| F_SWE_024 | reviewed | output/source_cards/swe-agent/F_SWE_024_swe_agent_ios_harness_sec12.md |
| F_SWE_025 | reviewed | output/source_cards/swe-agent/F_SWE_025_swe_agent_ios_harness_sec13.md |
| F_SWE_026 | reviewed | output/source_cards/swe-agent/F_SWE_026_swe_agent_ios_harness_sec14.md |
| F_SWE_027 | reviewed | output/source_cards/swe-agent/F_SWE_027_swe_agent_ios_harness_sec15.md |
| F_SWE_028 | reviewed | output/source_cards/swe-agent/F_SWE_028_swe_agent_ios_harness_sec16.md |
| F_SWE_029 | reviewed | output/source_cards/swe-agent/F_SWE_029_swe_agent_ios_harness_sec17.md |

## 3. Core Mechanism Targets

| layer | count |
| --- | --- |
| Action / ACI Layer | 25 |
| Context Layer | 2 |
| Feedback / Verification Layer | 19 |
| Goal Layer | 2 |
| Harness Maintenance Layer | 20 |
| Memory / State Layer | 9 |
| Risk / Release Layer | 27 |
| Role / Review Layer | 4 |
| Task Layer | 8 |

## 4. Highest-Impact Harness Files

| harness_file | mechanism_targets |
| --- | --- |
| docs/agent/ACI_TOOL_CONTRACTS.md | 18 |
| README.md | 13 |
| RISK_CONTROL.md | 13 |
| DECISIONS.md | 10 |
| VERIFICATION_MATRIX.md | 9 |
| TASKS.md | 8 |
| FAILURE_LOG.md | 7 |
| STATE.md | 5 |
| CONFIG.md | 4 |
| docs/agent/MINI_SWE_LOOP.md | 4 |
| AGENTS.md | 2 |
| ARCHITECTURE.md | 2 |
| docs/agent/ENVIRONMENT_ABSTRACTION.md | 2 |
| scripts/agent/replay_trajectory.sh | 2 |
| docs/agent/SWE_CONCEPTS.md | 2 |

## 5. Failure Modes Addressed

| failure_mode | mechanism_count |
| --- | --- |
| stuck_loop | 32 |
| version_confusion | 20 |
| tooling_gap | 20 |
| tooling_sprawl | 20 |
| imagined_progress | 16 |
| over_complex_runtime | 16 |
| duplicate_evidence | 12 |
| unsafe_tool_use | 12 |
| privacy_leak | 12 |
| framework_role_conflict | 8 |
| over_transfer | 8 |
| weak_synthesis | 8 |
| tool_contract_ambiguity | 8 |
| unbounded_agent_action | 8 |
| architecture_opacity | 8 |

## 6. Transferable Parts

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-SWE-003 | swe-agent | F_SWE_001 | v0_1 | Versioned Scope Split |
| M-SWE-004 | swe-agent | F_SWE_001 | v0_1 | Duplicate Report Warning |
| M-SWE-005 | swe-agent | F_SWE_002 | v0_1 | SWE ACI Research Pipeline |
| M-SWE-007 | swe-agent | F_SWE_002 | v0_1 | Evidence-Bound Migration Plan |
| M-SWE-008 | swe-agent | F_SWE_002 | v0_1 | ACI Before Runtime |
| M-SWE-012 | swe-agent | F_SWE_003 | v0_1 | Conflict-Driven Synthesis |
| M-SWE-020 | swe-agent | F_SWE_005 | v0_1 | ACI Security Envelope |
| M-SWE-021 | swe-agent | F_SWE_006 | v0_1 | SWE Repo Component Map |
| M-SWE-024 | swe-agent | F_SWE_006 | v0_1 | Repository Structure Boundary |
| M-SWE-028 | swe-agent | F_SWE_007 | v0_1 | Privacy-Aware Logging |
| M-SWE-031 | swe-agent | F_SWE_008 | v0_1 | Versioned Scope Split |
| M-SWE-032 | swe-agent | F_SWE_008 | v0_1 | Duplicate Report Warning |
| M-SWE-036 | swe-agent | F_SWE_009 | v0_1 | Prototype Boundary |
| M-SWE-039 | swe-agent | F_SWE_010 | v0_1 | Versioned Scope Split |
| M-SWE-040 | swe-agent | F_SWE_010 | v0_1 | Duplicate Report Warning |
| M-SWE-044 | swe-agent | F_SWE_011 | v0_1 | Prototype Boundary |
| M-SWE-048 | swe-agent | F_SWE_012 | v0_1 | Prototype Boundary |
| M-SWE-049 | swe-agent | F_SWE_013 | v0_1 | SWE Agent Loop Concepts |
| M-SWE-051 | swe-agent | F_SWE_013 | v0_1 | Environment Feedback Reliance |
| M-SWE-052 | swe-agent | F_SWE_013 | v0_1 | Concept Boundary for iOS |
| M-SWE-053 | swe-agent | F_SWE_014 | v0_1 | SWE Repo Component Map |
| M-SWE-056 | swe-agent | F_SWE_014 | v0_1 | Repository Structure Boundary |
| M-SWE-057 | swe-agent | F_SWE_015 | v0_1 | SWE Agent Loop Concepts |
| M-SWE-059 | swe-agent | F_SWE_015 | v0_1 | Environment Feedback Reliance |

## 7. Non-transferable Parts

- Runtime interception is not transferred unless a tested script/runtime exists.
- Duplicate reports are not copied wholesale; section-level Source Cards have priority.
- Raw files remain evidence, not default context.

## 8. Conflicts

See `output/conflicts/swe_agent_conflicts.md`.

## 9. Final Judgment

Use this framework as one layer in the fused iOS Harness. Do not let it override stronger evidence from another layer.

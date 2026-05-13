# Failure Mode: architecture_opacity

## Why It Matters

This failure mode appears in 24 mechanism records and must be explicitly guarded in the iOS Harness.

## Primary Guard Files

| harness_file | mechanism_count |
| --- | --- |
| ARCHITECTURE.md | 5 |
| docs/agent/ACI_TOOL_CONTRACTS.md | 3 |
| DECISIONS.md | 3 |
| STATE.md | 2 |
| PRODUCT_SPEC.md | 2 |
| README.md | 2 |
| docs/agent/ENVIRONMENT_ABSTRACTION.md | 2 |
| CONFIG.md | 2 |
| TASKS.md | 1 |
| VERIFICATION_MATRIX.md | 1 |
| scripts/agent/runtime/lease_check.py | 1 |

## Source Evidence

| mechanism | framework | source | summary |
| --- | --- | --- | --- |
| M-GSD-065 | gsd2 | F_GSD_009 | Runtime Architecture Map |
| M-GSD-066 | gsd2 | F_GSD_009 | Auto Mode State Transition |
| M-GSD-067 | gsd2 | F_GSD_009 | Dispatch Pipeline |
| M-GSD-068 | gsd2 | F_GSD_009 | Schema-Backed Truth Source |
| M-GSD-069 | gsd2 | F_GSD_009 | Verification Evidence Table |
| M-GSD-070 | gsd2 | F_GSD_009 | Worker Lease and Command Queue |
| M-GSD-071 | gsd2 | F_GSD_009 | CLI/Headless/MCP Surfaces |
| M-GSD-072 | gsd2 | F_GSD_009 | ADR-Guided Architecture Decisions |
| M-GST-117 | gstack | F_GST_030 | Repository Architecture Map |
| M-GST-118 | gstack | F_GST_030 | Command-Skill-Hook Layers |
| M-GST-119 | gstack | F_GST_030 | Platform-Agnostic Agent Design |
| M-GST-120 | gstack | F_GST_030 | Structure-to-Handoff Map |
| M-GST-157 | gstack | F_GST_040 | Repository Architecture Map |
| M-GST-158 | gstack | F_GST_040 | Command-Skill-Hook Layers |
| M-GST-159 | gstack | F_GST_040 | Platform-Agnostic Agent Design |
| M-GST-160 | gstack | F_GST_040 | Structure-to-Handoff Map |
| M-SWE-021 | swe-agent | F_SWE_006 | SWE Repo Component Map |
| M-SWE-022 | swe-agent | F_SWE_006 | Environment Abstraction |
| M-SWE-023 | swe-agent | F_SWE_006 | Configuration as Runtime Input |
| M-SWE-024 | swe-agent | F_SWE_006 | Repository Structure Boundary |
| M-SWE-053 | swe-agent | F_SWE_014 | SWE Repo Component Map |
| M-SWE-054 | swe-agent | F_SWE_014 | Environment Abstraction |
| M-SWE-055 | swe-agent | F_SWE_014 | Configuration as Runtime Input |
| M-SWE-056 | swe-agent | F_SWE_014 | Repository Structure Boundary |

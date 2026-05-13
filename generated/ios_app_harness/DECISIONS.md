# DECISIONS

## D-001: Clean assets are runtime authority

Decision: this harness reads clean Source Cards, summaries and mechanism indexes first. Raw research stays evidence-only.

Reason: raw folders contain duplicates, reports, converted documents and proposal artifacts.

## D-002: v0.1 is docs-first

Decision: v0.1 uses task cards, scope rules, review gates and verification matrices. Scripts are optional helpers; runtime interception is not claimed.

Reason: clean data has many v0.1 mechanisms and fewer v1.0 mechanisms.

## D-003: SWE-agent owns tool contracts, not global process

Decision: ACI tools and trajectory come from SWE-agent, but task discipline, file scope, roles and review gates come from the other frameworks.

Reason: cross-framework fusion avoids letting one framework dominate.

## D-004: Every source file must be consumed

Decision: every reviewed Source Card is mapped to at least one harness file in `data/source_to_harness_trace.jsonl`.

Reason: this prevents selective cherry-picking and makes the synthesis auditable.

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-AID-032 | aider | F_AID_008 | v0_1 | Repo Map Boundary |
| M-AID-033 | aider | F_AID_009 | v0_1 | Aider Suitability Boundary |
| M-AID-132 | aider | F_AID_033 | v0_1 | Repo Map Boundary |
| M-GSD-027 | gsd2 | F_GSD_004 | v0_1 | Conflict Resolution Policy |
| M-GSD-072 | gsd2 | F_GSD_009 | v0_1 | ADR-Guided Architecture Decisions |
| M-GST-002 | gstack | F_GST_001 | v0_1 | Template Bundle Boundary |
| M-GST-064 | gstack | F_GST_016 | v0_1 | Hook-Based Enforcement Boundary |
| M-GST-144 | gstack | F_GST_036 | v0_1 | Hook-Based Enforcement Boundary |
| M-GST-147 | gstack | F_GST_037 | v0_1 | Non-Transfer Identification |
| M-GST-156 | gstack | F_GST_039 | v0_1 | Skill Portability Boundary |
| M-SWE-008 | swe-agent | F_SWE_002 | v0_1 | ACI Before Runtime |
| M-SWE-024 | swe-agent | F_SWE_006 | v0_1 | Repository Structure Boundary |
| M-SWE-036 | swe-agent | F_SWE_009 | v0_1 | Prototype Boundary |
| M-SWE-044 | swe-agent | F_SWE_011 | v0_1 | Prototype Boundary |
| M-SWE-048 | swe-agent | F_SWE_012 | v0_1 | Prototype Boundary |
| M-SWE-052 | swe-agent | F_SWE_013 | v0_1 | Concept Boundary for iOS |
| M-SWE-056 | swe-agent | F_SWE_014 | v0_1 | Repository Structure Boundary |
| M-SWE-060 | swe-agent | F_SWE_015 | v0_1 | Concept Boundary for iOS |

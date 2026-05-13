# EXTRACTION SCHEMA

Every source file must be converted into one Source Card before it can influence framework summaries or mechanism libraries.

## Required Source Card Sections

1. Metadata
2. One-line Essence
3. File Summary
4. Core Mechanisms Extracted
5. Failure Modes Addressed
6. Design Logic
7. 5 Why Analysis
8. Evidence Snippets
9. iOS Harness Mapping
10. Transfer Decision
11. Uncertainties
12. Related Source Cards
13. Clean Summary for Codex

## Mechanism Record

Use this normalized shape when extracting a mechanism:

```yaml
mechanism:
  id:
  name:
  source_framework:
  source_file_id:
  description:
  failure_modes:
    - context_pollution
  ios_harness_targets:
    - target_layer:
      target_file:
  version_priority: v0_1 | v0_5 | v1_0 | no_transfer
  confidence: high | medium | low
  evidence:
    - evidence_id:
      source_location:
      quote_or_summary:
```

After Source Cards are reviewed, the same normalized mechanism shape must be materialized in:

```text
output/data/mechanisms.jsonl
```

Each JSONL row must represent exactly one mechanism and include enough data for cross-framework grouping by:

- source framework
- source file
- failure mode
- iOS Harness target file
- version priority
- confidence
- evidence

## Allowed iOS Harness Target Layers

- Goal Layer
- Context Layer
- Task Layer
- Action / ACI Layer
- Feedback / Verification Layer
- Memory / State Layer
- Role / Review Layer
- Risk / Release Layer
- Harness Maintenance Layer

## Version Priorities

| version | meaning |
|---|---|
| v0_1 | minimal rule/doc/process that can be adopted immediately |
| v0_5 | enhanced workflow with automation or stronger templates |
| v1_0 | runtime or CI enforced mechanism |
| no_transfer | useful context, but should not be transferred |

## Evidence Rules

- Prefer short evidence summaries with source line references.
- Do not copy large raw passages.
- Mark inferred statements with `inferred`.
- If a source file contradicts itself, record the conflict instead of resolving it silently.
- If a conclusion depends on another file, leave it as an uncertainty until that file has its own Source Card.

# STATE

phase: layered_ios_app_development_harness_generated
current_framework: none
current_file_id: none
raw_root: raw/
inventory_count: 134
framework_inventory_counts:
  superpowers: 14
  gsd2: 12
  aider: 39
  gstack: 40
  swe-agent: 29
reviewed_source_card_count: 134
last_updated: 2026-05-14

completed_frameworks:
  - superpowers_source_cards
  - gsd2_source_cards
  - aider_source_cards
  - gstack_source_cards
  - swe_agent_source_cards

completed_files:
  - F_SUP_001-F_SUP_014
  - F_GSD_001-F_GSD_012
  - F_AID_001-F_AID_039
  - F_GST_001-F_GST_040
  - F_SWE_001-F_SWE_029

reviewed_files:
  - F_SUP_001-F_SUP_014
  - F_GSD_001-F_GSD_012
  - F_AID_001-F_AID_039
  - F_GST_001-F_GST_040
  - F_SWE_001-F_SWE_029

in_progress:
  - none

blocked:
  - none

next:
  - use `ios_app_development_harness/` as the final layered standalone development framework
  - copy it into a real iOS app repo as `agent_harness/`
  - start from `START_HERE.md` and `CALL_GRAPH.md`
  - adapt project-specific layer files before enabling scripts

notes:
  - Superpowers, GSD2, Aider, gstack, and SWE-agent Source Cards are reviewed and indexed in `output/data/source_cards.jsonl`.
  - gstack has 40 reviewed Source Cards, 40 review files, and `output/conflicts/gstack_conflicts.md`.
  - SWE-agent has 29 reviewed Source Cards, 29 review files, and `output/conflicts/swe_agent_conflicts.md`.
  - `output/data/mechanisms.jsonl` currently contains 625 mechanism records.
  - Lightweight iOS Harness generated at `generated/ios_app_harness/`.
  - Layered Standalone iOS App Development Harness generated at `ios_app_development_harness/`.
  - `ios_app_development_harness/START_HERE.md` and `ios_app_development_harness/CALL_GRAPH.md` are the primary entry files.
  - `ios_app_development_harness/FULL_TUTORIAL.md` is the full teaching tutorial.
  - Framework summaries, mechanism docs, failure mode docs, and iOS mapping docs are generated from clean outputs.
  - `generated/ios_app_harness/data/source_to_harness_trace.jsonl` covers all 134 reviewed Source Cards.
  - `generated/ios_app_harness/data/mechanism_targets.jsonl` contains 629 mechanism target rows.
  - AppleDouble metadata files named `._*` are ignored and should be deleted before commit.
  - Local git repository has been initialized in `research_cleaning_harness/`; the sibling `raw/` directory is outside the repo scope.
  - Public GitHub repo is published at `git@github.com:Xaxrich/research-cleaning-harness.git`.
  - GitHub CLI API auth remains invalid, but SSH push works with `/Users/a58/.ssh/id_ed25519_xtaxharness_github`.

# STATE

phase: all_source_cards_reviewed
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
last_updated: 2026-05-13

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
  - GitHub public upload is blocked until `gh auth login -h github.com` refreshes the invalid token for account `Xaxrich`.

next:
  - run full validation after SWE-agent cleaning
  - begin framework summaries one framework at a time
  - then synthesize mechanisms and iOS Harness mapping

notes:
  - Superpowers, GSD2, Aider, gstack, and SWE-agent Source Cards are reviewed and indexed in `output/data/source_cards.jsonl`.
  - gstack has 40 reviewed Source Cards, 40 review files, and `output/conflicts/gstack_conflicts.md`.
  - SWE-agent has 29 reviewed Source Cards, 29 review files, and `output/conflicts/swe_agent_conflicts.md`.
  - `output/data/mechanisms.jsonl` currently contains 625 mechanism records.
  - AppleDouble metadata files named `._*` are ignored but not deleted.
  - Local git repository has been initialized in `research_cleaning_harness/`; the sibling `raw/` directory is outside the repo scope.

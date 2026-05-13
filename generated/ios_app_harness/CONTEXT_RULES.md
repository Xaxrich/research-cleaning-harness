# CONTEXT RULES

## Default

Read less, but read the right files. Search before broad reading. View before edit.

## Required For Every Task

- `STATE.md`
- Current task card in `TASKS.md`
- `FILE_SCOPE_RULES.md`
- Relevant entries from `CONTEXT_INDEX.md`
- The files explicitly listed in `allowed_files` or `read_only_files`

## Forbidden By Default

- Raw research folders.
- Unrelated framework reports.
- Secrets, certificates, provisioning profiles and private env files.
- Entire large files when a line window is enough.

## Evidence Pull

| mechanism | framework | source | version | reason |
| --- | --- | --- | --- | --- |
| M-AID-046 | aider | F_AID_012 | v0_1 | Conventions as Read-Only Context |
| M-AID-050 | aider | F_AID_013 | v0_1 | Read-Only Files Contract |
| M-AID-078 | aider | F_AID_020 | v0_1 | Conventions as Read-Only Context |
| M-AID-082 | aider | F_AID_021 | v0_1 | Conventions as Read-Only Context |
| M-AID-086 | aider | F_AID_022 | v0_1 | Conventions as Read-Only Context |
| M-AID-090 | aider | F_AID_023 | v0_1 | Conventions as Read-Only Context |
| M-AID-110 | aider | F_AID_028 | v0_1 | Read-Only Files Contract |
| M-AID-154 | aider | F_AID_039 | v0_1 | Read-Only Files Contract |
| M-GSD-017 | gsd2 | F_GSD_003 | v0_1 | Research Topic Partition |
| M-GSD-040 | gsd2 | F_GSD_006 | v0_1 | Fresh Session per Task |
| M-GSD-047 | gsd2 | F_GSD_007 | v0_1 | Context Window Binding |
| M-GSD-051 | gsd2 | F_GSD_007 | v0_1 | Excluded Content Rule |
| M-GSD-074 | gsd2 | F_GSD_010 | v0_1 | One Task per Context Window |
| M-GSD-077 | gsd2 | F_GSD_010 | v0_1 | Excluded Contexts |
| M-GST-049 | gstack | F_GST_013 | v0_1 | Search Before Building |
| M-GST-121 | gstack | F_GST_031 | v0_1 | Search Before Building |
| M-GST-129 | gstack | F_GST_033 | v0_1 | Search Before Building |
| M-GST-133 | gstack | F_GST_034 | v0_1 | Search Before Building |

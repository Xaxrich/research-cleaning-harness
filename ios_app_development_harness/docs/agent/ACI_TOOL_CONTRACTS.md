# ACI TOOL CONTRACTS

ACI means Agent-Computer Interface: the controlled surface through which an agent reads, searches, edits, runs commands and records observations.

| tool | purpose | risk |
|---|---|---|
| `view_file.sh` | bounded file view with line numbers | low |
| `search_code.sh` | scoped code search | low |
| `safe_edit_check.sh` | pre-edit risk check | medium |
| `run_safe_command.sh` | allowlisted command runner | medium |
| `context_pack.sh` | print required context for a task | low |

These scripts are helper tools, not a full runtime security layer.

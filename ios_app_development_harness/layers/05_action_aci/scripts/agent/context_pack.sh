#!/usr/bin/env bash
set -euo pipefail

task="${1:-TASKS.md}"
printf 'task_file: %s\n' "$task"
printf 'required_context:\n'
printf '  - AGENTS.md\n'
printf '  - CALL_GRAPH.md\n'
printf '  - layers/08_memory_state/STATE.md\n'
printf '  - layers/01_task/TASKS.md\n'
printf '  - layers/02_context/CONTEXT_INDEX.md\n'
printf '  - layers/03_file_scope/FILE_SCOPE_RULES.md\n'
printf '  - layers/06_verification/VERIFICATION_MATRIX.md\n'
printf '  - layers/07_risk_release/RISK_CONTROL.md\n'

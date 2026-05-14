#!/usr/bin/env bash
set -euo pipefail

task="${1:-TASKS.md}"
printf 'task_file: %s\n' "$task"
printf 'required_context:\n'
printf '  - STATE.md\n'
printf '  - TASKS.md\n'
printf '  - CONTEXT_INDEX.md\n'
printf '  - FILE_SCOPE_RULES.md\n'
printf '  - VERIFICATION_MATRIX.md\n'
printf '  - RISK_CONTROL.md\n'

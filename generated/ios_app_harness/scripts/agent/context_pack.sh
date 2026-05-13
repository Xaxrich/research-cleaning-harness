#!/usr/bin/env bash
set -euo pipefail

task_file="${1:-TASKS.md}"

printf 'context_pack_generated_at: %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
printf 'task_file: %s\n' "$task_file"
printf 'required:\n'
printf '  - STATE.md\n'
printf '  - TASKS.md\n'
printf '  - CONTEXT_INDEX.md\n'
printf '  - FILE_SCOPE_RULES.md\n'
printf '  - VERIFICATION_MATRIX.md\n'

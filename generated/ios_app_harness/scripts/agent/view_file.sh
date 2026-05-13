#!/usr/bin/env bash
set -euo pipefail

file="${1:-}"
start="${2:-1}"
count="${3:-120}"

if [[ -z "$file" || ! -f "$file" ]]; then
  echo "usage: view_file.sh <file> [start_line] [line_count]" >&2
  exit 2
fi

if [[ "$file" == raw/* || "$file" == */raw/* ]]; then
  echo "deny: raw research files are not runtime context" >&2
  exit 3
fi

awk -v start="$start" -v count="$count" 'NR >= start && NR < start + count { printf "%6d  %s\n", NR, $0 }' "$file"

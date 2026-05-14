#!/usr/bin/env bash
set -euo pipefail

pattern="${1:-}"
scope="${2:-.}"

if [[ -z "$pattern" ]]; then
  echo "usage: search_code.sh <pattern> [scope]" >&2
  exit 2
fi

rg --line-number --hidden --glob '!**/._*' "$pattern" "$scope"

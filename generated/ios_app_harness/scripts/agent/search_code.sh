#!/usr/bin/env bash
set -euo pipefail

pattern="${1:-}"
scope="${2:-.}"

if [[ -z "$pattern" ]]; then
  echo "usage: search_code.sh <pattern> [scope]" >&2
  exit 2
fi

if [[ "$scope" == raw* || "$scope" == */raw/* ]]; then
  echo "deny: raw research scope is not searchable by runtime harness" >&2
  exit 3
fi

rg --line-number --hidden --glob '!raw/**' --glob '!**/._*' "$pattern" "$scope"

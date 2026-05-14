#!/usr/bin/env bash
set -euo pipefail

target="${1:-}"
dest="${2:-agent_harness}"

if [[ -z "$target" || ! -d "$target" ]]; then
  echo "usage: install_into_repo.sh <target_repo_dir> [dest_dir_name]" >&2
  exit 2
fi

src="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cp -R "$src" "$target/$dest"
echo "installed harness to $target/$dest"

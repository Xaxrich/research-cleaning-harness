#!/usr/bin/env bash
set -euo pipefail

if [[ "$#" -eq 0 ]]; then
  echo "usage: run_safe_command.sh <command> [args...]" >&2
  exit 2
fi

cmd="$1"
shift || true

case "$cmd" in
  flutter)
    case "${1:-}" in analyze|test) exec flutter "$@" ;; esac
    ;;
  xcodebuild)
    case "${1:-}" in -list|-showBuildSettings|build|test) exec xcodebuild "$@" ;; esac
    ;;
  swift)
    case "${1:-}" in build|test) exec swift "$@" ;; esac
    ;;
  git)
    case "${1:-}" in status|diff|show|log) exec git "$@" ;; esac
    ;;
  rg)
    exec rg "$@"
    ;;
esac

echo "ask: command is not allowlisted: $cmd $*" >&2
exit 10

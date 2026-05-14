#!/usr/bin/env bash
set -euo pipefail

target="${1:-}"
if [[ -z "$target" ]]; then
  echo "usage: safe_edit_check.sh <target_file>" >&2
  exit 2
fi

case "$target" in
  *.p12|*.mobileprovision|*.cer|*.key|*.pem|.env*|*/.env*)
    echo "deny: secret/signing file: $target" >&2
    exit 3
    ;;
  *GoogleService-Info.plist|*firebase_options.*|*Entitlements.plist|*Info.plist|*firestore.rules|*storage.rules|*firebase.rules)
    echo "ask: high-risk iOS/Firebase file requires review: $target"
    exit 10
    ;;
esac

echo "allow: $target"

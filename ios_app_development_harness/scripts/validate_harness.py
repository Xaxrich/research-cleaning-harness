#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "FULL_TUTORIAL.md",
    "FRAMEWORK_SPEC.md",
    "AGENTS.md",
    "PRODUCT_SPEC.md",
    "STATE.md",
    "TASKS.md",
    "CONTEXT_INDEX.md",
    "CONTEXT_RULES.md",
    "FILE_SCOPE_RULES.md",
    "HIGH_RISK_FILES.md",
    "ROLE_MATRIX.md",
    "REVIEW_MATRIX.md",
    "RISK_CONTROL.md",
    "VERIFICATION_MATRIX.md",
    "MODEL_ROUTING.md",
    "GIT_WORKFLOW.md",
    "IOS_RELEASE_CHECKLIST.md",
    "FAILURE_LOG.md",
    "docs/agent/ACI_TOOL_CONTRACTS.md",
    "docs/agent/TESTING_GUIDE.md",
    "docs/agent/DEBUG_GUIDE.md",
    "docs/agent/WORKFLOW_CHAIN.md",
    "docs/agent/BOOTSTRAP.md",
    "templates/task_card.md",
    "templates/review_template.md",
    "templates/manual_approval.md",
    "templates/pr_description.md",
    "examples/task_docs_only.md",
    "examples/task_flutter_ui.md",
    "examples/task_firebase_rules.md",
    "examples/task_swift_bridge.md",
    "examples/task_release_prep.md",
    "examples/codex_prompts.md",
    "scripts/agent/view_file.sh",
    "scripts/agent/search_code.sh",
    "scripts/agent/safe_edit_check.sh",
    "scripts/agent/run_safe_command.sh",
    "scripts/agent/context_pack.sh",
]

KEY_TERMS = {
    "TASKS.md": ["allowed_files", "read_only_files", "forbidden_files"],
    "FILE_SCOPE_RULES.md": ["allowed", "read-only", "forbidden"],
    "RISK_CONTROL.md": ["release_blocking", "Manual Approval"],
    "VERIFICATION_MATRIX.md": ["Completion Rule"],
    "FULL_TUTORIAL.md": ["设计细节点", "最短可用路径"],
}


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")
    for rel, terms in KEY_TERMS.items():
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for term in terms:
            if term not in text:
                errors.append(f"{rel} missing term: {term}")

    for error in errors:
        print(error)
    print(f"validated standalone ios app development harness, failures: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

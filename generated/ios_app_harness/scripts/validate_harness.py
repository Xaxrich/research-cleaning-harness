#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ['README.md', 'AGENTS.md', 'PRODUCT_SPEC.md', 'STATE.md', 'TASKS.md', 'DECISIONS.md', 'CONTEXT_INDEX.md', 'CONTEXT_RULES.md', 'FILE_SCOPE_RULES.md', 'HIGH_RISK_FILES.md', 'ROLE_MATRIX.md', 'REVIEW_MATRIX.md', 'RISK_CONTROL.md', 'MODEL_ROUTING.md', 'VERIFICATION_MATRIX.md', 'FAILURE_LOG.md', 'GIT_WORKFLOW.md', 'IOS_RELEASE_CHECKLIST.md', 'docs/agent/ACI_TOOL_CONTRACTS.md', 'docs/agent/REPO_CONTEXT.md', 'docs/agent/EDIT_FORMATS.md', 'docs/agent/WORKFLOW_CHAIN.md', 'docs/agent/TESTING_GUIDE.md', 'docs/agent/DEBUG_GUIDE.md', 'docs/agent/RISK_GATE.md', 'docs/agent/SWE_CONCEPTS.md', 'docs/agent/MINI_SWE_LOOP.md', 'templates/task_card.md', 'templates/review_template.md', 'templates/manual_approval.md', 'templates/pr_description.md', 'scripts/agent/view_file.sh', 'scripts/agent/search_code.sh', 'scripts/agent/safe_edit_check.sh', 'scripts/agent/run_safe_command.sh', 'scripts/agent/context_pack.sh', 'scripts/validate_harness.py', 'data/mechanism_targets.jsonl', 'data/source_to_harness_trace.jsonl']


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")

    traces = read_jsonl(ROOT / "data" / "source_to_harness_trace.jsonl")
    targets = read_jsonl(ROOT / "data" / "mechanism_targets.jsonl")

    if len(traces) != 134:
        errors.append(f"expected 134 source traces, got {len(traces)}")
    if len(targets) != 629:
        errors.append(f"expected 629 mechanism target rows, got {len(targets)}")

    uncovered = [row["source_id"] for row in traces if not row.get("harness_files")]
    if uncovered:
        errors.append("uncovered source cards: " + ", ".join(uncovered[:20]))

    for rel in ("README.md", "AGENTS.md", "TASKS.md", "VERIFICATION_MATRIX.md", "RISK_CONTROL.md"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        if "Evidence Pull" not in text:
            errors.append(f"missing Evidence Pull section: {rel}")

    for error in errors:
        print(error)
    print(f"validated ios_app_harness, failures: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

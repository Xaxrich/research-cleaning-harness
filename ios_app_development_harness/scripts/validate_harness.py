#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "START_HERE.md",
    "CALL_GRAPH.md",
    "AGENTS.md",
    "FRAMEWORK_SPEC.md",
    "FULL_TUTORIAL.md",
    "docs/superpowers/plans/2026-05-14-harness-vnext.md",
    "layers/00_goal/DISCOVERY_GATE.md",
    "layers/00_goal/PRODUCT_BRIEF.md",
    "layers/00_goal/PRODUCT_SPEC.md",
    "layers/01_planning/README.md",
    "layers/01_planning/SOLUTION_PLAN.md",
    "layers/01_planning/TASK_BREAKDOWN.md",
    "layers/01_planning/USER_CONFIRMATION.md",
    "layers/01_planning/GATE_OUTPUT_PROTOCOL.md",
    "layers/01_planning/templates/module_plan.md",
    "layers/01_task/TASKS.md",
    "layers/01_task/templates/task_card.md",
    "layers/02_context/CONTEXT_INDEX.md",
    "layers/02_context/CONTEXT_RULES.md",
    "layers/03_file_scope/FILE_SCOPE_RULES.md",
    "layers/03_file_scope/HIGH_RISK_FILES.md",
    "layers/04_roles_review/ROLE_MATRIX.md",
    "layers/04_roles_review/REVIEW_MATRIX.md",
    "layers/04_roles_review/MODEL_ROUTING.md",
    "layers/04_roles_review/templates/review_template.md",
    "layers/05_action_aci/ACI_TOOL_CONTRACTS.md",
    "layers/05_action_aci/scripts/agent/view_file.sh",
    "layers/05_action_aci/scripts/agent/search_code.sh",
    "layers/05_action_aci/scripts/agent/safe_edit_check.sh",
    "layers/05_action_aci/scripts/agent/run_safe_command.sh",
    "layers/05_action_aci/scripts/agent/context_pack.sh",
    "layers/06_verification/VERIFICATION_MATRIX.md",
    "layers/06_verification/MODULE_VERIFICATION_POLICY.md",
    "layers/06_verification/SIMULATOR_TEST_POLICY.md",
    "layers/06_verification/ACCEPTANCE_CHECKLIST.md",
    "layers/06_verification/TESTING_GUIDE.md",
    "layers/06_verification/DEBUG_GUIDE.md",
    "layers/07_risk_release/RISK_CONTROL.md",
    "layers/07_risk_release/IOS_RELEASE_CHECKLIST.md",
    "layers/07_risk_release/templates/manual_approval.md",
    "layers/08_memory_state/STATE.md",
    "layers/08_memory_state/FAILURE_LOG.md",
    "layers/08_memory_state/DECISIONS.md",
    "layers/08_memory_state/GIT_WORKFLOW.md",
    "layers/08_memory_state/RUN_TRACE.md",
    "layers/08_memory_state/RETROSPECTIVE.md",
    "layers/09_workflows/WORKFLOW_CHAIN.md",
    "layers/09_workflows/BOOTSTRAP.md",
    "layers/10_examples/task_docs_only.md",
    "layers/10_examples/task_flutter_ui.md",
    "layers/10_examples/task_firebase_rules.md",
    "layers/10_examples/task_swift_bridge.md",
    "layers/10_examples/task_release_prep.md",
    "layers/10_examples/codex_prompts.md",
    "scripts/validate_harness.py",
    "scripts/install_into_repo.sh",
]

KEY_TERMS = {
    "CALL_GRAPH.md": ["主调用链", "失败调用链", "高风险调用链"],
    "AGENTS.md": ["Required Read Order", "Non-Negotiable Rules", "DISCOVERY_GATE.md", "需要你决定"],
    "layers/00_goal/DISCOVERY_GATE.md": ["Blocking Rule", "Required Questions"],
    "layers/01_planning/SOLUTION_PLAN.md": ["Blocking Rule", "Verification Strategy"],
    "layers/01_planning/USER_CONFIRMATION.md": ["Single-action Rule", "Decision Placement Rule", "Document Target Rule", "GATE_OUTPUT_PROTOCOL.md", "需要你决定"],
    "layers/01_planning/GATE_OUTPUT_PROTOCOL.md": ["Core Rule", "Required Response Shape", "当前门禁", "当前阶段", "你要看的文档", "回答后会写入", "本次确认什么", "需要你决定", "Anti-patterns"],
    "layers/01_task/TASKS.md": ["allowed_files", "read_only_files", "forbidden_files"],
    "layers/01_task/templates/task_card.md": ["verification_level", "Done Definition"],
    "layers/03_file_scope/FILE_SCOPE_RULES.md": ["allowed", "read-only", "forbidden"],
    "layers/06_verification/VERIFICATION_MATRIX.md": ["Completion Rule", "Verification Levels"],
    "layers/06_verification/MODULE_VERIFICATION_POLICY.md": ["Verification Levels", "Module Defaults"],
    "layers/06_verification/SIMULATOR_TEST_POLICY.md": ["Simulator testing", "Waiver"],
    "layers/07_risk_release/RISK_CONTROL.md": ["release_blocking", "Manual Approval"],
    "layers/08_memory_state/RUN_TRACE.md": ["Required Fields", "Privacy Rule"],
    "layers/10_examples/codex_prompts.md": ["Standard Gate Reply Example", "需要你决定", "你要看的文档"],
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
    print(f"validated layered ios app development harness, failures: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

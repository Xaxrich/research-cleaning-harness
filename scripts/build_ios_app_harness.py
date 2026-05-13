#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import stat
from collections import Counter, defaultdict
from pathlib import Path
from textwrap import dedent


HARNESS_ROOT = Path(__file__).resolve().parents[1]
GENERATED_ROOT = HARNESS_ROOT / "generated" / "ios_app_harness"
MAPPING_ROOT = HARNESS_ROOT / "output" / "ios_harness_mapping"
FRAMEWORKS_ROOT = HARNESS_ROOT / "output" / "frameworks"
MECHANISMS_ROOT = HARNESS_ROOT / "output" / "mechanisms"
FAILURE_MODES_ROOT = HARNESS_ROOT / "output" / "failure_modes"


FRAMEWORK_ORDER = ["superpowers", "gsd2", "aider", "gstack", "swe-agent"]
FRAMEWORK_SUMMARY_NAMES = {
    "superpowers": "superpowers_summary.md",
    "gsd2": "gsd2_summary.md",
    "aider": "aider_summary.md",
    "gstack": "gstack_summary.md",
    "swe-agent": "swe_agent_summary.md",
}

FRAMEWORK_CORE = {
    "superpowers": "工程纪律：planning、TDD、debugging、review、verification-before-completion。",
    "gsd2": "状态与恢复：task state machine、context isolation、failure recovery、model routing。",
    "aider": "仓库上下文：repo map、explicit file scope、read-only context、Git/verification loop。",
    "gstack": "角色治理：role matrix、review matrix、workflow、risk/blocking rights。",
    "swe-agent": "执行接口：ACI tools、action/observation、safe command、trajectory/replay。",
}

LAYER_TO_CORE_FILE = {
    "Goal Layer": "PRODUCT_SPEC.md",
    "Context Layer": "CONTEXT_INDEX.md",
    "Task Layer": "TASKS.md",
    "Action / ACI Layer": "docs/agent/ACI_TOOL_CONTRACTS.md",
    "Feedback / Verification Layer": "VERIFICATION_MATRIX.md",
    "Memory / State Layer": "STATE.md",
    "Role / Review Layer": "ROLE_MATRIX.md",
    "Risk / Release Layer": "RISK_CONTROL.md",
    "Harness Maintenance Layer": "README.md",
}

REQUIRED_HARNESS_FILES = [
    "README.md",
    "AGENTS.md",
    "PRODUCT_SPEC.md",
    "STATE.md",
    "TASKS.md",
    "DECISIONS.md",
    "CONTEXT_INDEX.md",
    "CONTEXT_RULES.md",
    "FILE_SCOPE_RULES.md",
    "HIGH_RISK_FILES.md",
    "ROLE_MATRIX.md",
    "REVIEW_MATRIX.md",
    "RISK_CONTROL.md",
    "MODEL_ROUTING.md",
    "VERIFICATION_MATRIX.md",
    "FAILURE_LOG.md",
    "GIT_WORKFLOW.md",
    "IOS_RELEASE_CHECKLIST.md",
    "docs/agent/ACI_TOOL_CONTRACTS.md",
    "docs/agent/REPO_CONTEXT.md",
    "docs/agent/EDIT_FORMATS.md",
    "docs/agent/WORKFLOW_CHAIN.md",
    "docs/agent/TESTING_GUIDE.md",
    "docs/agent/DEBUG_GUIDE.md",
    "docs/agent/RISK_GATE.md",
    "docs/agent/SWE_CONCEPTS.md",
    "docs/agent/MINI_SWE_LOOP.md",
    "templates/task_card.md",
    "templates/review_template.md",
    "templates/manual_approval.md",
    "templates/pr_description.md",
    "scripts/agent/view_file.sh",
    "scripts/agent/search_code.sh",
    "scripts/agent/safe_edit_check.sh",
    "scripts/agent/run_safe_command.sh",
    "scripts/agent/context_pack.sh",
    "scripts/validate_harness.py",
    "data/mechanism_targets.jsonl",
    "data/source_to_harness_trace.jsonl",
]


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write(path: Path, content: str, executable: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    if executable:
        current = path.stat().st_mode
        path.chmod(current | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def slug(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9_./-]+", "_", value)
    return re.sub(r"_+", "_", value).strip("_")


def harness_file_for(target_layer: str, target_file: str) -> str:
    target = target_file.strip()
    if not target or target == "scripts/agent/":
        return "docs/agent/ACI_TOOL_CONTRACTS.md"
    if ";" in target:
        return LAYER_TO_CORE_FILE.get(target_layer, "README.md")
    if target.startswith("output/"):
        return LAYER_TO_CORE_FILE.get(target_layer, "README.md")
    if target.startswith("scripts/agent/"):
        if target.endswith("/"):
            return "docs/agent/ACI_TOOL_CONTRACTS.md"
        return target
    if target.startswith("docs/agent/") or target.startswith("templates/"):
        return target
    name = Path(target).name
    upper = target.upper()
    if "CONTEXT" in upper:
        return "CONTEXT_RULES.md" if "RULE" in upper else "CONTEXT_INDEX.md"
    if "FILE_SCOPE" in upper:
        return "FILE_SCOPE_RULES.md"
    if "HIGH_RISK" in upper:
        return "HIGH_RISK_FILES.md"
    if "ROLE" in upper:
        return "ROLE_MATRIX.md"
    if "REVIEW" in upper:
        return "REVIEW_MATRIX.md"
    if "RISK" in upper or "PRIVACY" in upper:
        return "RISK_CONTROL.md"
    if "MODEL" in upper:
        return "MODEL_ROUTING.md"
    if "VERIFY" in upper or "VERIFICATION" in upper or "TEST" in upper:
        return "VERIFICATION_MATRIX.md"
    if "RELEASE" in upper or "APP_STORE" in upper or "IOS_RELEASE" in upper:
        return "IOS_RELEASE_CHECKLIST.md"
    if "GIT" in upper:
        return "GIT_WORKFLOW.md"
    if "STATE" in upper:
        return "STATE.md"
    if "TASK" in upper:
        return "TASKS.md"
    if "DECISION" in upper:
        return "DECISIONS.md"
    if name.endswith(".md"):
        return name
    return LAYER_TO_CORE_FILE.get(target_layer, "README.md")


def mechanism_target_rows(mechanisms: list[dict]) -> list[dict]:
    rows: list[dict] = []
    for mechanism in mechanisms:
        for target in mechanism.get("ios_harness_targets", []):
            rows.append(
                {
                    "mechanism_id": mechanism["id"],
                    "mechanism_name": mechanism["name"],
                    "source_framework": mechanism["source_framework"],
                    "source_file_id": mechanism["source_file_id"],
                    "source_card": mechanism["source_card"],
                    "target_layer": target["target_layer"],
                    "target_file": target["target_file"],
                    "version": target["version"],
                    "harness_file": harness_file_for(target["target_layer"], target["target_file"]),
                    "failure_modes": mechanism.get("failure_modes", []),
                    "evidence_count": len(mechanism.get("evidence", [])),
                }
            )
    return rows


def table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    header = rows[0]
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    for row in rows[1:]:
        lines.append("| " + " | ".join(str(cell).replace("|", "/") for cell in row) + " |")
    return "\n".join(lines)


def top_mechanisms(rows: list[dict], limit: int = 16) -> list[dict]:
    seen: set[str] = set()
    selected: list[dict] = []
    rows = sorted(rows, key=lambda r: (r["version"] != "v0_1", r["source_framework"], r["mechanism_id"]))
    for row in rows:
        if row["mechanism_id"] in seen:
            continue
        seen.add(row["mechanism_id"])
        selected.append(row)
        if len(selected) >= limit:
            break
    return selected


def evidence_section(rows: list[dict], limit: int = 18) -> str:
    selected = top_mechanisms(rows, limit)
    if not selected:
        return "No direct clean-data mechanism rows target this file yet."
    return table(
        [
            ["mechanism", "framework", "source", "version", "reason"],
            *[
                [
                    row["mechanism_id"],
                    row["source_framework"],
                    row["source_file_id"],
                    row["version"],
                    row["mechanism_name"],
                ]
                for row in selected
            ],
        ]
    )


def write_data_files(target_rows: list[dict], source_cards: list[dict]) -> None:
    source_to_rows: dict[str, list[dict]] = defaultdict(list)
    for row in target_rows:
        source_to_rows[row["source_file_id"]].append(row)

    mechanism_path = GENERATED_ROOT / "data" / "mechanism_targets.jsonl"
    trace_path = GENERATED_ROOT / "data" / "source_to_harness_trace.jsonl"
    write(mechanism_path, "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in target_rows))

    traces: list[dict] = []
    for source in sorted(source_cards, key=lambda r: r["source_id"]):
        rows = source_to_rows[source["source_id"]]
        targets = sorted({row["harness_file"] for row in rows})
        traces.append(
            {
                "source_id": source["source_id"],
                "framework": source["framework"],
                "source_card": source["source_card"],
                "mechanism_count": len({row["mechanism_id"] for row in rows}),
                "harness_files": targets,
                "primary_harness_file": targets[0] if targets else "",
            }
        )
    write(trace_path, "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in traces))


def rows_for_file(target_rows: list[dict], *files: str) -> list[dict]:
    file_set = set(files)
    return [row for row in target_rows if row["harness_file"] in file_set]


def rows_for_layer(target_rows: list[dict], layer: str) -> list[dict]:
    return [row for row in target_rows if row["target_layer"] == layer]


def write_core_harness(target_rows: list[dict], source_cards: list[dict]) -> None:
    framework_counts = Counter(row["source_framework"] for row in target_rows)
    layer_counts = Counter(row["target_layer"] for row in target_rows)
    version_counts = Counter(row["version"] for row in target_rows)

    write(
        GENERATED_ROOT / "README.md",
        f"""# Lightweight iOS App Harness

This is the v0.1 harness distilled from the reviewed Research Cleaning Harness assets.

It intentionally starts as a docs-first, evidence-backed operating layer for Codex and other coding agents working on an iOS app. Runtime enforcement is version-gated: v0.1 is rules and task discipline, v0.5 adds scripts, v1.0 adds stronger interception/replay.

## Data Basis

{table([
    ["metric", "count"],
    ["reviewed Source Cards", str(len(source_cards))],
    ["mechanism target rows", str(len(target_rows))],
    ["frameworks", ", ".join(FRAMEWORK_ORDER)],
    ["v0_1 mechanisms", str(version_counts["v0_1"])],
    ["v0_5 mechanisms", str(version_counts["v0_5"])],
    ["v1_0 mechanisms", str(version_counts["v1_0"])],
])}

## Fusion Rule

{table([
    ["framework", "primary contribution"],
    *[[framework, FRAMEWORK_CORE[framework]] for framework in FRAMEWORK_ORDER],
])}

## Operating Loop

1. Select or create one task in `TASKS.md`.
2. Load only the context listed in `CONTEXT_INDEX.md` and `CONTEXT_RULES.md`.
3. Lock editable, read-only and forbidden files using `FILE_SCOPE_RULES.md`.
4. Pick the role and review gate from `ROLE_MATRIX.md` and `REVIEW_MATRIX.md`.
5. Use ACI-style tools from `docs/agent/ACI_TOOL_CONTRACTS.md` and `scripts/agent/`.
6. Run the task-specific checks from `VERIFICATION_MATRIX.md`.
7. Update `STATE.md`, `FAILURE_LOG.md`, and Git evidence before claiming completion.

## Layer Coverage

{table([["layer", "mechanism targets"], *[[layer, str(layer_counts[layer])] for layer in sorted(layer_counts)]])}

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "README.md"), 18)}

## Source Trace

Every reviewed source card is represented in `data/source_to_harness_trace.jsonl`. Human-readable coverage is in `../output/ios_harness_mapping/source_to_harness_trace.md` from the cleaning project.
""",
    )

    write(
        GENERATED_ROOT / "AGENTS.md",
        f"""# AGENTS

## Prime Directive

You are operating inside a lightweight iOS App Harness. Your job is not to be clever with a large context; your job is to move one bounded iOS task through scope, action, verification and handoff with traceable evidence.

## Framework Fusion

{table([
    ["framework", "what to use", "what not to over-import"],
    ["Superpowers", "planning, TDD, debugging, review, completion verification", "do not turn every small task into a heavy ceremony"],
    ["GSD2", "STATE/TASKS discipline, recovery, routing, model limits", "do not build a full runtime before v0.5"],
    ["Aider", "repo context, explicit editable files, read-only rules, Git hygiene", "do not use repo map as a substitute for tests"],
    ["gstack", "role ownership, review matrix, workflow gates, risk blocking", "do not run a multi-agent org for trivial changes"],
    ["SWE-agent", "ACI tools, action/observation, safe commands, trajectory", "do not claim runtime interception until implemented"],
])}

## Mandatory Task Flow

1. Read `STATE.md`, `TASKS.md`, `CONTEXT_INDEX.md`, `FILE_SCOPE_RULES.md`, and the task card.
2. Declare task type, owner role, allowed files, read-only files, forbidden files and verification commands.
3. Inspect before editing. Search before broad reading. Use line-bounded views for large files.
4. Before editing, run or mentally apply `scripts/agent/safe_edit_check.sh`.
5. After editing, run the smallest meaningful checks first, then broaden if risk requires it.
6. Record failures in `FAILURE_LOG.md`; do not loop silently.
7. Do not mark complete without fresh verification evidence.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "AGENTS.md"), 20)}
""",
    )

    write(
        GENERATED_ROOT / "PRODUCT_SPEC.md",
        f"""# PRODUCT SPEC

## Purpose

This harness coordinates coding agents working on an iOS app repo. It is optimized for bounded changes, traceable context, safe edits, verification evidence and release-risk control.

## Non-Goals

- It does not replace Xcode, Flutter, Firebase or App Store tooling.
- It does not grant autonomous release/upload authority.
- It does not make raw research files part of runtime context.

## v0.1 Scope

- Task cards with explicit file scope.
- Context index and context loading rules.
- Role/review/risk matrices.
- Verification matrix and failure log.
- Lightweight ACI tool contracts and optional scripts.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "PRODUCT_SPEC.md"), 12)}
""",
    )

    write_state_tasks_decisions(target_rows)
    write_context_files(target_rows)
    write_role_risk_files(target_rows)
    write_verification_files(target_rows)
    write_docs_and_templates(target_rows)
    write_scripts(source_count=len(source_cards), target_count=len(target_rows))


def write_state_tasks_decisions(target_rows: list[dict]) -> None:
    write(
        GENERATED_ROOT / "STATE.md",
        f"""# STATE

phase: ready_for_task_execution
current_task: none
current_role: none
last_updated: 2026-05-13

active_files:
  editable: []
  read_only: []
  forbidden: []

verification:
  required: []
  completed: []
  blocked: []

trajectory:
  enabled: manual
  output: data/trajectory.jsonl

blocked:
  - none

next:
  - create a task card in TASKS.md
  - build context pack from CONTEXT_INDEX.md
  - define allowed/read-only/forbidden files before editing

## Update Rules

- Update before changing task phase.
- Record owner role and verification commands.
- Record failures instead of retrying silently.
- Keep raw research files out of runtime context.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "STATE.md"), 18)}
""",
    )

    write(
        GENERATED_ROOT / "TASKS.md",
        f"""# TASKS

Use one task card per bounded change.

## Task Card Template

```yaml
task_id:
status: ready
task_type: flutter_ui | firebase_rules | swift_bridge | tests | bugfix | release | docs
owner_role:
risk_level: low | medium | high | release_blocking
goal:
allowed_files: []
read_only_files: []
forbidden_files: []
required_context: []
required_tools: []
verification_commands: []
completion_evidence: []
rollback_plan:
```

## v0.1 Rules

- No task starts without `allowed_files`, `read_only_files` and `forbidden_files`.
- Any high-risk file needs a review gate from `REVIEW_MATRIX.md`.
- Release, privacy, signing, Firebase rules and native bridge work require explicit risk review.
- Failed verification updates `FAILURE_LOG.md` before another attempt.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "TASKS.md"), 24)}
""",
    )

    write(
        GENERATED_ROOT / "DECISIONS.md",
        f"""# DECISIONS

## D-001: Clean assets are runtime authority

Decision: this harness reads clean Source Cards, summaries and mechanism indexes first. Raw research stays evidence-only.

Reason: raw folders contain duplicates, reports, converted documents and proposal artifacts.

## D-002: v0.1 is docs-first

Decision: v0.1 uses task cards, scope rules, review gates and verification matrices. Scripts are optional helpers; runtime interception is not claimed.

Reason: clean data has many v0.1 mechanisms and fewer v1.0 mechanisms.

## D-003: SWE-agent owns tool contracts, not global process

Decision: ACI tools and trajectory come from SWE-agent, but task discipline, file scope, roles and review gates come from the other frameworks.

Reason: cross-framework fusion avoids letting one framework dominate.

## D-004: Every source file must be consumed

Decision: every reviewed Source Card is mapped to at least one harness file in `data/source_to_harness_trace.jsonl`.

Reason: this prevents selective cherry-picking and makes the synthesis auditable.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "DECISIONS.md"), 18)}
""",
    )


def write_context_files(target_rows: list[dict]) -> None:
    write(
        GENERATED_ROOT / "CONTEXT_INDEX.md",
        f"""# CONTEXT INDEX

## Load Order

| tier | files | purpose |
|---|---|---|
| P0 | `STATE.md`, current task in `TASKS.md`, `FILE_SCOPE_RULES.md` | task state and edit boundary |
| P1 | `PRODUCT_SPEC.md`, `CONTEXT_RULES.md`, `ROLE_MATRIX.md`, `VERIFICATION_MATRIX.md` | normal task context |
| P2 | `docs/agent/REPO_CONTEXT.md`, platform convention files, relevant source cards | deeper context when needed |
| P3 | raw research files | avoid by default; use only if clean evidence is missing |

## Context Pack Rule

The context pack should list task id, task type, owner role, files loaded, reason loaded and token/risk estimate.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "CONTEXT_INDEX.md"), 24)}
""",
    )

    write(
        GENERATED_ROOT / "CONTEXT_RULES.md",
        f"""# CONTEXT RULES

## Default

Read less, but read the right files. Search before broad reading. View before edit.

## Required For Every Task

- `STATE.md`
- Current task card in `TASKS.md`
- `FILE_SCOPE_RULES.md`
- Relevant entries from `CONTEXT_INDEX.md`
- The files explicitly listed in `allowed_files` or `read_only_files`

## Forbidden By Default

- Raw research folders.
- Unrelated framework reports.
- Secrets, certificates, provisioning profiles and private env files.
- Entire large files when a line window is enough.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "CONTEXT_RULES.md"), 18)}
""",
    )

    write(
        GENERATED_ROOT / "FILE_SCOPE_RULES.md",
        f"""# FILE SCOPE RULES

## File Sets

| set | meaning | behavior |
|---|---|---|
| allowed_files | files the agent may edit | edit only after inspection |
| read_only_files | files the agent may read but not modify | context only |
| forbidden_files | files the agent may neither read broadly nor edit | require escalation |

## iOS Defaults

| task_type | editable examples | read-only examples | forbidden or high-risk examples |
|---|---|---|---|
| flutter_ui | `lib/**`, related tests | `pubspec.yaml`, design docs | signing, secrets, release metadata |
| firebase_rules | `firebase.rules`, tests | Firebase docs, schema docs | production credentials |
| swift_bridge | `ios/**`, platform channel files | Flutter caller files | entitlements without approval |
| tests | `test/**`, `integration_test/**` | source under test | production config |
| release | metadata/checklists only | build logs, privacy docs | upload/signing without manual approval |

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "FILE_SCOPE_RULES.md", "HIGH_RISK_FILES.md"), 18)}
""",
    )

    write(
        GENERATED_ROOT / "HIGH_RISK_FILES.md",
        """# HIGH RISK FILES

High-risk files require explicit review and, for release/signing/upload actions, manual approval.

| pattern | risk | default action |
|---|---|---|
| `**/*.p12`, `**/*.mobileprovision` | signing secrets | deny |
| `.env*`, `GoogleService-Info.plist`, `firebase_options.*` | credentials/config | ask |
| `ios/**/Entitlements.plist` | capabilities | ask |
| `ios/**/Info.plist` | privacy/release metadata | ask |
| `firebase.rules`, `firestore.rules`, `storage.rules` | backend access control | ask |
| release/upload scripts | external side effects | manual approval |
""",
    )


def write_role_risk_files(target_rows: list[dict]) -> None:
    write(
        GENERATED_ROOT / "ROLE_MATRIX.md",
        f"""# ROLE MATRIX

| role | owns | can approve | must escalate |
|---|---|---|---|
| orchestrator | task framing, scope, state | low-risk task plan | ambiguous or cross-domain tasks |
| flutter_ui | Flutter UI and widget tests | local UI changes | native bridge or release changes |
| firebase_backend | Firebase rules/functions/config | emulator-tested backend changes | production credentials |
| swift_interop | iOS native bridge, entitlements review | native code with tests | signing, privacy, release |
| mobile_qa | verification matrix and test evidence | test evidence sufficiency | missing device/simulator evidence |
| security_privacy | secrets, privacy, permissions | privacy/risk gate | external upload or credential access |
| app_store_release | release checklist and metadata | release readiness docs | upload/submission actions |

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "ROLE_MATRIX.md"), 18)}
""",
    )

    write(
        GENERATED_ROOT / "REVIEW_MATRIX.md",
        f"""# REVIEW MATRIX

| change_type | required review | blocking checks |
|---|---|---|
| docs-only | orchestrator | source trace and no unsupported claims |
| Flutter UI | flutter_ui + mobile_qa | analyze/test evidence |
| Firebase rules | firebase_backend + security_privacy | emulator/rules test evidence |
| Swift bridge | swift_interop + mobile_qa | build/test evidence |
| privacy/capabilities | security_privacy | privacy checklist |
| release | app_store_release + security_privacy + mobile_qa | release checklist and manual approval |

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "REVIEW_MATRIX.md"), 16)}
""",
    )

    write(
        GENERATED_ROOT / "RISK_CONTROL.md",
        f"""# RISK CONTROL

## Risk Levels

| level | examples | action |
|---|---|---|
| low | local docs, small UI copy, tests | proceed with task card |
| medium | code edits, refactors, dependency changes | require verification evidence |
| high | Firebase rules, native bridge, privacy metadata | require role review |
| release_blocking | signing, upload, App Store submission, production data | manual approval |

## Command Policy

- Allowed: read-only search, bounded file view, local tests, analyze commands.
- Ask first: dependency installs, networked commands, signing, release builds.
- Deny by default: credential reads, destructive file operations, production upload.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "RISK_CONTROL.md"), 24)}
""",
    )

    write(
        GENERATED_ROOT / "MODEL_ROUTING.md",
        f"""# MODEL ROUTING

| task/risk | weak model | strong model | human approval |
|---|---|---|---|
| docs cleanup | yes | optional | no |
| small UI/test task | yes, if file scope is tiny | optional | no |
| multi-file refactor | no | yes | maybe |
| Firebase/security/privacy | no | yes | for high-risk actions |
| release/signing/upload | no | yes for preparation only | required |

## Weak Model Rules

- Max 1-3 editable files.
- No high-risk files.
- Must use task template and explicit verification.
- Escalate on failed verification, scope growth or uncertainty.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "MODEL_ROUTING.md"), 18)}
""",
    )


def write_verification_files(target_rows: list[dict]) -> None:
    write(
        GENERATED_ROOT / "VERIFICATION_MATRIX.md",
        f"""# VERIFICATION MATRIX

| task_type | minimum checks | stronger checks |
|---|---|---|
| flutter_ui | `flutter analyze`, targeted widget/unit tests | golden/screenshot/manual simulator check |
| firebase_rules | emulator rules tests | staging dry-run |
| swift_bridge | iOS build or targeted native tests | simulator flow |
| bugfix | failing test reproduced then passing | regression test |
| release | checklist, privacy check, build evidence | TestFlight/release dry run with approval |
| docs-only | link/schema validation | reviewer pass |

## Completion Rule

Do not claim completion unless the final answer includes commands run, exit status and unresolved risk.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "VERIFICATION_MATRIX.md"), 24)}
""",
    )

    write(
        GENERATED_ROOT / "FAILURE_LOG.md",
        f"""# FAILURE LOG

Record failures here instead of retrying silently.

| time | task_id | command/action | failure_class | next_action | owner |
|---|---|---|---|---|---|

## Failure Classes

- context_pollution
- wrong_file_edit
- no_test_completion
- stuck_loop
- unsafe_command
- weak_model_overreach
- release_risk
- privacy_leak

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "FAILURE_LOG.md"), 18)}
""",
    )

    write(
        GENERATED_ROOT / "GIT_WORKFLOW.md",
        f"""# GIT WORKFLOW

## Rules

- Check dirty state before edits.
- Never overwrite user changes.
- Keep one task to one coherent diff.
- Commit only after verification evidence exists.
- PR/commit messages include scope, tests, risk and rollback.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "GIT_WORKFLOW.md", "GIT_ATOMIC_COMMIT.md"), 16)}
""",
    )

    write(
        GENERATED_ROOT / "IOS_RELEASE_CHECKLIST.md",
        f"""# IOS RELEASE CHECKLIST

Release work is high-risk. Preparation can be agent-assisted; submission/upload requires manual approval.

| area | check |
|---|---|
| build | clean release build evidence |
| tests | required tests passed |
| privacy | Info.plist, privacy manifest and permissions reviewed |
| Firebase | rules/config reviewed and tested |
| signing | certificates/profiles handled manually |
| App Store | metadata, screenshots, version, compliance reviewed |
| rollback | rollback or hotfix plan exists |

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "IOS_RELEASE_CHECKLIST.md"), 16)}
""",
    )


def write_docs_and_templates(target_rows: list[dict]) -> None:
    docs = {
        "docs/agent/ACI_TOOL_CONTRACTS.md": f"""# ACI TOOL CONTRACTS

Each tool must define input, output, failure modes, safety level and trajectory event.

| tool | purpose | risk | output |
|---|---|---|---|
| `view_file.sh` | bounded line-window file read | low | line-numbered content |
| `search_code.sh` | scoped text/path search | low | path:line matches |
| `safe_edit_check.sh` | pre-edit path/risk check | medium | allow/ask/deny |
| `run_safe_command.sh` | allowlisted verification commands | medium/high | command result |
| `context_pack.sh` | task context manifest | low | context list |

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "docs/agent/ACI_TOOL_CONTRACTS.md", "scripts/agent/view_file.sh", "scripts/agent/search_code.sh", "scripts/agent/safe_edit_check.sh", "scripts/agent/run_safe_command.sh", "scripts/agent/context_pack.sh"), 24)}
""",
        "docs/agent/REPO_CONTEXT.md": f"""# REPO CONTEXT

Use repo context as a relevance map, not as proof of correctness.

## Rules

- Search first with `rg`.
- Load only task-relevant files.
- Keep conventions and architecture read-only unless the task explicitly changes them.
- Treat dependency and generated files as high-risk unless scoped.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "docs/agent/REPO_CONTEXT.md", "docs/agent/REPO_MAP.md"), 14)}
""",
        "docs/agent/EDIT_FORMATS.md": f"""# EDIT FORMATS

Prefer minimal, line-oriented edits after viewing the target region.

## Rules

- Never edit a file that is not in `allowed_files`.
- Never edit high-risk files without review.
- Avoid broad rewrites unless the task is explicitly a refactor.
- Record before/after intent in task evidence.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "docs/agent/EDIT_FORMATS.md"), 14)}
""",
        "docs/agent/WORKFLOW_CHAIN.md": f"""# WORKFLOW CHAIN

| workflow | phases |
|---|---|
| feature | task card -> context pack -> edit -> tests -> review -> state update |
| bugfix | reproduce -> isolate -> fix -> regression test -> failure log update |
| Firebase | scope -> local/emulator validation -> security review -> evidence |
| Swift interop | scope -> native edit -> build/test -> QA review |
| release | checklist -> risk review -> manual approval -> handoff |

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "docs/agent/WORKFLOW_CHAIN.md"), 14)}
""",
        "docs/agent/TESTING_GUIDE.md": f"""# TESTING GUIDE

Start with the smallest meaningful test and broaden based on risk.

## Required Evidence

- command
- exit code
- relevant output summary
- remaining gaps

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "docs/agent/TESTING_GUIDE.md"), 14)}
""",
        "docs/agent/DEBUG_GUIDE.md": f"""# DEBUG GUIDE

1. Reproduce or state why reproduction is impossible.
2. Gather evidence before proposing a fix.
3. Change one cause at a time.
4. Rerun the failing check.
5. Record stuck loops in `FAILURE_LOG.md`.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "docs/agent/DEBUG_GUIDE.md"), 12)}
""",
        "docs/agent/RISK_GATE.md": f"""# RISK GATE

Risk gates block unsafe actions before they become code changes or external side effects.

Use `RISK_CONTROL.md`, `HIGH_RISK_FILES.md`, `REVIEW_MATRIX.md` and `IOS_RELEASE_CHECKLIST.md` together.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "docs/agent/RISK_GATE.md"), 14)}
""",
        "docs/agent/SWE_CONCEPTS.md": f"""# SWE CONCEPTS

The useful SWE-agent transfer is the action/observation discipline:

- task becomes tool actions
- each action returns observation
- observations update state
- verification determines completion
- trajectory allows replay/debugging later

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "docs/agent/SWE_CONCEPTS.md"), 10)}
""",
        "docs/agent/MINI_SWE_LOOP.md": f"""# MINI SWE LOOP

v0.5 prototype loop:

1. observe task/state
2. choose one allowed tool
3. act
4. capture observation
5. verify or continue
6. terminate, fail or escalate

This is a prototype loop, not full release automation.

## Evidence Pull

{evidence_section(rows_for_file(target_rows, "docs/agent/MINI_SWE_LOOP.md"), 10)}
""",
    }
    for rel_path, content in docs.items():
        write(GENERATED_ROOT / rel_path, content)

    write(
        GENERATED_ROOT / "templates" / "task_card.md",
        """# Task Card: <task_id>

| Field | Value |
|---|---|
| status | ready |
| owner_role | |
| task_type | |
| risk_level | |
| goal | |
| allowed_files | |
| read_only_files | |
| forbidden_files | |
| required_context | |
| required_tools | |
| verification_commands | |
| rollback_plan | |

## Work Log

| step | evidence |
|---|---|

## Completion Evidence

| command/check | result | notes |
|---|---|---|
""",
    )
    write(
        GENERATED_ROOT / "templates" / "review_template.md",
        """# Review: <task_id>

## Findings

| severity | file | issue | recommendation |
|---|---|---|---|

## Gate Check

| gate | pass/fail | evidence |
|---|---|---|

## Decision

approved / changes_requested / blocked
""",
    )
    write(
        GENERATED_ROOT / "templates" / "manual_approval.md",
        """# Manual Approval

| Field | Value |
|---|---|
| task_id | |
| requested_action | |
| risk_level | |
| reason | |
| approver | |
| approved_at | |
| constraints | |
""",
    )
    write(
        GENERATED_ROOT / "templates" / "pr_description.md",
        """# PR Description

## Scope

## Verification

## Risk

## Rollback

## Source Trace
""",
    )


def write_scripts(source_count: int, target_count: int) -> None:
    write(
        GENERATED_ROOT / "scripts" / "agent" / "view_file.sh",
        """#!/usr/bin/env bash
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

awk -v start="$start" -v count="$count" 'NR >= start && NR < start + count { printf "%6d  %s\\n", NR, $0 }' "$file"
""",
        executable=True,
    )
    write(
        GENERATED_ROOT / "scripts" / "agent" / "search_code.sh",
        """#!/usr/bin/env bash
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
""",
        executable=True,
    )
    write(
        GENERATED_ROOT / "scripts" / "agent" / "safe_edit_check.sh",
        """#!/usr/bin/env bash
set -euo pipefail

target="${1:-}"
if [[ -z "$target" ]]; then
  echo "usage: safe_edit_check.sh <target_file>" >&2
  exit 2
fi

case "$target" in
  raw/*|*/raw/*|*.p12|*.mobileprovision|*.cer|*.key|*.pem|*.env|*/.env*)
    echo "deny: high-risk or raw file: $target" >&2
    exit 3
    ;;
esac

case "$target" in
  *GoogleService-Info.plist|*firebase_options.*|*Entitlements.plist|*Info.plist|*firestore.rules|*storage.rules|*firebase.rules)
    echo "ask: high-risk iOS/Firebase file requires review: $target"
    exit 10
    ;;
esac

echo "allow: $target"
""",
        executable=True,
    )
    write(
        GENERATED_ROOT / "scripts" / "agent" / "run_safe_command.sh",
        """#!/usr/bin/env bash
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
    case "${1:-}" in -list|-showBuildSettings|test|build) exec xcodebuild "$@" ;; esac
    ;;
  swift)
    case "${1:-}" in test|build) exec swift "$@" ;; esac
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
""",
        executable=True,
    )
    write(
        GENERATED_ROOT / "scripts" / "agent" / "context_pack.sh",
        """#!/usr/bin/env bash
set -euo pipefail

task_file="${1:-TASKS.md}"

printf 'context_pack_generated_at: %s\\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
printf 'task_file: %s\\n' "$task_file"
printf 'required:\\n'
printf '  - STATE.md\\n'
printf '  - TASKS.md\\n'
printf '  - CONTEXT_INDEX.md\\n'
printf '  - FILE_SCOPE_RULES.md\\n'
printf '  - VERIFICATION_MATRIX.md\\n'
""",
        executable=True,
    )
    write(
        GENERATED_ROOT / "scripts" / "validate_harness.py",
        f"""#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {REQUIRED_HARNESS_FILES!r}


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {{rel}}")

    traces = read_jsonl(ROOT / "data" / "source_to_harness_trace.jsonl")
    targets = read_jsonl(ROOT / "data" / "mechanism_targets.jsonl")

    if len(traces) != {source_count}:
        errors.append(f"expected {source_count} source traces, got {{len(traces)}}")
    if len(targets) != {target_count}:
        errors.append(f"expected {target_count} mechanism target rows, got {{len(targets)}}")

    uncovered = [row["source_id"] for row in traces if not row.get("harness_files")]
    if uncovered:
        errors.append("uncovered source cards: " + ", ".join(uncovered[:20]))

    for rel in ("README.md", "AGENTS.md", "TASKS.md", "VERIFICATION_MATRIX.md", "RISK_CONTROL.md"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        if "Evidence Pull" not in text:
            errors.append(f"missing Evidence Pull section: {{rel}}")

    for error in errors:
        print(error)
    print(f"validated ios_app_harness, failures: {{len(errors)}}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
""",
        executable=True,
    )


def write_framework_summaries(source_cards: list[dict], mechanisms: list[dict], target_rows: list[dict]) -> None:
    FRAMEWORKS_ROOT.mkdir(parents=True, exist_ok=True)
    by_framework_cards = defaultdict(list)
    by_framework_mechanisms = defaultdict(list)
    by_framework_targets = defaultdict(list)
    for card in source_cards:
        by_framework_cards[card["framework"]].append(card)
    for mechanism in mechanisms:
        by_framework_mechanisms[mechanism["source_framework"]].append(mechanism)
    for row in target_rows:
        by_framework_targets[row["source_framework"]].append(row)

    for framework in FRAMEWORK_ORDER:
        cards = sorted(by_framework_cards[framework], key=lambda row: row["source_id"])
        fw_mechanisms = by_framework_mechanisms[framework]
        fw_targets = by_framework_targets[framework]
        layer_counts = Counter(row["target_layer"] for row in fw_targets)
        target_counts = Counter(row["harness_file"] for row in fw_targets)
        mode_counts = Counter(mode for mech in fw_mechanisms for mode in mech.get("failure_modes", []))
        conflict = {
            "superpowers": "output/conflicts/superpowers_conflicts.md",
            "gsd2": "output/conflicts/gsd2_conflicts.md",
            "aider": "output/conflicts/aider_conflicts.md",
            "gstack": "output/conflicts/gstack_conflicts.md",
            "swe-agent": "output/conflicts/swe_agent_conflicts.md",
        }[framework]
        write(
            FRAMEWORKS_ROOT / FRAMEWORK_SUMMARY_NAMES[framework],
            f"""# Framework Summary: {framework}

## 1. One-line Essence

{framework} 的可迁移价值是：{FRAMEWORK_CORE[framework]}

## 2. Source Coverage

{table([["source_id", "status", "source_card"], *[[card["source_id"], card["status"], card["source_card"]] for card in cards]])}

## 3. Core Mechanism Targets

{table([["layer", "count"], *[[layer, str(layer_counts[layer])] for layer in sorted(layer_counts)]])}

## 4. Highest-Impact Harness Files

{table([["harness_file", "mechanism_targets"], *[[path, str(count)] for path, count in target_counts.most_common(15)]])}

## 5. Failure Modes Addressed

{table([["failure_mode", "mechanism_count"], *[[mode, str(count)] for mode, count in mode_counts.most_common(15)]])}

## 6. Transferable Parts

{evidence_section(fw_targets, 24)}

## 7. Non-transferable Parts

- Runtime interception is not transferred unless a tested script/runtime exists.
- Duplicate reports are not copied wholesale; section-level Source Cards have priority.
- Raw files remain evidence, not default context.

## 8. Conflicts

See `{conflict}`.

## 9. Final Judgment

Use this framework as one layer in the fused iOS Harness. Do not let it override stronger evidence from another layer.
""",
        )


def write_mechanism_and_failure_docs(mechanisms: list[dict], target_rows: list[dict]) -> None:
    MECHANISMS_ROOT.mkdir(parents=True, exist_ok=True)
    FAILURE_MODES_ROOT.mkdir(parents=True, exist_ok=True)
    mechanism_specs = {
        "skills_and_process.md": ["AGENTS.md", "docs/agent/TASKS.md", "QUALITY_GATE.md"],
        "task_state_machine.md": ["STATE.md", "TASKS.md", "FAILURE_LOG.md"],
        "agent_roles.md": ["ROLE_MATRIX.md", "REVIEW_MATRIX.md", "MODEL_ROUTING.md"],
        "repo_context.md": ["CONTEXT_INDEX.md", "CONTEXT_RULES.md", "FILE_SCOPE_RULES.md", "docs/agent/REPO_CONTEXT.md"],
        "aci_tools.md": ["docs/agent/ACI_TOOL_CONTRACTS.md", "scripts/agent/view_file.sh", "scripts/agent/search_code.sh", "scripts/agent/safe_edit_check.sh", "scripts/agent/run_safe_command.sh"],
        "verification.md": ["VERIFICATION_MATRIX.md", "docs/agent/TESTING_GUIDE.md", "IOS_RELEASE_CHECKLIST.md"],
        "risk_gate.md": ["RISK_CONTROL.md", "HIGH_RISK_FILES.md", "docs/agent/RISK_GATE.md", "IOS_RELEASE_CHECKLIST.md"],
    }
    for name, files in mechanism_specs.items():
        rows = rows_for_file(target_rows, *files)
        write(
            MECHANISMS_ROOT / name,
            f"""# Mechanism: {name.removesuffix('.md').replace('_', ' ').title()}

## Essence

This mechanism group is synthesized from reviewed Source Cards and materialized into the lightweight iOS Harness.

## Target Files

{table([["harness_file", "mechanism_targets"], *[[path, str(count)] for path, count in Counter(row["harness_file"] for row in rows).most_common()]])}

## Source Framework Contributions

{table([["framework", "mechanism_targets"], *[[framework, str(count)] for framework, count in Counter(row["source_framework"] for row in rows).most_common()]])}

## Evidence Pull

{evidence_section(rows, 32)}
""",
        )

    failure_to_mechanisms = defaultdict(list)
    for mechanism in mechanisms:
        for mode in mechanism.get("failure_modes", []):
            failure_to_mechanisms[mode].append(mechanism)
    for mode, rows in sorted(failure_to_mechanisms.items(), key=lambda item: (-len(item[1]), item[0]))[:25]:
        target_counter = Counter(
            harness_file_for(target["target_layer"], target["target_file"])
            for mechanism in rows
            for target in mechanism.get("ios_harness_targets", [])
        )
        write(
            FAILURE_MODES_ROOT / f"{slug(mode)}.md",
            f"""# Failure Mode: {mode}

## Why It Matters

This failure mode appears in {len(rows)} mechanism records and must be explicitly guarded in the iOS Harness.

## Primary Guard Files

{table([["harness_file", "mechanism_count"], *[[path, str(count)] for path, count in target_counter.most_common(12)]])}

## Source Evidence

{table([["mechanism", "framework", "source", "summary"], *[[m["id"], m["source_framework"], m["source_file_id"], m["name"]] for m in rows[:24]]])}
""",
        )


def write_mapping_outputs(target_rows: list[dict], source_cards: list[dict]) -> None:
    MAPPING_ROOT.mkdir(parents=True, exist_ok=True)
    file_counts = Counter(row["harness_file"] for row in target_rows)
    layer_counts = Counter(row["target_layer"] for row in target_rows)
    version_counts = Counter(row["version"] for row in target_rows)
    source_rows = defaultdict(list)
    for row in target_rows:
        source_rows[row["source_file_id"]].append(row)

    write(
        MAPPING_ROOT / "file_placement_map.md",
        f"""# iOS Harness File Placement Map

Generated from reviewed clean mechanisms.

{table([["harness_file", "mechanism_targets"], *[[path, str(count)] for path, count in file_counts.most_common()]])}
""",
    )
    for version, filename in [("v0_1", "v0_1_scope.md"), ("v0_5", "v0_5_scope.md"), ("v1_0", "v1_0_scope.md")]:
        rows = [row for row in target_rows if row["version"] == version]
        write(
            MAPPING_ROOT / filename,
            f"""# iOS Harness {version} Scope

## Summary

{version} contains {len(rows)} mechanism target rows.

## Target Files

{table([["harness_file", "mechanism_targets"], *[[path, str(count)] for path, count in Counter(row["harness_file"] for row in rows).most_common()]])}

## Evidence Pull

{evidence_section(rows, 40)}
""",
        )
    write(
        MAPPING_ROOT / "coverage_matrix.md",
        f"""# Coverage Matrix

## By Framework

{table([["framework", "source_cards", "mechanism_targets"], *[[framework, str(sum(1 for s in source_cards if s["framework"] == framework)), str(sum(1 for r in target_rows if r["source_framework"] == framework))] for framework in FRAMEWORK_ORDER]])}

## By Layer

{table([["layer", "mechanism_targets"], *[[layer, str(layer_counts[layer])] for layer in sorted(layer_counts)]])}

## By Version

{table([["version", "mechanism_targets"], *[[version, str(version_counts[version])] for version in sorted(version_counts)]])}
""",
    )
    write(
        MAPPING_ROOT / "source_to_harness_trace.md",
        f"""# Source To Harness Trace

Every reviewed Source Card has at least one harness target.

{table([["source_id", "framework", "mechanisms", "primary_harness_file", "source_card"], *[[source["source_id"], source["framework"], str(len({row["mechanism_id"] for row in source_rows[source["source_id"]]})), sorted({row["harness_file"] for row in source_rows[source["source_id"]]})[0], source["source_card"]] for source in sorted(source_cards, key=lambda row: row["source_id"])]])}
""",
    )
    write(
        MAPPING_ROOT / "codex_handoff.md",
        f"""# Codex Handoff: Lightweight iOS App Harness

## Start Here

Read `generated/ios_app_harness/README.md`, then `AGENTS.md`, `TASKS.md`, `CONTEXT_INDEX.md`, `FILE_SCOPE_RULES.md`, `VERIFICATION_MATRIX.md`, and `RISK_CONTROL.md`.

## What Exists

- Lightweight docs-first iOS Harness in `generated/ios_app_harness/`.
- Machine-readable source trace in `generated/ios_app_harness/data/source_to_harness_trace.jsonl`.
- Mechanism target index in `generated/ios_app_harness/data/mechanism_targets.jsonl`.
- Framework summaries in `output/frameworks/`.
- Mechanism groups in `output/mechanisms/`.
- Failure mode docs in `output/failure_modes/`.

## What Not To Claim

- Do not claim runtime interception exists.
- Do not claim App Store upload automation exists.
- Do not read raw research files by default.

## Validation

Run:

```bash
python3 generated/ios_app_harness/scripts/validate_harness.py
python3 scripts/validate_source_cards.py
python3 scripts/validate_yaml.py
python3 scripts/validate_clean_data.py
python3 -m unittest discover tests
```
""",
    )


def main() -> int:
    source_cards = read_jsonl(HARNESS_ROOT / "output" / "data" / "source_cards.jsonl")
    mechanisms = read_jsonl(HARNESS_ROOT / "output" / "data" / "mechanisms.jsonl")
    target_rows = mechanism_target_rows(mechanisms)

    write_data_files(target_rows, source_cards)
    write_core_harness(target_rows, source_cards)
    write_framework_summaries(source_cards, mechanisms, target_rows)
    write_mechanism_and_failure_docs(mechanisms, target_rows)
    write_mapping_outputs(target_rows, source_cards)

    print(f"wrote lightweight iOS harness to {GENERATED_ROOT}")
    print(f"source traces: {len(source_cards)}")
    print(f"mechanism target rows: {len(target_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

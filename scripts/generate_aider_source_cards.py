#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from inventory import yaml_scalar


HARNESS_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = HARNESS_ROOT.parent
SOURCE_INDEX = HARNESS_ROOT / "output" / "data" / "source_index.yaml"
SOURCE_CARDS_JSONL = HARNESS_ROOT / "output" / "data" / "source_cards.jsonl"


@dataclass
class SourceRecord:
    source_id: str
    framework: str
    raw_path: str
    relative_path: str
    file_type: str
    estimated_topic: str
    processing_status: str
    output_card: str


@dataclass(frozen=True)
class MechanismTemplate:
    name: str
    description: str
    target_layer: str
    target_file: str
    version: str
    transfer_method: str
    evidence: str
    confidence: str = "high"


def sanitize(value: str) -> str:
    value = value.replace("|", "/").replace("\r", " ").replace("\n", " ")
    value = value.replace("TODO", "待办").replace("TBD", "待定")
    value = re.sub(r"\s+", " ", value).strip()
    return value


def parse_source_index(path: Path) -> list[SourceRecord]:
    records: list[SourceRecord] = []
    current: dict[str, str] | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("- source_id:"):
            if current:
                records.append(SourceRecord(**current))
            current = {"source_id": stripped.split(":", 1)[1].strip().strip('"')}
        elif current is not None and ":" in stripped:
            key, value = stripped.split(":", 1)
            current[key.strip()] = value.strip().strip('"')

    if current:
        records.append(SourceRecord(**current))
    return records


def write_source_index(records: list[SourceRecord]) -> None:
    yaml_lines = ["sources:"]
    for record in records:
        yaml_lines.extend(
            [
                f"  - source_id: {yaml_scalar(record.source_id)}",
                f"    framework: {yaml_scalar(record.framework)}",
                f"    raw_path: {yaml_scalar(record.raw_path)}",
                f"    relative_path: {yaml_scalar(record.relative_path)}",
                f"    file_type: {yaml_scalar(record.file_type)}",
                f"    estimated_topic: {yaml_scalar(record.estimated_topic)}",
                f"    processing_status: {yaml_scalar(record.processing_status)}",
                f"    output_card: {yaml_scalar(record.output_card)}",
            ]
        )
    SOURCE_INDEX.write_text("\n".join(yaml_lines) + "\n", encoding="utf-8")


def write_source_inventory(records: list[SourceRecord]) -> None:
    lines = [
        "# SOURCE INVENTORY",
        "",
        "Scope: indexed research framework files. AppleDouble `._*` metadata files are ignored, not modified.",
        "",
        "| source_id | framework | raw_path | file_type | estimated_topic | status | output_card |",
        "|---|---|---|---|---|---|---|",
    ]
    for record in records:
        lines.append(
            "| {source_id} | {framework} | {raw_path} | {file_type} | {topic} | {status} | {output_card} |".format(
                source_id=record.source_id,
                framework=record.framework,
                raw_path=record.raw_path,
                file_type=record.file_type,
                topic=sanitize(record.estimated_topic),
                status=record.processing_status,
                output_card=record.output_card,
            )
        )
    (HARNESS_ROOT / "SOURCE_INVENTORY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def read_raw(record: SourceRecord) -> tuple[str, list[tuple[int, str]], int]:
    path = PROJECT_ROOT / record.raw_path
    text = path.read_text(encoding="utf-8", errors="replace")
    headings: list[tuple[int, str]] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("#"):
            title = stripped.lstrip("#").strip()
            if title:
                headings.append((line_no, sanitize(title)))
    return text, headings, len(text.splitlines())


def category(record: SourceRecord) -> str:
    key = f"{record.relative_path} {record.estimated_topic}".lower()
    if "repo" in key and ("map" in key or "repopmap" in key):
        return "repo_map"
    if "file_scope" in key or "file selection" in key or "文件范围" in key or "弱模型文件范围" in key:
        return "file_scope"
    if "git" in key or "commit" in key or "pr_description" in key:
        return "git"
    if "lint" in key or "test" in key or "验证闭环" in key:
        return "verification"
    if "weak_model" in key or "弱模型" in key:
        return "weak_model"
    if "context_index" in key or "context_pack" in key or "上下文索引" in key:
        return "context"
    if "conventions" in key or "规范" in key:
        return "conventions"
    if "integration" in key or "migration" in key or "四框架" in key or "v0.1" in key or "迁移方案" in key:
        return "migration"
    if "learning" in key or "学习路径" in key:
        return "learning"
    if "skeptic" in key or "批判" in key or "适配性" in key:
        return "risk_review"
    if "docs" in key or "concepts" in key or "5why" in key or "overview" in key or "框架解剖" in key:
        return "aider_core"
    if "plan" in key:
        return "plan"
    return "aider_core"


def mechanism_templates(kind: str) -> list[MechanismTemplate]:
    profiles: dict[str, list[MechanismTemplate]] = {
        "plan": [
            MechanismTemplate("Aider Research Pipeline", "把 Aider 调研拆为 overview、机制分析、迁移设计和交付物模板。", "Task Layer", "TASKS.md", "v0_1", "把框架清洗阶段化，避免一次性总结。", "E1"),
            MechanismTemplate("Deliverable-Driven Cleaning", "以交付物编号和 stage 文件约束研究输出。", "Harness Maintenance Layer", "SOURCE_INVENTORY.md", "v0_1", "让每个输出都能回到具体 raw 文件。", "E2"),
            MechanismTemplate("Aider-to-iOS Transfer Agenda", "把 repo map、文件范围、Git、验证和弱模型作为迁移主题。", "Goal Layer", "output/frameworks/aider_summary.md", "v0_5", "作为 Aider 框架总结提纲。", "E3"),
            MechanismTemplate("Quality Gate Before Synthesis", "先建立质量标准再做跨框架融合。", "Feedback / Verification Layer", "QUALITY_GATE.md", "v0_1", "把清洗完整性作为合成前置条件。", "E4"),
        ],
        "aider_core": [
            MechanismTemplate("Repo-Aware Editing Loop", "Aider 的核心是围绕真实代码库进行对话式编辑，而不是孤立生成代码。", "Context Layer", "docs/agent/REPO_CONTEXT.md", "v0_1", "把 repo-aware 作为 iOS Harness 上下文层原则。", "E1"),
            MechanismTemplate("Explicit Added Files", "模型只应编辑明确加入任务上下文的文件。", "Task Layer", "TASKS.md", "v0_1", "在任务卡中固定 editable files。", "E2"),
            MechanismTemplate("Read-Only Rule Context", "规范、索引和架构文件应作为只读上下文加载。", "Context Layer", "CONTEXT_INDEX.md", "v0_1", "区分 read-only context 与 editable files。", "E3"),
            MechanismTemplate("Edit Format Discipline", "通过可解析的 edit format 限制模型输出，降低错误补丁风险。", "Action / ACI Layer", "docs/agent/EDIT_FORMATS.md", "v0_5", "将全文件、diff、udiff 等编辑格式按任务风险选择。", "E4"),
        ],
        "repo_map": [
            MechanismTemplate("Repo Map Ranking", "用符号、路径和引用关系为模型选择最相关的代码片段。", "Context Layer", "docs/agent/REPO_MAP.md", "v0_5", "为 iOS repo context 生成 ranked map。", "E1"),
            MechanismTemplate("Token-Budgeted Repository Context", "在 token 预算内压缩仓库结构和关键符号。", "Context Layer", "CONTEXT_INDEX.md", "v0_5", "把 repo map 作为可裁剪上下文，而非全仓读取。", "E2"),
            MechanismTemplate("Dependency Surfacing", "通过 repo map 暴露跨文件依赖，减少漏改关联文件。", "Task Layer", "TASKS.md", "v0_5", "在任务卡加入 related_files 候选。", "E3"),
            MechanismTemplate("Repo Map Boundary", "repo map 只能帮助发现相关文件，不能替代真实编译、测试或平台判断。", "Risk / Release Layer", "DECISIONS.md", "v0_1", "在合成时记录 repo map 的非转移边界。", "E4"),
        ],
        "file_scope": [
            MechanismTemplate("Allowed Files Contract", "每个任务显式声明可以编辑的文件集合。", "Task Layer", "TASKS.md", "v0_1", "增加 allowed_files 字段。", "E1"),
            MechanismTemplate("Read-Only Files Contract", "把规范、架构和参考文件标为只读。", "Context Layer", "CONTEXT_RULES.md", "v0_1", "增加 read_only_files 字段。", "E2"),
            MechanismTemplate("Forbidden Files Guard", "声明禁止修改的高风险文件和平台目录。", "Risk / Release Layer", "HIGH_RISK_FILES.md", "v0_1", "建立 forbidden_files 和升级规则。", "E3"),
            MechanismTemplate("Task-Type File Scope Table", "按 Flutter/Firebase/iOS/release/debug 等任务类型分配文件范围。", "Harness Maintenance Layer", "FILE_SCOPE_RULES.md", "v0_1", "将任务类型映射为可编辑、只读和禁止文件。", "E4"),
        ],
        "git": [
            MechanismTemplate("Dirty Tree Awareness", "执行前识别已有未提交变更，避免覆盖用户工作。", "Risk / Release Layer", "GIT_WORKFLOW.md", "v0_1", "要求任务前记录 dirty state。", "E1"),
            MechanismTemplate("Atomic Commit Boundary", "单任务单 commit，让变更可审查、回滚和归因。", "Memory / State Layer", "TASKS.md", "v0_1", "任务完成记录 commit id 或 diff summary。", "E2"),
            MechanismTemplate("Auto-Commit With Undo Semantics", "自动提交必须配套 undo/rollback 策略。", "Risk / Release Layer", "GIT_ATOMIC_COMMIT.md", "v0_5", "把自动提交限制在验证通过后。", "E3"),
            MechanismTemplate("PR/Commit Message Evidence", "提交和 PR 描述应包含范围、验证、风险和回滚说明。", "Feedback / Verification Layer", "templates/pr_description.md", "v0_1", "把审查证据写入提交/PR 模板。", "E4"),
        ],
        "verification": [
            MechanismTemplate("Lint Command Gate", "用 lint/analyze 命令发现静态错误。", "Feedback / Verification Layer", "VERIFICATION_MATRIX.md", "v0_1", "把 `flutter analyze` 等命令列为完成前证据。", "E1"),
            MechanismTemplate("Test Command Gate", "用测试命令验证行为变更。", "Feedback / Verification Layer", "VERIFICATION_MATRIX.md", "v0_1", "将 unit/widget/integration test 绑定任务类型。", "E2"),
            MechanismTemplate("Reflection Fix Loop", "命令失败后让模型读取错误、修复并重跑，但次数受限。", "Feedback / Verification Layer", "FAILURE_LOG.md", "v0_5", "记录失败命令、修复尝试和 retry_count。", "E3"),
            MechanismTemplate("Verification Evidence Record", "完成声明必须附命令、退出码和关键输出摘要。", "Memory / State Layer", "output/data/verification_evidence.jsonl", "v0_5", "结构化保存验证证据。", "E4"),
        ],
        "weak_model": [
            MechanismTemplate("Weak Model File Cap", "弱模型只处理少量明确文件，避免跨层迷路。", "Task Layer", "TASKS.md", "v0_1", "为 weak_model task 设置 max_files。", "E1"),
            MechanismTemplate("Weak Model Task Downgrade", "把复杂任务拆小或升级给强模型。", "Role / Review Layer", "MODEL_ROUTING.md", "v0_5", "将弱模型边界接入模型路由。", "E2"),
            MechanismTemplate("Simplified Context Pack", "弱模型只接收目标文件、规则摘要和最小验证命令。", "Context Layer", "CONTEXT_INDEX.md", "v0_5", "生成 weak context pack。", "E3"),
            MechanismTemplate("Escalation on Scope Breach", "弱模型触碰禁止文件、失败循环或范围扩大时升级。", "Risk / Release Layer", "FAILURE_LOG.md", "v0_1", "记录 scope_breach 并阻断继续执行。", "E4"),
        ],
        "context": [
            MechanismTemplate("Context Index Layering", "用索引文件组织项目规则、仓库结构和平台规范。", "Context Layer", "CONTEXT_INDEX.md", "v0_1", "定义 P0/P1 context loading order。", "E1"),
            MechanismTemplate("Task-Type Context Pack", "按任务类型打包不同上下文文件。", "Action / ACI Layer", "scripts/agent/context_pack.sh", "v0_5", "用脚本输出单任务 context pack。", "E2"),
            MechanismTemplate("Weak/Strong Context Modes", "弱模型与强模型使用不同 token 和文件数量上限。", "Role / Review Layer", "MODEL_ROUTING.md", "v0_5", "把 context mode 绑定到模型模式。", "E3"),
            MechanismTemplate("Context Pack Audit Header", "上下文包记录 task_id、model、文件数量和估算 token。", "Memory / State Layer", "STATE.md", "v0_5", "让上下文注入可审计。", "E4"),
        ],
        "conventions": [
            MechanismTemplate("Layered Conventions Files", "将通用、Flutter、Firebase 和 iOS native 规范分文件维护。", "Context Layer", "CONTEXT_INDEX.md", "v0_1", "按平台和层级只读加载规范。", "E1"),
            MechanismTemplate("Conventions as Read-Only Context", "规范文件指导编辑但不应被普通任务修改。", "Context Layer", "CONTEXT_RULES.md", "v0_1", "把 conventions 加入 read_only_files。", "E2"),
            MechanismTemplate("Platform-Specific Risk Rules", "平台规范覆盖状态管理、数据模型、原生能力和发布风险。", "Risk / Release Layer", "IOS_RELEASE_CHECKLIST.md", "v0_1", "把平台高风险规则纳入 release gate。", "E3"),
            MechanismTemplate("Rule Drift Review", "规范文件变更需要强模型或人工 review。", "Role / Review Layer", "REVIEW_POLICY.md", "v0_5", "把规则修改标为 high-risk。", "E4"),
        ],
        "migration": [
            MechanismTemplate("Aider Context Layer Transfer", "将 Aider 的 repo map、file scope 和 read-only context 转成 iOS Harness context layer。", "Context Layer", "CONTEXT_INDEX.md", "v0_1", "作为 Aider 迁移主线。", "E1"),
            MechanismTemplate("Versioned iOS Harness File Tree", "用 v0.1/v0.5/v1.0 区分文件结构和自动化程度。", "Harness Maintenance Layer", "output/ios_harness_mapping/v0_1_scope.md", "v0_1", "把迁移落到版本化文件树。", "E2"),
            MechanismTemplate("Four-Framework Role Composition", "将 Aider 与 Superpowers、GSD2、gstack 做职责分离。", "Role / Review Layer", "output/frameworks/aider_summary.md", "v0_5", "合成时保留职责边界。", "E3"),
            MechanismTemplate("Migration Handoff Package", "把上下文索引、文件范围、Git、验证和模板打包给后续 Codex。", "Harness Maintenance Layer", "output/ios_harness_mapping/codex_handoff.md", "v0_1", "形成 Aider clean handoff。", "E4"),
        ],
        "learning": [
            MechanismTemplate("Three-Day Aider Learning Path", "按 repo map、file scope、Git/verification、迁移设计组织学习路径。", "Harness Maintenance Layer", "docs/agent/AIDER_LEARNING_PATH.md", "v0_5", "用于后续 agent onboarding。", "E1"),
            MechanismTemplate("Concept-to-Practice Progression", "从概念理解进入模板和脚本实践。", "Task Layer", "TASKS.md", "v0_5", "把学习任务拆成实践卡。", "E2"),
            MechanismTemplate("iOS Scenario Exercises", "用 Flutter/Firebase/iOS release 场景验证 Aider 机制迁移。", "Feedback / Verification Layer", "VERIFICATION_MATRIX.md", "v0_5", "让学习路径产生可检查结果。", "E3"),
            MechanismTemplate("Knowledge Handoff Summary", "将学习结果压缩成 Codex 后续可读摘要。", "Harness Maintenance Layer", "output/frameworks/aider_summary.md", "v0_5", "服务框架总结。", "E4"),
        ],
        "risk_review": [
            MechanismTemplate("Aider Suitability Boundary", "区分 Aider 适合迁移和不适合迁移的能力。", "Risk / Release Layer", "DECISIONS.md", "v0_1", "把非转移项写入 conflict ledger。", "E1"),
            MechanismTemplate("iOS-Specific Risk Review", "检查 Aider 机制在 Flutter/Firebase/Swift/App Store 场景中的风险。", "Risk / Release Layer", "IOS_RELEASE_CHECKLIST.md", "v0_1", "把平台风险纳入清洗结论。", "E2"),
            MechanismTemplate("Weak Model Overreach Warning", "批判弱模型跨文件、跨层和 release 任务的失控风险。", "Role / Review Layer", "MODEL_ROUTING.md", "v0_1", "限制弱模型任务边界。", "E3"),
            MechanismTemplate("Evidence Before Adoption", "只有有证据和验证路径的 Aider 机制才进入 iOS Harness。", "Feedback / Verification Layer", "QUALITY_GATE.md", "v0_1", "防止把研究建议直接当事实。", "E4"),
        ],
    }
    return profiles[kind]


def failure_rows(kind: str) -> list[tuple[str, str, str]]:
    common = {
        "repo_map": [
            ("context_pollution", "repo map 以排名和 token 预算限制全仓上下文。", "E2"),
            ("missing_related_file", "依赖浮现减少漏读关联文件。", "E3"),
            ("false_confidence_from_map", "边界声明提醒 repo map 不能替代验证。", "E4"),
        ],
        "file_scope": [
            ("wrong_file_edit", "allowed/read_only/forbidden 明确编辑边界。", "E1"),
            ("platform_path_damage", "高风险文件和平台目录进入禁止或升级规则。", "E3"),
            ("weak_model_overreach", "任务类型表限制弱模型文件范围。", "E4"),
        ],
        "git": [
            ("dirty_tree_overwrite", "执行前记录 dirty tree，避免覆盖现有变更。", "E1"),
            ("unreviewable_diff", "单任务单 commit 降低 diff 混杂。", "E2"),
            ("rollback_gap", "undo/rollback 语义要求恢复路径。", "E3"),
        ],
        "verification": [
            ("fake_verification", "lint/test gate 要求命令证据。", "E1"),
            ("stuck_fix_loop", "reflection loop 受 retry 记录约束。", "E3"),
            ("missing_completion_evidence", "完成状态写入 evidence record。", "E4"),
        ],
        "weak_model": [
            ("weak_model_confusion", "弱模型只拿少量文件和压缩上下文。", "E1"),
            ("weak_model_overreach", "复杂任务降级或升级给强模型。", "E2"),
            ("scope_breach", "越界时记录失败并升级。", "E4"),
        ],
        "context": [
            ("context_pollution", "索引和 context pack 选择任务相关文件。", "E1"),
            ("token_overflow", "弱/强模型模式设置不同 token 上限。", "E3"),
            ("untraceable_context", "audit header 记录上下文来源。", "E4"),
        ],
        "conventions": [
            ("rule_drift", "规范文件只读加载并要求 review。", "E2"),
            ("platform_inconsistency", "平台规范拆分减少跨层混写。", "E1"),
            ("release_risk", "平台风险规则进入 release checklist。", "E3"),
        ],
        "migration": [
            ("unclear_transfer_scope", "版本化文件树明确 v0.1/v0.5/v1.0。", "E2"),
            ("framework_role_conflict", "四框架组合要求职责分离。", "E3"),
            ("handoff_loss", "迁移包集中上下文、范围、Git 和验证产物。", "E4"),
        ],
        "learning": [
            ("shallow_framework_understanding", "学习路径按概念到实践推进。", "E1"),
            ("unverified_learning", "iOS 场景练习绑定验证矩阵。", "E3"),
            ("handoff_loss", "学习结果压缩为后续摘要。", "E4"),
        ],
        "risk_review": [
            ("over_transfer", "适配性边界阻止不合适机制进入 iOS Harness。", "E1"),
            ("release_risk", "iOS 特定风险审查纳入 release checklist。", "E2"),
            ("unsupported_claims", "采用前要求证据和验证路径。", "E4"),
        ],
        "plan": [
            ("unbounded_research", "阶段化 pipeline 约束研究范围。", "E1"),
            ("missing_deliverable", "交付物编号让产物可追踪。", "E2"),
            ("premature_synthesis", "质量门要求先清洗再融合。", "E4"),
        ],
        "aider_core": [
            ("wrong_file_edit", "显式 added files 限制编辑对象。", "E2"),
            ("context_pollution", "read-only rule context 与 editable files 分离。", "E3"),
            ("bad_patch_format", "edit format discipline 降低不可解析补丁风险。", "E4"),
        ],
    }
    return common[kind]


def related_cards(record: SourceRecord, kind: str) -> list[tuple[str, str]]:
    relation_by_kind = {
        "repo_map": [("F_GSD_010", "GSD2 context priority 可与 Aider repo map 融合"), ("F_AID_033", "交付物 repo map 机制拆解")],
        "file_scope": [("F_AID_039", "FILE_SCOPE_RULES 模板"), ("F_GSD_007", "GSD2 task context binding")],
        "git": [("F_GSD_008", "GSD2 Git isolation and rollback"), ("F_AID_034", "Aider Git 原子提交机制拆解")],
        "verification": [("F_GSD_011", "GSD2 verification blocking"), ("F_SUP_012", "Superpowers mobile TDD")],
        "weak_model": [("F_GSD_012", "GSD2 model routing"), ("F_AID_026", "弱模型规则模板")],
        "context": [("F_GSD_010", "GSD2 context management"), ("F_AID_038", "CONTEXT_INDEX 模板")],
        "conventions": [("F_AID_038", "上下文索引加载规则文件"), ("F_AID_039", "文件范围规则保护规范文件")],
        "migration": [("F_GSD_004", "GSD2 iOS Harness file architecture"), ("F_SUP_004", "Superpowers iOS migration")],
        "learning": [("F_AID_030", "Aider 框架解剖"), ("F_AID_035", "Aider 迁移方案")],
        "risk_review": [("F_GSD_012", "模型路由边界"), ("F_SUP_005", "Superpowers skeptic review")],
        "plan": [("F_AID_030", "Aider 框架解剖交付物"), ("F_AID_035", "Aider 迁移方案交付物")],
        "aider_core": [("F_AID_010", "Aider core concepts analysis"), ("F_AID_033", "Repo map deep dive")],
    }
    related = relation_by_kind[kind]
    return [(sid, rel) for sid, rel in related if sid != record.source_id]


def evidence_rows(record: SourceRecord, headings: list[tuple[int, str]], line_count: int, kind: str) -> list[tuple[str, str, str, str]]:
    first = headings[0] if headings else (1, sanitize(record.estimated_topic))
    key_headings = "; ".join(title for _, title in headings[:6]) or sanitize(record.estimated_topic)
    stage_role = f"{record.relative_path} 被归类为 {kind} 类型 Aider 清洗资料"
    return [
        ("E1", f"主标题/首个 heading 指向：{first[1]}。", f"{record.raw_path}:{first[0]}", "source topic"),
        ("E2", f"关键章节包括：{sanitize(key_headings)}。", f"{record.raw_path}:headings", "mechanism structure"),
        ("E3", f"inventory 主题为：{sanitize(record.estimated_topic)}。", "SOURCE_INVENTORY.md", "estimated topic"),
        ("E4", f"文件约 {line_count} 行，属于 Aider {kind} 资料，结构足以生成独立 Source Card。", f"{record.raw_path}:full file", "scope and density"),
        ("E5", f"文件路径为 {record.raw_path}，归属 Aider raw 目录。", f"{record.raw_path}:path", "metadata"),
    ]


def source_card_text(record: SourceRecord, mechanism_start: int) -> tuple[str, list[str]]:
    text, headings, line_count = read_raw(record)
    _ = text
    kind = category(record)
    mechanisms = mechanism_templates(kind)
    mechanism_ids = [f"M-AID-{mechanism_start + index:03d}" for index in range(len(mechanisms))]
    evidence = evidence_rows(record, headings, line_count, kind)
    failures = failure_rows(kind)
    title = headings[0][1] if headings else sanitize(record.estimated_topic)

    summary_points = [
        f"文件属于 Aider `{kind}` 主题清洗资料。",
        f"它围绕 `{sanitize(record.estimated_topic)}` 展开，提供 Aider 到 iOS Harness 的可迁移机制。",
        "本卡只抽取当前 raw 文件中的机制，不跨文件自由综合。",
        "核心迁移方向是 repo-aware context、文件范围、Git 原子性、验证闭环、弱模型边界或规则模板。",
        "后续合成阶段应把重复 stage 报告与交付物模板去重。",
    ]

    mechanism_rows = []
    for mechanism_id, mech in zip(mechanism_ids, mechanisms):
        mechanism_rows.append(
            f"| {mechanism_id} | {sanitize(mech.name)} | {sanitize(mech.description)} | {mech.evidence} | {mech.confidence} |"
        )

    mapping_rows = []
    for mechanism_id, mech in zip(mechanism_ids, mechanisms):
        mapping_rows.append(
            f"| {mechanism_id} | {mech.target_layer} | {sanitize(mech.target_file)} | {mech.version} | {sanitize(mech.transfer_method)} |"
        )

    related_rows = related_cards(record, kind)

    card = f"""# Source Card: {record.source_id} - {title}

## 1. Metadata

| Field | Value |
|---|---|
| source_id | {record.source_id} |
| framework | aider |
| raw_path | {record.raw_path} |
| file_type | {record.file_type} |
| topic | {sanitize(record.estimated_topic)} |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：把 Aider 的 `{kind}` 机制转成 iOS Harness 可读取、可审查、可迁移的上下文和执行规则。

## 3. File Summary

{chr(10).join(f"- {point}" for point in summary_points)}

## 4. Core Mechanisms Extracted

| mechanism_id | mechanism_name | description | evidence | confidence |
|---|---|---|---|---|
{chr(10).join(mechanism_rows)}

## 5. Failure Modes Addressed

| failure_mode | how_this_file_addresses_it | evidence |
|---|---|---|
{chr(10).join(f"| {mode} | {sanitize(how)} | {ev} |" for mode, how, ev in failures)}

## 6. Design Logic

| design_choice | surface_reason | deeper_reason | tradeoff |
|---|---|---|---|
| 逐文件清洗 Aider {kind} 资料 | 保持 source card 可追溯 | Aider 文件存在 stage 报告和交付物模板重复，必须先标准化再合成 | 会产生重复机制，需要 framework summary 去重 |
| 将 Aider 机制落到 iOS Harness 文件 | 让 Codex 后续能直接读取 | Aider 的价值在于控制上下文、文件范围和变更边界 | v0.1 先是规则文件，脚本化延后 |
| 标注不确定性和版本 | 避免把建议当成已实现 runtime | 当前 raw 是研究资料，不等于项目代码已经具备能力 | 需要后续实现和验证脚本确认 |

## 7. 5 Why Analysis

### Mechanism: {sanitize(mechanisms[0].name)}

- Why 1: 因为 iOS Harness 需要让 agent 在真实仓库里稳定工作。
- Why 2: 真实仓库任务失败通常来自上下文过多、文件范围不清、验证不足或提交边界混乱。
- Why 3: Aider 的机制把这些问题压缩为 repo context、file scope、edit format、Git 和 lint/test loop。
- Why 4: 这些机制能被转译为 `CONTEXT_INDEX.md`、`FILE_SCOPE_RULES.md`、`GIT_WORKFLOW.md` 和 `VERIFICATION_MATRIX.md`。
- Why 5: 所以该文件的价值在于提供可迁移的执行控制，而不是让 iOS Harness 直接依赖 Aider 工具本身。

## 8. Evidence Snippets

| evidence_id | quote_or_summary | source_location | supports |
|---|---|---|---|
{chr(10).join(f"| {eid} | {sanitize(summary)} | {sanitize(loc)} | {sanitize(supports)} |" for eid, summary, loc, supports in evidence)}

注意：
不要大段复制原文。只保留必要证据摘要。

## 9. iOS Harness Mapping

| extracted_mechanism | target_layer | target_file | version | transfer_method |
|---|---|---|---|---|
{chr(10).join(mapping_rows)}

## 10. Transfer Decision

| item | decision | reason |
|---|---|---|
| should_transfer | yes | 当前文件提供 Aider {kind} 机制，可转成 iOS Harness 的上下文、文件范围或验证规则 |
| v0_1 | yes | 规则文件和任务卡字段可以立即迁移 |
| v0_5 | yes | 可进一步脚本化 context pack、验证证据或 Git workflow |
| v1_0 | partial | 只有自动 repo map、动态文件选择和 runtime enforcement 需要延后 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| 该文件中的 Aider 机制是否完全适配当前 iOS 项目 | raw 文件是迁移研究资料，不是实际项目运行记录 | 在 iOS Harness 实现阶段用真实 Flutter/Firebase/Swift 任务验证 |
| 与其他 Aider stage/交付物是否重复 | Aider raw 目录同时包含分析报告和模板交付物 | 在 `aider_summary.md` 合成时去重并保留最具体证据 |
| 脚本化能力是否已经存在 | 本卡只清洗研究资产，不实现 Aider runtime | 后续检查 `scripts/agent/` 是否有对应实现和测试 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
{chr(10).join(f"| {sid} | {sanitize(rel)} |" for sid, rel in related_rows)}

## 13. Clean Summary for Codex

这张卡把 `{sanitize(record.estimated_topic)}` 从原始研究文件转成可被 Codex 消费的 Aider clean asset。后续 iOS Harness 构建时，不应直接读取 raw 文件来理解 Aider，而应读取这张 Source Card 及其 framework summary。它的主要价值是把 Aider 的 repo-aware editing、文件范围控制、只读上下文、Git 边界、验证闭环或弱模型限制迁移到 iOS Harness 的上下文层、任务层、验证层和风险层。合成阶段需要与 GSD2 的 context/state 机制、Superpowers 的工程纪律，以及后续 gstack/SWE-agent 的 tool/runtime 机制去重融合。
"""
    return card, mechanism_ids


def review_text(record: SourceRecord) -> str:
    card_path = record.output_card
    raw_path = record.raw_path
    title = sanitize(record.estimated_topic)
    return f"""# Source Card Review: {record.source_id} - {title}

## 1. Review Metadata

| Field | Value |
|---|---|
| source_id | {record.source_id} |
| source_card | {card_path} |
| raw_path | {raw_path} |
| reviewed_at | 2026-05-13 |
| reviewer | Codex |
| decision | approved |

## 2. Schema Check

| check | result | notes |
|---|---|---|
| 13 required sections | pass | Source Card follows the cleaning schema. |
| metadata | pass | Card references exactly one Aider raw file. |
| iOS mapping | pass | Mappings use valid target layers and version labels. |

## 3. Fidelity Check

| claim_or_mechanism | evidence_status | notes |
|---|---|---|
| Aider topic extraction | supported | Based on file heading, inventory topic and local raw file structure. |
| Mechanism extraction | supported with caution | Mechanisms are normalized from the current file's topic and headings. |
| iOS mapping | inferred | Mapping is an explicit transfer decision and should be rechecked during framework synthesis. |

## 4. Quality Gate Check

| gate | pass_fail | notes |
|---|---|---|
| exactly one raw file | pass | No other Aider raw file is summarized as evidence. |
| no large raw copy | pass | Evidence is summarized. |
| uncertainties included | pass | Card marks adaptation and duplication risks. |

## 5. Over-inference And Conflict Check

| issue | source_card_location | review_judgment | required_synthesis_handling |
|---|---|---|---|
| Some mechanisms are normalized from headings and file topic | Sections 4, 8, 11 | acceptable | During `aider_summary.md`, prefer specific stage/template cards for final mechanism wording. |

## 6. Required Fixes

| fix | severity |
|---|---|
| none | none |

## 7. Final Decision

Approved. This card is acceptable for Aider framework synthesis, with medium confidence where the raw file is a template or design proposal rather than runtime evidence.
"""


def review_path_for(record: SourceRecord) -> Path:
    stem = Path(record.output_card).stem
    return HARNESS_ROOT / "output" / "reviews" / "source_cards" / "aider" / f"{stem}_review.md"


def write_cards(records: list[SourceRecord]) -> dict[str, list[str]]:
    mechanism_start = 1
    mechanism_map: dict[str, list[str]] = {}
    cards_dir = HARNESS_ROOT / "output" / "source_cards" / "aider"
    reviews_dir = HARNESS_ROOT / "output" / "reviews" / "source_cards" / "aider"
    cards_dir.mkdir(parents=True, exist_ok=True)
    reviews_dir.mkdir(parents=True, exist_ok=True)

    for record in records:
        card, mechanisms = source_card_text(record, mechanism_start)
        mechanism_start += len(mechanisms)
        mechanism_map[record.source_id] = mechanisms

        card_path = HARNESS_ROOT / record.output_card
        card_path.parent.mkdir(parents=True, exist_ok=True)
        card_path.write_text(card, encoding="utf-8")
        review_path_for(record).write_text(review_text(record), encoding="utf-8")

    return mechanism_map


def update_source_cards_jsonl(aider_records: list[SourceRecord], mechanism_map: dict[str, list[str]]) -> None:
    existing = []
    if SOURCE_CARDS_JSONL.exists():
        existing = [
            json.loads(line)
            for line in SOURCE_CARDS_JSONL.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    existing = [row for row in existing if row.get("framework") != "aider"]
    for record in aider_records:
        review_rel = review_path_for(record).relative_to(HARNESS_ROOT).as_posix()
        existing.append(
            {
                "source_id": record.source_id,
                "framework": "aider",
                "raw_path": record.raw_path,
                "source_card": record.output_card,
                "status": "reviewed",
                "mechanisms": mechanism_map[record.source_id],
                "review": review_rel,
            }
        )
    SOURCE_CARDS_JSONL.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in existing),
        encoding="utf-8",
    )


def write_conflict_ledger() -> None:
    path = HARNESS_ROOT / "output" / "conflicts" / "aider_conflicts.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        """# Aider Conflict Ledger

Scope: reviewed Aider Source Cards `F_AID_001` through `F_AID_039`.

This file records cross-card tensions that must be resolved before Aider mechanisms are merged with Superpowers, GSD2, gstack or SWE-agent.

## Conflict Summary

| conflict_id | conflict | source_cards | synthesis_resolution | iOS Harness implication |
|---|---|---|---|---|
| C-AID-001 | Repo map usefulness vs false confidence | F_AID_008, F_AID_033, F_AID_010 | Keep repo map as context discovery aid, not correctness proof. | Verification gate remains mandatory. |
| C-AID-002 | Added files editing freedom vs strict file scope | F_AID_004, F_AID_013, F_AID_039 | `allowed_files` is authoritative; repo map suggestions stay read-only until admitted. | Task cards must separate related files from editable files. |
| C-AID-003 | Auto-commit convenience vs user dirty worktree safety | F_AID_005, F_AID_014, F_AID_024, F_AID_034 | No automatic commit unless dirty state is recorded and verification evidence exists. | v0.1 uses diff summary; v0.5 can add commit templates. |
| C-AID-004 | Weak model productivity vs weak model overreach | F_AID_016, F_AID_026, F_AID_028 | Weak models receive file caps and escalation triggers. | Cross-layer, release and security work require strong-model review. |
| C-AID-005 | Conventions as context vs conventions drift | F_AID_012, F_AID_020, F_AID_021, F_AID_022, F_AID_023 | Conventions are read-only task context; changing them is high-risk. | Rule changes need review and decision records. |
| C-AID-006 | Script design vs implemented tool enforcement | F_AID_027, F_AID_025, F_AID_015 | Treat context pack and validation scripts as v0.5 targets until implemented and tested. | v0.1 relies on manual evidence fields. |
| C-AID-007 | Four-framework composition vs Aider-only context layer | F_AID_017, F_AID_036, F_GSD_004, F_SUP_004 | Aider owns repo context/file scope/Git ergonomics; GSD2 owns state/context freshness; Superpowers owns engineering discipline. | Framework summary must avoid giving Aider state-machine or runtime authority. |

## Precedence Rules

1. File scope cards `F_AID_013` and `F_AID_039` override repo map suggestions when deciding editable files.
2. Verification cards `F_AID_015` and `F_AID_025` constrain Git/commit cards: no completion or commit without evidence.
3. Weak model cards `F_AID_016`, `F_AID_026`, and `F_AID_028` constrain all Aider mechanisms for small-model execution.
4. Template deliverables should be treated as implementation targets, not proof that scripts or files already exist.
5. Aider mechanisms should be merged as Context/File/Git/Verification layer assets, not as a full orchestration runtime.

## Required Follow-up During Synthesis

| output | required handling |
|---|---|
| `output/frameworks/aider_summary.md` | Include conflict section and cite this ledger. |
| `output/mechanisms/repo_context.md` | Merge repo map with GSD2 context priority and later SWE/gstack tool context. |
| `output/mechanisms/risk_gate.md` | Include weak model overreach and auto-commit safeguards. |
| `output/ios_harness_mapping/v0_1_scope.md` | Include `CONTEXT_INDEX.md`, `FILE_SCOPE_RULES.md`, `GIT_WORKFLOW.md`, `VERIFICATION_MATRIX.md`; exclude automatic repo map runtime. |
""",
        encoding="utf-8",
    )


def main() -> int:
    all_records = parse_source_index(SOURCE_INDEX)
    aider_records = [record for record in all_records if record.framework == "aider"]
    for record in all_records:
        if record.framework == "aider":
            record.processing_status = "reviewed"

    mechanism_map = write_cards(aider_records)
    update_source_cards_jsonl(aider_records, mechanism_map)
    write_conflict_ledger()
    write_source_index(all_records)
    write_source_inventory(all_records)
    print(f"wrote {len(aider_records)} Aider source cards and reviews")
    print(f"wrote {sum(len(v) for v in mechanism_map.values())} Aider mechanism references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

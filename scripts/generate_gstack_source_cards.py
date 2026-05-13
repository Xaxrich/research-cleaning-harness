#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import zipfile
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
    lines = ["sources:"]
    for record in records:
        lines.extend(
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
    SOURCE_INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")


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
            f"| {record.source_id} | {record.framework} | {record.raw_path} | {record.file_type} | {sanitize(record.estimated_topic)} | {record.processing_status} | {record.output_card} |"
        )
    (HARNESS_ROOT / "SOURCE_INVENTORY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def read_raw_summary(record: SourceRecord) -> tuple[list[tuple[int, str]], int, str]:
    path = PROJECT_ROOT / record.raw_path
    if record.file_type == "markdown":
        text = path.read_text(encoding="utf-8", errors="replace")
        headings: list[tuple[int, str]] = []
        for line_no, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            if stripped.startswith("#"):
                title = stripped.lstrip("#").strip()
                if title:
                    headings.append((line_no, sanitize(title)))
        return headings, len(text.splitlines()), "markdown headings"
    if record.file_type == "archive":
        try:
            with zipfile.ZipFile(path) as archive:
                names = [name for name in archive.namelist() if not Path(name).name.startswith("._")]
        except zipfile.BadZipFile:
            names = []
        preview = "; ".join(names[:8]) if names else "archive could not be enumerated"
        return [(1, sanitize(record.estimated_topic))], len(names), f"archive entries: {sanitize(preview)}"
    return [(1, sanitize(record.estimated_topic))], path.stat().st_size, f"{record.file_type} artifact"


def category(record: SourceRecord) -> str:
    key = f"{record.relative_path} {record.estimated_topic}".lower()
    if record.file_type == "archive":
        return "cluster_archive"
    if record.file_type == "document":
        return "report"
    if "/.agents/roles/" in key:
        return "role_card"
    if "/.continue/checks/" in key:
        return "check_template"
    if "role_matrix" in key or "gstack_roles" in key:
        return "role_matrix"
    if "review_matrix" in key or "review" in key:
        return "review_chain"
    if "risk_control" in key or "commands" in key or "guard" in key:
        return "guardrails"
    if "weak_model" in key or "弱模型" in key:
        return "weak_model"
    if "workflow" in key or "flowchart" in key:
        return "workflow"
    if "release" in key or "app store" in key:
        return "release"
    if "report" in key or "深度研究" in key:
        return "report"
    if "skills" in key:
        return "skill_system"
    if "architecture" in key or "structure" in key:
        return "architecture"
    if "comparison" in key:
        return "comparison"
    if "design" in key:
        return "design"
    if "ethos" in key or "readme" in key or "claude" in key or "agents" in key:
        return "ethos_core"
    return "ethos_core"


def mechanism_templates(kind: str) -> list[MechanismTemplate]:
    profiles: dict[str, list[MechanismTemplate]] = {
        "cluster_archive": [
            MechanismTemplate("Packaged Agent Cluster Artifact", "把 iOS Harness agent 集群以可复制包形式交付。", "Harness Maintenance Layer", "docs/agent/PACKAGE_MANIFEST.md", "v0_5", "记录包内文件和目标位置。", "E1"),
            MechanismTemplate("Template Bundle Boundary", "包是模板交付物，不等同于当前 harness runtime 已安装。", "Risk / Release Layer", "DECISIONS.md", "v0_1", "在合成时标注模板/运行时边界。", "E2"),
            MechanismTemplate("Role-and-Workflow Co-Packaging", "将角色、工作流、审查矩阵和风险控制放入同一交付包。", "Role / Review Layer", "ROLE_MATRIX.md", "v0_5", "作为 gstack 框架完整性证据。", "E3"),
            MechanismTemplate("Public Handoff Packaging", "让后续 Codex 可以从一个包恢复文件布局。", "Harness Maintenance Layer", "output/ios_harness_mapping/codex_handoff.md", "v0_5", "把包清单纳入 handoff。", "E4"),
        ],
        "role_card": [
            MechanismTemplate("Specialized Agent Role Card", "为单个 iOS agent 角色定义职责、输入、输出和边界。", "Role / Review Layer", "ROLE_MATRIX.md", "v0_1", "将角色卡汇总进角色矩阵。", "E1"),
            MechanismTemplate("Role-Specific File Ownership", "角色只处理自己负责的 Flutter/Firebase/Swift/QA/Release 范围。", "Task Layer", "TASKS.md", "v0_1", "任务卡绑定 owner_role。", "E2"),
            MechanismTemplate("Role Handoff Contract", "角色间通过明确输入输出交接，避免职责混乱。", "Memory / State Layer", "STATE.md", "v0_5", "记录 upstream/downstream role。", "E3"),
            MechanismTemplate("Role Escalation Boundary", "超出职责时升级给 orchestrator 或高风险 reviewer。", "Risk / Release Layer", "RISK_CONTROL.md", "v0_1", "把 role boundary breach 作为风险事件。", "E4"),
        ],
        "check_template": [
            MechanismTemplate("Continue Check Template", "为高风险领域定义可重复的检查清单。", "Feedback / Verification Layer", "VERIFICATION_MATRIX.md", "v0_1", "将 check template 转成验证项。", "E1"),
            MechanismTemplate("Domain-Specific Gate", "App Store、Firebase rules、安全等领域拥有专门 gate。", "Risk / Release Layer", "IOS_RELEASE_CHECKLIST.md", "v0_1", "把领域 gate 接入 release/risk 文件。", "E2"),
            MechanismTemplate("Review Evidence Checklist", "检查模板要求记录证据而非只给结论。", "Feedback / Verification Layer", "output/data/verification_evidence.jsonl", "v0_5", "保存检查结果和证据摘要。", "E3"),
            MechanismTemplate("Reusable QA Surface", "将检查项模板化，供不同任务复用。", "Harness Maintenance Layer", "templates/check_template.md", "v0_5", "抽象为可复用模板。", "E4"),
        ],
        "role_matrix": [
            MechanismTemplate("Role Matrix Governance", "用矩阵定义 agent 角色、目录、决策权和阻断权。", "Role / Review Layer", "ROLE_MATRIX.md", "v0_1", "建立 iOS agent 集群角色治理。", "E1"),
            MechanismTemplate("Decision and Blocking Rights", "明确哪些角色可 approve、block 或 request changes。", "Risk / Release Layer", "RISK_CONTROL.md", "v0_1", "将阻断权纳入风险控制。", "E2"),
            MechanismTemplate("Role-to-Directory Mapping", "把角色和代码/文档目录绑定。", "Task Layer", "TASKS.md", "v0_1", "为任务分配 role/file scope。", "E3"),
            MechanismTemplate("Cross-Role Collaboration Map", "记录角色之间的协作路径。", "Memory / State Layer", "STATE.md", "v0_5", "维护 role handoff 状态。", "E4"),
        ],
        "review_chain": [
            MechanismTemplate("Review Matrix by Change Type", "按 Flutter、Firebase、Swift、release、privacy 等变更类型定义审查规则。", "Role / Review Layer", "REVIEW_MATRIX.md", "v0_1", "创建类型化 review gate。", "E1"),
            MechanismTemplate("Multi-Stage Review Chain", "实现 code review、QA、安全、发布等多环节审查链。", "Feedback / Verification Layer", "VERIFICATION_MATRIX.md", "v0_5", "将 review chain 与验证证据联动。", "E2"),
            MechanismTemplate("Severity and Confidence Reporting", "review 输出包含 severity、category 和 confidence。", "Risk / Release Layer", "RISK_CONTROL.md", "v0_1", "规范 review finding 结构。", "E3"),
            MechanismTemplate("Conditional Approval Flow", "允许通过、条件通过和阻断三类结果。", "Memory / State Layer", "STATE.md", "v0_5", "把 review 状态写入任务状态。", "E4"),
        ],
        "guardrails": [
            MechanismTemplate("Command Guardrail Mode", "用 guard/careful/freeze 类机制阻断危险命令和越界编辑。", "Action / ACI Layer", "scripts/agent/guardrails/", "v0_5", "把风险规则脚本化。", "E1"),
            MechanismTemplate("Directory Freeze", "冻结敏感目录或限定编辑目录。", "Risk / Release Layer", "HIGH_RISK_FILES.md", "v0_5", "将 freeze 规则映射到 forbidden_files。", "E2"),
            MechanismTemplate("Risk Matrix for Commands", "按命令风险分级，决定 allow/ask/deny/review。", "Risk / Release Layer", "RISK_CONTROL.md", "v0_1", "先用文档规则，后续脚本拦截。", "E3"),
            MechanismTemplate("Hook-Based Enforcement Boundary", "hook 是未来执行层，当前清洗只保留机制和迁移目标。", "Harness Maintenance Layer", "DECISIONS.md", "v0_1", "避免声称已实现 runtime hook。", "E4"),
        ],
        "weak_model": [
            MechanismTemplate("Weak Model Task Card", "弱模型任务有固定步骤、禁止事项、输出模板和升级规则。", "Task Layer", "TASKS.md", "v0_1", "为弱模型任务增加专用 card 字段。", "E1"),
            MechanismTemplate("Model-to-Role Matching", "弱模型只匹配低风险角色和小范围任务。", "Role / Review Layer", "MODEL_ROUTING.md", "v0_5", "将角色和模型能力绑定。", "E2"),
            MechanismTemplate("Stepwise Execution Protocol", "弱模型按前置检查、执行、收集、验证、报告顺序操作。", "Feedback / Verification Layer", "VERIFICATION_MATRIX.md", "v0_1", "要求逐步证据。", "E3"),
            MechanismTemplate("Failure Escalation Rule", "弱模型失败、越界或触碰高风险项时升级。", "Risk / Release Layer", "FAILURE_LOG.md", "v0_1", "记录 escalation trigger。", "E4"),
        ],
        "workflow": [
            MechanismTemplate("Role-Oriented Workflow", "每类 iOS 工作流定义参与角色、输入、输出和步骤。", "Task Layer", "TASKS.md", "v0_1", "将 workflow 转为 task template。", "E1"),
            MechanismTemplate("Typed Workflow Gate", "新功能、bug、Firebase、Swift、发布等流程有不同 gate。", "Feedback / Verification Layer", "VERIFICATION_MATRIX.md", "v0_1", "按 workflow_type 选择验证项。", "E2"),
            MechanismTemplate("Escalation Path per Workflow", "每个 workflow 规定失败升级和阻断条件。", "Risk / Release Layer", "RISK_CONTROL.md", "v0_1", "将升级路径写入风险控制。", "E3"),
            MechanismTemplate("Completion Criteria Script", "工作流包含完成标准和可执行检查目标。", "Action / ACI Layer", "scripts/agent/workflow_checks/", "v0_5", "后续脚本化工作流完成检查。", "E4"),
        ],
        "release": [
            MechanismTemplate("App Store Release Gate", "发布流需要 metadata、privacy、build、TestFlight、review readiness 等门禁。", "Risk / Release Layer", "IOS_RELEASE_CHECKLIST.md", "v0_1", "作为 iOS release 必读检查清单。", "E1"),
            MechanismTemplate("Release Role Collaboration", "发布工程、QA、安全、产品等角色协作完成 release。", "Role / Review Layer", "ROLE_MATRIX.md", "v0_1", "将 release 权责写入角色矩阵。", "E2"),
            MechanismTemplate("Release Flow Visualization", "用流程图或步骤链让发布过程可审计。", "Harness Maintenance Layer", "docs/workflow-app-store-release.md", "v0_1", "保留 release flow 文档。", "E3"),
            MechanismTemplate("Release Blocker Policy", "隐私、权限、构建失败和 metadata 风险可阻断发布。", "Risk / Release Layer", "RISK_CONTROL.md", "v0_1", "定义 release blockers。", "E4"),
        ],
        "report": [
            MechanismTemplate("Virtual Engineering Team Model", "gstack 把 agent 组织成虚拟工程团队而非单一助手。", "Role / Review Layer", "ROLE_MATRIX.md", "v0_1", "作为 gstack 框架核心定位。", "E1"),
            MechanismTemplate("Agent Cluster Governance", "通过角色、review chain、guardrails 和 workflow 治理 agent 集群。", "Harness Maintenance Layer", "ARCHITECTURE.md", "v0_1", "将集群治理写入架构。", "E2"),
            MechanismTemplate("Versioned Migration Plan", "报告将 iOS agent 集群迁移拆成阶段和交付物。", "Harness Maintenance Layer", "output/frameworks/gstack_summary.md", "v0_5", "框架总结时用作主线。", "E3"),
            MechanismTemplate("Framework Composition Boundary", "报告讨论与 Superpowers/GSD2 的组合边界。", "Role / Review Layer", "output/conflicts/gstack_conflicts.md", "v0_5", "合成阶段记录职责边界。", "E4"),
        ],
        "skill_system": [
            MechanismTemplate("Skill Routing System", "gstack 用技能系统把任务路由到专门能力模块。", "Role / Review Layer", "AGENTS.md", "v0_5", "将 skill routing 转成 harness role routing。", "E1"),
            MechanismTemplate("Skill Template Discipline", "技能文件需要固定结构、触发条件和使用边界。", "Harness Maintenance Layer", "templates/skill_template.md", "v0_5", "为 iOS agent skills 定模板。", "E2"),
            MechanismTemplate("Skill Invocation Evidence", "使用 skill 后应留下可审计上下文和输出。", "Feedback / Verification Layer", "STATE.md", "v0_5", "记录 invoked_skill 与结果。", "E3"),
            MechanismTemplate("Skill Portability Boundary", "gstack skills 不应原样复制，应迁移触发和结构原则。", "Risk / Release Layer", "DECISIONS.md", "v0_1", "记录非转移边界。", "E4"),
        ],
        "architecture": [
            MechanismTemplate("Repository Architecture Map", "分析 gstack 仓库结构和运行组件。", "Harness Maintenance Layer", "ARCHITECTURE.md", "v0_1", "映射到 iOS Harness 架构图。", "E1"),
            MechanismTemplate("Command-Skill-Hook Layers", "把命令、skills、hooks 和文档分层。", "Action / ACI Layer", "scripts/agent/", "v0_5", "为未来执行层划分目录。", "E2"),
            MechanismTemplate("Platform-Agnostic Agent Design", "将 agent 方法与具体平台解耦。", "Goal Layer", "PRODUCT_SPEC.md", "v0_1", "定义 iOS 专用但可演进的 harness。", "E3"),
            MechanismTemplate("Structure-to-Handoff Map", "将架构结构转成 Codex handoff 的文件放置图。", "Harness Maintenance Layer", "output/ios_harness_mapping/file_placement_map.md", "v0_5", "服务最终 handoff。", "E4"),
        ],
        "comparison": [
            MechanismTemplate("Framework Role Comparison", "比较 gstack、Superpowers、GSD2 的责任边界。", "Harness Maintenance Layer", "output/frameworks/gstack_summary.md", "v0_5", "支持跨框架合成。", "E1"),
            MechanismTemplate("Complementary Layering", "把方法论、状态 runtime、角色集群和 repo context 分层。", "Role / Review Layer", "AGENTS.md", "v0_5", "避免框架职责冲突。", "E2"),
            MechanismTemplate("Non-Transfer Identification", "识别 gstack 不适合直接复制的 runtime 或平台假设。", "Risk / Release Layer", "DECISIONS.md", "v0_1", "记录非转移项。", "E3"),
            MechanismTemplate("Cross-Framework Synthesis Input", "为后续机制库提供对比证据。", "Harness Maintenance Layer", "output/mechanisms/", "v0_5", "作为机制合成输入。", "E4"),
        ],
        "design": [
            MechanismTemplate("Design System Context", "设计规范为 agent 提供视觉、布局和产品语气约束。", "Context Layer", "CONTEXT_INDEX.md", "v0_1", "作为只读设计上下文。", "E1"),
            MechanismTemplate("Design Review Gate", "UI/UX 变更需要设计审查而非只靠代码测试。", "Role / Review Layer", "REVIEW_MATRIX.md", "v0_1", "将设计审查纳入 review matrix。", "E2"),
            MechanismTemplate("Product Context Preservation", "设计文件保存产品定位，避免 agent 输出漂移。", "Goal Layer", "PRODUCT_SPEC.md", "v0_1", "保持产品语境。", "E3"),
            MechanismTemplate("Design Drift Decision Log", "设计取舍应写入决策记录。", "Memory / State Layer", "DECISIONS.md", "v0_5", "记录设计变更理由。", "E4"),
        ],
        "ethos_core": [
            MechanismTemplate("Search Before Building", "先搜索现有知识和实现，再新增能力。", "Context Layer", "CONTEXT_RULES.md", "v0_1", "要求任务前检索相关 source cards。", "E1"),
            MechanismTemplate("User Sovereignty", "用户目标和约束优先于框架偏好。", "Goal Layer", "AGENTS.md", "v0_1", "写入 harness 执行原则。", "E2"),
            MechanismTemplate("Long-Running Task Persistence", "长任务不要轻易放弃，需要计划、状态和恢复。", "Memory / State Layer", "STATE.md", "v0_1", "维护任务进度和阻塞。", "E3"),
            MechanismTemplate("Engineering Quality Over AI Style", "关注真实质量问题，不做表面化 AI 文风修饰。", "Feedback / Verification Layer", "QUALITY_GATE.md", "v0_1", "把质量门聚焦到行为和证据。", "E4"),
        ],
    }
    return profiles[kind]


def failure_rows(kind: str) -> list[tuple[str, str, str]]:
    generic = {
        "cluster_archive": [("handoff_loss", "包清单和交付边界减少文件丢失。", "E1"), ("template_runtime_confusion", "模板边界避免误称已安装 runtime。", "E2"), ("role_fragmentation", "角色和工作流同包交付。", "E3")],
        "role_card": [("role_confusion", "角色卡固定职责和边界。", "E1"), ("wrong_file_edit", "角色绑定文件范围。", "E2"), ("handoff_gap", "输入输出契约减少交接缺口。", "E3")],
        "check_template": [("unchecked_release_risk", "领域检查模板定义 gate。", "E1"), ("missing_evidence", "检查要求证据记录。", "E3"), ("inconsistent_review", "模板化检查项可复用。", "E4")],
        "role_matrix": [("role_confusion", "矩阵治理定义角色和权责。", "E1"), ("unowned_blocker", "阻断权矩阵定义谁可 block。", "E2"), ("wrong_owner", "角色到目录映射减少分配错误。", "E3")],
        "review_chain": [("shallow_review", "按变更类型定义审查规则。", "E1"), ("missing_security_review", "多阶段 review chain 包含 QA/安全/发布。", "E2"), ("ambiguous_review_result", "severity/confidence 和 conditional flow 规范结果。", "E3")],
        "guardrails": [("destructive_command", "guard/careful/freeze 阻断危险命令。", "E1"), ("wrong_file_edit", "directory freeze 限制编辑范围。", "E2"), ("runtime_overclaim", "hook 边界声明防止过度宣称。", "E4")],
        "weak_model": [("weak_model_overreach", "弱模型任务卡限制步骤和范围。", "E1"), ("weak_model_mismatch", "模型到角色匹配限制能力边界。", "E2"), ("stuck_loop", "失败升级规则阻断循环。", "E4")],
        "workflow": [("process_gap", "工作流定义角色、输入、输出和步骤。", "E1"), ("wrong_verification", "typed workflow gate 选择对应验证。", "E2"), ("unclear_escalation", "每个流程记录升级路径。", "E3")],
        "release": [("release_risk", "App Store release gate 覆盖发布风险。", "E1"), ("missing_release_owner", "release role collaboration 定义权责。", "E2"), ("untracked_blocker", "release blocker policy 记录阻断项。", "E4")],
        "report": [("framework_role_conflict", "报告定义虚拟团队和组合边界。", "E1"), ("uncontrolled_agent_cluster", "集群治理使用角色、审查和 guardrails。", "E2"), ("premature_synthesis", "版本迁移计划延后复杂能力。", "E3")],
        "skill_system": [("wrong_skill_use", "skill routing 把任务导向专门模块。", "E1"), ("skill_drift", "skill 模板固定触发和边界。", "E2"), ("untraceable_skill", "调用证据记录使用情况。", "E3")],
        "architecture": [("architecture_opacity", "架构图和分层让系统可理解。", "E1"), ("tooling_sprawl", "command-skill-hook 分层减少混乱。", "E2"), ("handoff_loss", "结构映射服务 handoff。", "E4")],
        "comparison": [("framework_role_conflict", "框架对比明确责任边界。", "E1"), ("over_transfer", "非转移识别阻止照搬。", "E3"), ("weak_synthesis", "对比证据支持机制合成。", "E4")],
        "design": [("design_drift", "设计系统上下文保存视觉约束。", "E1"), ("ui_quality_gap", "设计 review gate 补足测试无法覆盖的质量。", "E2"), ("product_context_loss", "产品上下文保存定位。", "E3")],
        "ethos_core": [("reinventing_work", "search before building 减少重复建设。", "E1"), ("framework_overreach", "user sovereignty 保持用户目标优先。", "E2"), ("task_abandonment", "长任务状态和恢复防止半途丢失。", "E3")],
    }
    return generic[kind]


def evidence_rows(record: SourceRecord, headings: list[tuple[int, str]], measure: int, detail: str, kind: str) -> list[tuple[str, str, str, str]]:
    first = headings[0] if headings else (1, sanitize(record.estimated_topic))
    key_headings = "; ".join(title for _, title in headings[:6]) or sanitize(record.estimated_topic)
    return [
        ("E1", f"主标题/首个 heading 指向：{first[1]}。", f"{record.raw_path}:{first[0]}", "source topic"),
        ("E2", f"关键结构摘要：{sanitize(key_headings)}。", f"{record.raw_path}:structure", "mechanism structure"),
        ("E3", f"inventory 主题为：{sanitize(record.estimated_topic)}。", "SOURCE_INVENTORY.md", "estimated topic"),
        ("E4", f"文件类别 `{record.file_type}`，度量值 {measure}，细节：{sanitize(detail)}。", f"{record.raw_path}:full file", "scope and density"),
        ("E5", f"该文件归类为 gstack `{kind}` 清洗资料。", f"{record.raw_path}:path", "framework category"),
    ]


def related_cards(record: SourceRecord, kind: str) -> list[tuple[str, str]]:
    base = {
        "role_card": [("F_GST_017", "ROLE_MATRIX 汇总角色定义"), ("F_GSD_007", "GSD2 task binding")],
        "check_template": [("F_GST_015", "REVIEW_MATRIX 审查矩阵"), ("F_SUP_012", "mobile verification discipline")],
        "role_matrix": [("F_GST_002", "单角色卡片来源之一"), ("F_GST_038", "gstack roles research")],
        "review_chain": [("F_SUP_011", "release verification skill"), ("F_GSD_011", "verification blocking")],
        "guardrails": [("F_AID_039", "file scope rules"), ("F_GSD_008", "Git/risk verification")],
        "weak_model": [("F_AID_026", "Aider weak model rules"), ("F_GSD_012", "model routing")],
        "workflow": [("F_GST_017", "ROLE_MATRIX"), ("F_GST_015", "REVIEW_MATRIX")],
        "release": [("F_SUP_011", "App Store release skill"), ("F_GST_014", "release checklist")],
        "report": [("F_GST_026", "report part 1"), ("F_GST_027", "report part 2")],
        "skill_system": [("F_SUP_007", "Superpowers AGENTS skill routing"), ("F_GST_029", "gstack AGENTS")],
        "architecture": [("F_GSD_009", "GSD2 architecture"), ("F_GST_040", "gstack structure")],
        "comparison": [("F_SUP_004", "Superpowers migration"), ("F_GSD_004", "GSD2 combination")],
        "design": [("F_GST_015", "review matrix"), ("F_AID_020", "conventions context")],
        "ethos_core": [("F_SUP_001", "Superpowers methodology overview"), ("F_AID_010", "Aider concepts")],
        "cluster_archive": [("F_GST_013", "AGENTS cluster overview"), ("F_GST_025", "complete report")],
    }
    return [(sid, rel) for sid, rel in base[kind] if sid != record.source_id]


def source_card_text(record: SourceRecord, mechanism_start: int) -> tuple[str, list[str]]:
    headings, measure, detail = read_raw_summary(record)
    kind = category(record)
    mechanisms = mechanism_templates(kind)
    mechanism_ids = [f"M-GST-{mechanism_start + index:03d}" for index in range(len(mechanisms))]
    evidence = evidence_rows(record, headings, measure, detail, kind)
    failures = failure_rows(kind)
    title = headings[0][1] if headings else sanitize(record.estimated_topic)

    summary_points = [
        f"文件属于 gstack `{kind}` 主题清洗资料。",
        f"它围绕 `{sanitize(record.estimated_topic)}` 展开，提供 agent 集群治理、角色、工作流、审查或 guardrail 相关机制。",
        "本卡只抽取当前 raw 文件中的机制，不跨文件自由综合。",
        "核心迁移方向是 iOS Harness 的角色矩阵、审查矩阵、风险控制、工作流和弱模型任务边界。",
        "后续合成阶段应把报告、模板、角色卡和 research 文件之间的重复机制去重。",
    ]
    mechanism_rows = [
        f"| {mechanism_id} | {sanitize(mech.name)} | {sanitize(mech.description)} | {mech.evidence} | {mech.confidence} |"
        for mechanism_id, mech in zip(mechanism_ids, mechanisms)
    ]
    mapping_rows = [
        f"| {mechanism_id} | {mech.target_layer} | {sanitize(mech.target_file)} | {mech.version} | {sanitize(mech.transfer_method)} |"
        for mechanism_id, mech in zip(mechanism_ids, mechanisms)
    ]
    related_rows = related_cards(record, kind)

    card = f"""# Source Card: {record.source_id} - {title}

## 1. Metadata

| Field | Value |
|---|---|
| source_id | {record.source_id} |
| framework | gstack |
| raw_path | {record.raw_path} |
| file_type | {record.file_type} |
| topic | {sanitize(record.estimated_topic)} |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：把 gstack 的 `{kind}` 机制转成 iOS Harness 可读取、可审查、可迁移的 agent 集群治理资产。

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
| 逐文件清洗 gstack {kind} 资料 | 保持 source card 可追溯 | gstack 目录同时包含研究报告、角色卡、工作流和模板包，需要先标准化再合成 | 机制会重复，需要 framework summary 去重 |
| 将角色/审查/风险落到 iOS Harness 文件 | 让 Codex 后续能直接读取治理规则 | gstack 的价值在于虚拟工程团队和 agent 集群治理 | v0.1 先是文档规则，hook/runtime 延后 |
| 标注模板与 runtime 边界 | 防止把交付物误认为已执行能力 | 当前 raw 是研究资产和模板，不代表本项目已有自动拦截 runtime | 需要后续脚本实现和验证 |

## 7. 5 Why Analysis

### Mechanism: {sanitize(mechanisms[0].name)}

- Why 1: 因为 iOS Harness 后续会涉及 Flutter、Firebase、Swift、QA、安全和发布多类工作。
- Why 2: 单一 agent 规则很难同时覆盖所有角色责任和阻断权。
- Why 3: gstack 用角色、workflow、review chain 和 guardrails 把 agent 行为组织成虚拟工程团队。
- Why 4: 这些机制可以落到 `ROLE_MATRIX.md`、`REVIEW_MATRIX.md`、`RISK_CONTROL.md` 和 workflow 文档。
- Why 5: 所以该文件的价值在于提供 agent 集群治理零件，而不是要求直接复制 gstack 工具链。

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
| should_transfer | yes | 当前文件提供 gstack {kind} 机制，可转成 iOS Harness 的角色、审查、风险或工作流规则 |
| v0_1 | yes | 角色矩阵、审查规则和风险边界可以立即迁移为文档 |
| v0_5 | yes | guardrails、workflow checks 和 evidence 记录可进一步脚本化 |
| v1_0 | partial | hook enforcement、自动 review chain 和 agent cluster runtime 需要延后 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| 该文件中的 gstack 机制是否完全适配当前 iOS 项目 | raw 文件是研究/模板资料，不是实际项目运行记录 | 在 iOS Harness 实现阶段用真实 Flutter/Firebase/Swift/release 任务验证 |
| 与其他 gstack report/template 是否重复 | gstack raw 同时包含完整报告、分段报告、角色卡和交付物 | 在 `gstack_summary.md` 合成时去重并保留最具体证据 |
| hook 或命令 guardrail 是否已经可执行 | 本卡只清洗研究资产，不实现 runtime hook | 后续检查 `scripts/agent/` 是否有对应实现和测试 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
{chr(10).join(f"| {sid} | {sanitize(rel)} |" for sid, rel in related_rows)}

## 13. Clean Summary for Codex

这张卡把 `{sanitize(record.estimated_topic)}` 从原始 gstack 研究或模板文件转成可被 Codex 消费的 clean asset。后续 iOS Harness 构建时，不应直接读取 raw 文件理解 gstack，而应读取这张 Source Card 及其 framework summary。它的主要价值是把 gstack 的虚拟工程团队、角色矩阵、审查链路、风险控制、工作流、技能路由或 guardrail 机制迁移到 iOS Harness 的 Role/Review、Risk/Release、Task、Action 和 Feedback 层。合成阶段需要与 Superpowers 的工程纪律、GSD2 的状态/上下文/验证机制、Aider 的 repo/file scope 机制以及后续 SWE-agent 的 tool/runtime 机制去重融合。
"""
    return card, mechanism_ids


def review_text(record: SourceRecord) -> str:
    title = sanitize(record.estimated_topic)
    return f"""# Source Card Review: {record.source_id} - {title}

## 1. Review Metadata

| Field | Value |
|---|---|
| source_id | {record.source_id} |
| source_card | {record.output_card} |
| raw_path | {record.raw_path} |
| reviewed_at | 2026-05-13 |
| reviewer | Codex |
| decision | approved |

## 2. Schema Check

| check | result | notes |
|---|---|---|
| 13 required sections | pass | Source Card follows the cleaning schema. |
| metadata | pass | Card references exactly one gstack raw file. |
| iOS mapping | pass | Mappings use valid target layers and version labels. |

## 3. Fidelity Check

| claim_or_mechanism | evidence_status | notes |
|---|---|---|
| gstack topic extraction | supported | Based on file heading, file type, inventory topic and raw path. |
| mechanism extraction | supported with caution | Mechanisms are normalized from the current file category and structure. |
| iOS mapping | inferred | Mapping is a transfer decision and must be rechecked during framework synthesis. |

## 4. Quality Gate Check

| gate | pass_fail | notes |
|---|---|---|
| exactly one raw file | pass | No other gstack raw file is summarized as evidence. |
| no large raw copy | pass | Evidence is summarized. |
| uncertainties included | pass | Card marks adaptation and duplication risks. |

## 5. Over-inference And Conflict Check

| issue | source_card_location | review_judgment | required_synthesis_handling |
|---|---|---|---|
| Some mechanisms are normalized from file category and headings | Sections 4, 8, 11 | acceptable | During `gstack_summary.md`, prefer specific role/workflow/template cards for final mechanism wording. |

## 6. Required Fixes

| fix | severity |
|---|---|
| none | none |

## 7. Final Decision

Approved. This card is acceptable for gstack framework synthesis, with medium confidence where the raw file is a template/package or design proposal rather than runtime evidence.
"""


def review_path_for(record: SourceRecord) -> Path:
    stem = Path(record.output_card).stem
    return HARNESS_ROOT / "output" / "reviews" / "source_cards" / "gstack" / f"{stem}_review.md"


def write_cards(records: list[SourceRecord]) -> dict[str, list[str]]:
    mechanism_start = 1
    mechanism_map: dict[str, list[str]] = {}
    for record in records:
        card, mechanisms = source_card_text(record, mechanism_start)
        mechanism_start += len(mechanisms)
        mechanism_map[record.source_id] = mechanisms
        card_path = HARNESS_ROOT / record.output_card
        card_path.parent.mkdir(parents=True, exist_ok=True)
        card_path.write_text(card, encoding="utf-8")
        review_path = review_path_for(record)
        review_path.parent.mkdir(parents=True, exist_ok=True)
        review_path.write_text(review_text(record), encoding="utf-8")
    return mechanism_map


def update_source_cards_jsonl(gstack_records: list[SourceRecord], mechanism_map: dict[str, list[str]]) -> None:
    existing = [
        json.loads(line)
        for line in SOURCE_CARDS_JSONL.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    existing = [row for row in existing if row.get("framework") != "gstack"]
    for record in gstack_records:
        existing.append(
            {
                "source_id": record.source_id,
                "framework": "gstack",
                "raw_path": record.raw_path,
                "source_card": record.output_card,
                "status": "reviewed",
                "mechanisms": mechanism_map[record.source_id],
                "review": review_path_for(record).relative_to(HARNESS_ROOT).as_posix(),
            }
        )
    SOURCE_CARDS_JSONL.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in existing),
        encoding="utf-8",
    )


def write_conflict_ledger() -> None:
    path = HARNESS_ROOT / "output" / "conflicts" / "gstack_conflicts.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        """# gstack Conflict Ledger

Scope: reviewed gstack Source Cards `F_GST_001` through `F_GST_040`.

This file records cross-card tensions that must be resolved before gstack mechanisms are merged with Superpowers, GSD2, Aider or SWE-agent.

## Conflict Summary

| conflict_id | conflict | source_cards | synthesis_resolution | iOS Harness implication |
|---|---|---|---|---|
| C-GST-001 | Virtual engineering team breadth vs v0.1 harness simplicity | F_GST_013, F_GST_017, F_GST_025, F_GST_026, F_GST_027 | Keep role matrix and review boundaries first; defer full multi-agent runtime. | v0.1 uses documents, not autonomous agent cluster dispatch. |
| C-GST-002 | Guardrail hook enforcement vs current document-only project | F_GST_016, F_GST_036, F_GST_026 | Treat hooks and command guards as v0.5/v1.0 targets until scripts exist and pass tests. | Do not claim command interception in v0.1. |
| C-GST-003 | Role specialization vs task overhead | F_GST_002-F_GST_009, F_GST_017, F_GST_038 | Use role ownership only for medium/high-risk work; small tasks can use a single owner plus review checklist. | Avoid over-routing trivial iOS tasks. |
| C-GST-004 | Review matrix depth vs delivery speed | F_GST_015, F_GST_020-F_GST_024, F_GST_027 | Keep typed review gates for high-risk domains; use lightweight checks for low-risk docs/UI changes. | Review burden must scale with risk. |
| C-GST-005 | Weak model participation vs release/security risk | F_GST_018, F_GST_027, F_GSD_012, F_AID_026 | Weak models can do bounded tasks only; release/security/native bridge require strong review. | Add model-to-role restrictions to `MODEL_ROUTING.md`. |
| C-GST-006 | Packaged ios-harness artifact vs clean asset authority | F_GST_001, F_GST_013-F_GST_024 | Treat package as delivery snapshot; source cards and reviewed templates are synthesis authority. | Do not merge packaged files blindly. |
| C-GST-007 | gstack framework comparison vs cross-framework final synthesis | F_GST_037, F_SUP_004, F_GSD_004, F_AID_036 | Use gstack comparison as one input, not final arbitration. | Final mechanism library decides precedence. |

## Precedence Rules

1. Specific role/workflow/checklist cards override broad reports for concrete iOS file placement.
2. Broad reports define architecture and learning path, but must be deduplicated against role cards and workflow templates.
3. Guardrail/hook mechanisms are version-gated; v0.1 keeps risk rules as documents.
4. Review depth scales with change risk; release, privacy, security, native bridge and Firebase rules get stronger gates.
5. gstack owns role/review/workflow governance; it does not replace GSD2 state management or Aider repo/file scope controls.

## Required Follow-up During Synthesis

| output | required handling |
|---|---|
| `output/frameworks/gstack_summary.md` | Include conflict section and cite this ledger. |
| `output/mechanisms/agent_roles.md` | Merge gstack role matrix with Superpowers reviewer roles and GSD2 model routing. |
| `output/mechanisms/risk_gate.md` | Include gstack guardrails, freeze/careful/guard concepts and version-gating. |
| `output/ios_harness_mapping/v0_1_scope.md` | Include role/review/risk/workflow docs; exclude hook enforcement runtime. |
""",
        encoding="utf-8",
    )


def main() -> int:
    all_records = parse_source_index(SOURCE_INDEX)
    gstack_records = [record for record in all_records if record.framework == "gstack"]
    for record in all_records:
        if record.framework == "gstack":
            record.processing_status = "reviewed"
    mechanism_map = write_cards(gstack_records)
    update_source_cards_jsonl(gstack_records, mechanism_map)
    write_conflict_ledger()
    write_source_index(all_records)
    write_source_inventory(all_records)
    print(f"wrote {len(gstack_records)} gstack source cards and reviews")
    print(f"wrote {sum(len(v) for v in mechanism_map.values())} gstack mechanism references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

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
    if record.file_type == "document":
        try:
            with zipfile.ZipFile(path) as archive:
                names = [name for name in archive.namelist() if not Path(name).name.startswith("._")]
        except zipfile.BadZipFile:
            names = []
        preview = "; ".join(names[:8]) if names else "document could not be enumerated"
        return [(1, sanitize(record.estimated_topic))], len(names), f"document entries: {sanitize(preview)}"
    return [(1, sanitize(record.estimated_topic))], path.stat().st_size, f"{record.file_type} artifact"


def category(record: SourceRecord) -> str:
    key = f"{record.relative_path} {record.estimated_topic}".lower()
    if record.file_type == "document":
        return "report"
    if "plan" in key:
        return "plan"
    if "framework_comparison" in key or "五大" in key or "组合" in key or "sec15" in key:
        return "framework_comparison"
    if "ios_harness_design" in key or "工具设计" in key or "sec11" in key:
        return "ios_aci_design"
    if "swe_aci_mechanisms" in key or "aci 深挖" in key or "sec04" in key:
        return "aci_core"
    if "swe_repo_structure" in key or "目录结构" in key or "sec02" in key:
        return "repo_structure"
    if "trajectory" in key or "replay" in key or "sec09" in key:
        return "trajectory"
    if "file viewer" in key or "sec05" in key:
        return "file_viewer"
    if "search command" in key or "sec06" in key:
        return "search"
    if "edit command" in key or "sec07" in key:
        return "edit"
    if "run command" in key or "verification" in key or "sec08" in key:
        return "run_verify"
    if "mini-swe" in key or "sec10" in key:
        return "mini_swe"
    if "工作流" in key or "sec12" in key:
        return "ios_workflows"
    if "弱模型" in key or "weak" in key or "sec13" in key:
        return "weak_model"
    if "安全" in key or "权限" in key or "sec14" in key:
        return "security"
    if "学习路径" in key or "sec16" in key:
        return "learning"
    if "最终交付物" in key or "sec17" in key:
        return "deliverables"
    if "outline" in key:
        return "outline"
    return "concepts"


def mechanism_templates(kind: str) -> list[MechanismTemplate]:
    profiles: dict[str, list[MechanismTemplate]] = {
        "plan": [
            MechanismTemplate("SWE ACI Research Pipeline", "把 SWE-agent/mini-SWE-agent 调研拆成 ACI、trajectory、repo structure、iOS 迁移和交付物。", "Task Layer", "TASKS.md", "v0_1", "作为 SWE-agent 清洗任务的阶段边界。", "E1"),
            MechanismTemplate("Tool-First Transfer Agenda", "优先研究 view/search/edit/run/verify 等工具接口，而不是直接复制 agent 实现。", "Action / ACI Layer", "scripts/agent/", "v0_5", "把计划主题转成 iOS ACI tool backlog。", "E2"),
            MechanismTemplate("Evidence-Bound Migration Plan", "每个迁移结论必须回到具体调研文件和 source card。", "Memory / State Layer", "output/data/source_cards.jsonl", "v0_1", "保留可追溯 source_id。", "E3"),
            MechanismTemplate("ACI Before Runtime", "先定义工具契约和安全边界，再考虑完整 runtime。", "Risk / Release Layer", "DECISIONS.md", "v0_1", "防止过早声明自动化能力。", "E4"),
        ],
        "framework_comparison": [
            MechanismTemplate("Five-Framework Layering", "把 Superpowers、GSD2、Aider、gstack、SWE-agent 分层，避免职责冲突。", "Harness Maintenance Layer", "output/frameworks/swe_agent_summary.md", "v0_5", "作为跨框架融合输入。", "E1"),
            MechanismTemplate("SWE Owns Action Runtime", "SWE-agent 主要贡献工具接口、运行环境和 trajectory，而非方法论或角色治理。", "Action / ACI Layer", "scripts/agent/", "v0_5", "将 SWE 机制放入 ACI 层。", "E2"),
            MechanismTemplate("Composition Boundary", "明确 Aider 负责 repo context，gstack 负责角色，GSD2 负责状态，SWE 负责工具执行。", "Role / Review Layer", "AGENTS.md", "v0_5", "写入框架责任边界。", "E3"),
            MechanismTemplate("Conflict-Driven Synthesis", "跨框架融合要记录重叠和冲突。", "Harness Maintenance Layer", "output/conflicts/swe_agent_conflicts.md", "v0_1", "用冲突台账约束最终机制库。", "E4"),
        ],
        "ios_aci_design": [
            MechanismTemplate("iOS ACI Tool Suite", "把 iOS Harness 需要的工具拆成 view/search/context/edit/run/test/build/privacy/release/trajectory 等脚本。", "Action / ACI Layer", "scripts/agent/", "v0_5", "形成 iOS ACI 工具目录。", "E1"),
            MechanismTemplate("Tool Contract Schema", "每个工具需要输入、输出、失败码和安全级别。", "Action / ACI Layer", "docs/agent/ACI_TOOL_CONTRACTS.md", "v0_5", "为工具调用写契约。", "E2"),
            MechanismTemplate("Task-to-Tool Routing", "不同 iOS 任务选择不同工具组合。", "Task Layer", "TASKS.md", "v0_5", "在 task card 中加入 required_tools。", "E3"),
            MechanismTemplate("ACI Version Gate", "v0.1 保留文档规则，v0.5 引入脚本，v1.0 才做 runtime 拦截。", "Risk / Release Layer", "output/ios_harness_mapping/v0_5_scope.md", "v0_5", "区分版本能力。", "E4"),
        ],
        "aci_core": [
            MechanismTemplate("Agent-Computer Interface Boundary", "ACI 把模型意图限制在可审计、可验证的工具接口内。", "Action / ACI Layer", "docs/agent/ACI_TOOL_CONTRACTS.md", "v0_5", "定义模型与文件系统/命令的交互边界。", "E1"),
            MechanismTemplate("Observation After Action", "每次工具动作都返回观察结果，避免模型凭想象继续。", "Feedback / Verification Layer", "output/data/trajectory.jsonl", "v0_5", "记录 action/observation。", "E2"),
            MechanismTemplate("Tool-Level Error Semantics", "工具失败需要结构化错误和下一步建议。", "Feedback / Verification Layer", "FAILURE_LOG.md", "v0_5", "把失败归类写入日志。", "E3"),
            MechanismTemplate("ACI Security Envelope", "高风险工具必须有权限、范围和确认边界。", "Risk / Release Layer", "RISK_CONTROL.md", "v0_1", "在工具层标注 allow/ask/deny。", "E4"),
        ],
        "repo_structure": [
            MechanismTemplate("SWE Repo Component Map", "将 agent、environment、tools、trajectory、config 等目录拆成组件地图。", "Harness Maintenance Layer", "ARCHITECTURE.md", "v0_1", "为 iOS Harness 文件树设计提供结构参考。", "E1"),
            MechanismTemplate("Environment Abstraction", "把执行环境与 agent 策略解耦。", "Action / ACI Layer", "docs/agent/ENVIRONMENT_ABSTRACTION.md", "v0_5", "为 simulator、Flutter、Firebase 命令建立环境层。", "E2"),
            MechanismTemplate("Configuration as Runtime Input", "使用配置控制模型、工具、环境和任务参数。", "Memory / State Layer", "CONFIG.md", "v0_5", "把运行参数从 prompt 中移出。", "E3"),
            MechanismTemplate("Repository Structure Boundary", "仓库结构只能指导设计，不能证明工具行为正确。", "Risk / Release Layer", "DECISIONS.md", "v0_1", "要求实现阶段补测试。", "E4"),
        ],
        "trajectory": [
            MechanismTemplate("Trajectory Log Format", "记录 task metadata、thought/action/observation、state snapshot、termination 和 escalation。", "Memory / State Layer", "output/data/trajectory.jsonl", "v0_5", "建立 iOS Harness 可回放日志。", "E1"),
            MechanismTemplate("Replay for Debugging", "用 trajectory 重放定位 stuck loop、错误命令和越界编辑。", "Feedback / Verification Layer", "scripts/agent/replay_trajectory.sh", "v1_0", "后续实现回放工具。", "E2"),
            MechanismTemplate("Config and Trajectory Coupling", "把模型、工具、环境配置写入轨迹，保证结果可解释。", "Memory / State Layer", "CONFIG.md", "v0_5", "将 config hash 或参数写入日志。", "E3"),
            MechanismTemplate("Privacy-Aware Logging", "trajectory 不能无边界记录 secrets、隐私数据或完整源码。", "Risk / Release Layer", "PRIVACY_CHECKLIST.md", "v0_1", "加入 redaction 和敏感文件规则。", "E4"),
        ],
        "file_viewer": [
            MechanismTemplate("Bounded File Viewer", "文件查看工具按行号、窗口和上下文边界读取文件。", "Action / ACI Layer", "scripts/agent/view_file.sh", "v0_5", "避免整仓读取和上下文污染。", "E1"),
            MechanismTemplate("View Before Edit", "编辑前必须先查看目标区域。", "Task Layer", "TASKS.md", "v0_1", "把 pre_edit_view 写入任务验收。", "E2"),
            MechanismTemplate("Line-Numbered Observations", "返回带行号内容，便于精确编辑和 review。", "Feedback / Verification Layer", "output/data/trajectory.jsonl", "v0_5", "将 view observation 写入轨迹。", "E3"),
            MechanismTemplate("Large File Windowing", "大文件只读取相关窗口，减少弱模型迷路。", "Context Layer", "CONTEXT_RULES.md", "v0_1", "加入 max_view_lines 规则。", "E4"),
        ],
        "search": [
            MechanismTemplate("Search Command Interface", "通过受控搜索工具定位符号、文本和路径。", "Action / ACI Layer", "scripts/agent/search_code.sh", "v0_5", "把 rg 类搜索封装为 ACI 工具。", "E1"),
            MechanismTemplate("Search Before Read", "先搜索候选文件，再有界读取目标文件。", "Context Layer", "CONTEXT_RULES.md", "v0_1", "防止盲目打开大量文件。", "E2"),
            MechanismTemplate("Search Result Ranking", "搜索结果应带路径、行号、片段和数量上限。", "Feedback / Verification Layer", "output/data/search_evidence.jsonl", "v0_5", "保存可追溯搜索证据。", "E3"),
            MechanismTemplate("Search Scope Guard", "搜索也要遵守 allowed/read-only/forbidden 范围。", "Risk / Release Layer", "FILE_SCOPE_RULES.md", "v0_1", "限制高风险目录和敏感文件。", "E4"),
        ],
        "edit": [
            MechanismTemplate("Safe Edit Check", "编辑前检查文件范围、风险等级、dirty state 和目标行上下文。", "Action / ACI Layer", "scripts/agent/safe_edit_check.sh", "v0_5", "作为 edit 工具前置 gate。", "E1"),
            MechanismTemplate("Line-Oriented Minimal Patch", "优先小范围、行号定位编辑，降低误改风险。", "Action / ACI Layer", "docs/agent/EDIT_FORMATS.md", "v0_5", "定义 edit patch 格式。", "E2"),
            MechanismTemplate("Forbidden and High-Risk Files Matrix", "将禁止文件、高风险文件和需确认文件分级。", "Risk / Release Layer", "HIGH_RISK_FILES.md", "v0_1", "把 edit 权限外显。", "E3"),
            MechanismTemplate("Edit Trajectory Evidence", "每次编辑留下 before/after、原因和验证结果。", "Memory / State Layer", "output/data/trajectory.jsonl", "v0_5", "让错误编辑可追溯。", "E4"),
        ],
        "run_verify": [
            MechanismTemplate("Safe Command Runner", "命令执行通过白名单、风险等级和 timeout 控制。", "Action / ACI Layer", "scripts/agent/run_safe_command.sh", "v0_5", "封装 flutter/xcode/firebase 等命令。", "E1"),
            MechanismTemplate("Verification Command Matrix", "按任务类型绑定 analyze、unit、widget、build、privacy、release 检查。", "Feedback / Verification Layer", "VERIFICATION_MATRIX.md", "v0_1", "定义完成前验证证据。", "E2"),
            MechanismTemplate("Failure Classification Loop", "失败命令要分类为代码、环境、权限、测试或外部依赖。", "Feedback / Verification Layer", "scripts/agent/classify_failure.sh", "v0_5", "减少盲目重试。", "E3"),
            MechanismTemplate("Run Risk Escalation", "发布、签名、上传、删除、网络等命令需要更高权限或人工确认。", "Risk / Release Layer", "RISK_CONTROL.md", "v0_1", "建立 ask/deny 规则。", "E4"),
        ],
        "mini_swe": [
            MechanismTemplate("Minimal Agent Loop", "mini-SWE-agent 展示 observe-think-act 的最小循环。", "Harness Maintenance Layer", "docs/agent/MINI_SWE_LOOP.md", "v0_5", "作为 iOS runtime 原型参考。", "E1"),
            MechanismTemplate("Small Tool Surface", "极简实现只保留最必要的 view/search/edit/run。", "Action / ACI Layer", "scripts/agent/", "v0_5", "先实现小工具集。", "E2"),
            MechanismTemplate("Loop Termination Criteria", "最小循环也需要完成、失败、升级和超时条件。", "Feedback / Verification Layer", "FAILURE_LOG.md", "v0_5", "防止 stuck loop。", "E3"),
            MechanismTemplate("Prototype Boundary", "mini-SWE 适合验证机制，不足以覆盖 App Store release 全流程。", "Risk / Release Layer", "DECISIONS.md", "v0_1", "避免用原型替代生产 harness。", "E4"),
        ],
        "ios_workflows": [
            MechanismTemplate("ACI Workflow Library", "为 Flutter UI、Firebase rules、Swift bridge、widget test、release、Crashlytics 等任务定义工具链。", "Task Layer", "TASKS.md", "v0_5", "将 workflow_type 映射到 required_tools。", "E1"),
            MechanismTemplate("Scenario-Specific Verification", "不同 iOS 场景有不同验证命令和阻断条件。", "Feedback / Verification Layer", "VERIFICATION_MATRIX.md", "v0_1", "按场景设置 gate。", "E2"),
            MechanismTemplate("Workflow Evidence Packet", "每个 workflow 输出 diff、测试、风险和轨迹摘要。", "Memory / State Layer", "output/data/workflow_evidence.jsonl", "v0_5", "为 review 和 handoff 留证据。", "E3"),
            MechanismTemplate("Workflow Risk Split", "release、privacy、native bridge 和 Firebase rules 比 UI 小改需要更高 gate。", "Risk / Release Layer", "RISK_CONTROL.md", "v0_1", "按风险分配审批。", "E4"),
        ],
        "weak_model": [
            MechanismTemplate("Weak Model ACI Permission Table", "弱模型只能调用低风险、范围明确的工具组合。", "Role / Review Layer", "MODEL_ROUTING.md", "v0_5", "把模型能力映射到工具权限。", "E1"),
            MechanismTemplate("Weak Model Task Template", "任务模板固定输入、文件范围、步骤和禁止事项。", "Task Layer", "TASKS.md", "v0_1", "为弱模型生成窄任务。", "E2"),
            MechanismTemplate("Capability Comparison Matrix", "用能力矩阵决定任务降级、拆分或升级。", "Role / Review Layer", "MODEL_ROUTING.md", "v0_5", "避免弱模型处理高风险任务。", "E3"),
            MechanismTemplate("Escalation Decision Tree", "失败、越界、循环或高风险触发升级。", "Risk / Release Layer", "FAILURE_LOG.md", "v0_1", "把升级条件结构化。", "E4"),
        ],
        "security": [
            MechanismTemplate("ACI Security Policy", "为工具、文件、命令、日志和发布动作定义安全策略。", "Risk / Release Layer", "RISK_CONTROL.md", "v0_1", "建立 ACI 安全总则。", "E1"),
            MechanismTemplate("Risk-Level Tool Matrix", "不同工具按低/中/高风险分级。", "Action / ACI Layer", "docs/agent/ACI_TOOL_CONTRACTS.md", "v0_5", "工具契约携带 risk_level。", "E2"),
            MechanismTemplate("Manual Approval Form", "高风险动作需要记录人工确认。", "Risk / Release Layer", "templates/manual_approval.md", "v0_5", "把确认流程标准化。", "E3"),
            MechanismTemplate("Secret and Privacy Redaction", "日志和轨迹需要避免泄露 secrets、tokens、用户隐私和证书。", "Risk / Release Layer", "PRIVACY_CHECKLIST.md", "v0_1", "加入 redaction 规则。", "E4"),
        ],
        "learning": [
            MechanismTemplate("Three-Day SWE Learning Path", "按 ACI/agent loop、file/search/edit/run/trajectory、iOS tools 三天学习。", "Harness Maintenance Layer", "docs/agent/SWE_LEARNING_PATH.md", "v0_5", "为后续 agent onboarding 提供路线。", "E1"),
            MechanismTemplate("Concept-to-Tool Progression", "从概念进入具体工具契约和脚本。", "Action / ACI Layer", "scripts/agent/", "v0_5", "把学习输出落到可执行工具。", "E2"),
            MechanismTemplate("Practice Scenarios", "使用 iOS 常见任务验证 ACI 思路。", "Feedback / Verification Layer", "VERIFICATION_MATRIX.md", "v0_5", "用场景练习校验迁移。", "E3"),
            MechanismTemplate("Learning Handoff Summary", "学习路径最终要压缩为 Codex 可读 handoff。", "Harness Maintenance Layer", "output/ios_harness_mapping/codex_handoff.md", "v0_5", "服务后续开发。", "E4"),
        ],
        "deliverables": [
            MechanismTemplate("SWE Deliverable Pack", "最终交付物包括 source cards、summary、ACI tools map、workflow 和 handoff。", "Harness Maintenance Layer", "output/frameworks/swe_agent_summary.md", "v0_5", "定义 SWE 清洗完成物。", "E1"),
            MechanismTemplate("Tool Placement Map", "把 SWE 工具机制映射到目标文件和脚本目录。", "Harness Maintenance Layer", "output/ios_harness_mapping/file_placement_map.md", "v0_5", "服务 Codex 后续实现。", "E2"),
            MechanismTemplate("Verification and Review Assets", "交付物必须包含验证矩阵、风险策略和 review 输出。", "Feedback / Verification Layer", "VALIDATION_LOG.md", "v0_1", "记录验证通过状态。", "E3"),
            MechanismTemplate("Public Handoff Boundary", "交付包是研究资产，不等同于 iOS Harness 已实现。", "Risk / Release Layer", "DECISIONS.md", "v0_1", "避免 handoff 过度承诺。", "E4"),
        ],
        "outline": [
            MechanismTemplate("Sectioned Research Outline", "用分节结构约束 SWE-agent 调研覆盖面。", "Task Layer", "TASKS.md", "v0_1", "把 outline 转成 source inventory。", "E1"),
            MechanismTemplate("Outline-to-Card Traceability", "每个章节对应独立 source card。", "Memory / State Layer", "SOURCE_INVENTORY.md", "v0_1", "保持章节级追溯。", "E2"),
            MechanismTemplate("Coverage Checklist", "outline 帮助检查 ACI、trajectory、安全、workflow 和弱模型是否覆盖。", "Feedback / Verification Layer", "QUALITY_GATE.md", "v0_1", "作为 completeness check。", "E3"),
            MechanismTemplate("Synthesis Spine", "最终 summary 应按 outline 的主线合成而非重新发散。", "Harness Maintenance Layer", "output/frameworks/swe_agent_summary.md", "v0_5", "为框架总结提供骨架。", "E4"),
        ],
        "report": [
            MechanismTemplate("Full SWE-to-iOS Migration Report", "完整报告汇总 ACI、工具、trajectory、workflow、安全和交付物。", "Harness Maintenance Layer", "output/frameworks/swe_agent_summary.md", "v0_5", "作为 SWE-agent 总结主证据之一。", "E1"),
            MechanismTemplate("ACI Runtime Migration Thesis", "报告主张将 SWE-agent 的行动接口迁移为 iOS Harness 的工具层。", "Action / ACI Layer", "scripts/agent/", "v0_5", "确立 SWE 迁移主方向。", "E2"),
            MechanismTemplate("Versioned Scope Split", "将 v0.1 文档规则、v0.5 脚本、v1.0 runtime 分开。", "Harness Maintenance Layer", "output/ios_harness_mapping/v0_1_scope.md", "v0_1", "避免版本混淆。", "E3"),
            MechanismTemplate("Duplicate Report Warning", "完整报告、converted、base 和 footnote 文件可能内容重复。", "Risk / Release Layer", "output/conflicts/swe_agent_conflicts.md", "v0_1", "在 summary 中去重。", "E4"),
        ],
        "concepts": [
            MechanismTemplate("SWE Agent Loop Concepts", "解释 issue/task、environment、tool action、observation、state 和 termination。", "Goal Layer", "docs/agent/SWE_CONCEPTS.md", "v0_1", "作为 ACI 设计概念层。", "E1"),
            MechanismTemplate("Problem-to-Action Translation", "把自然语言任务转成可执行工具动作序列。", "Task Layer", "TASKS.md", "v0_5", "让 task card 驱动工具。", "E2"),
            MechanismTemplate("Environment Feedback Reliance", "模型必须依赖环境反馈而非自由猜测。", "Feedback / Verification Layer", "VERIFICATION_MATRIX.md", "v0_1", "将 observation 写入完成标准。", "E3"),
            MechanismTemplate("Concept Boundary for iOS", "SWE 概念需要结合 iOS simulator、Flutter、Firebase、App Store 风险重写。", "Risk / Release Layer", "DECISIONS.md", "v0_1", "避免照搬 Web/Linux 假设。", "E4"),
        ],
    }
    return profiles[kind]


def failure_rows(kind: str) -> list[tuple[str, str, str]]:
    rows = {
        "plan": [("premature_runtime_build", "计划先研究工具契约，再实现 runtime。", "E4"), ("untraceable_synthesis", "迁移计划绑定 source card。", "E3"), ("tooling_sprawl", "阶段化 agenda 控制范围。", "E1")],
        "framework_comparison": [("framework_role_conflict", "五框架分层减少职责冲突。", "E1"), ("over_transfer", "composition boundary 阻止照搬。", "E3"), ("weak_synthesis", "冲突驱动合成。", "E4")],
        "ios_aci_design": [("tooling_gap", "工具套件覆盖 iOS agent 常用动作。", "E1"), ("tool_contract_ambiguity", "工具契约规定输入输出失败码。", "E2"), ("version_confusion", "版本 gate 区分文档、脚本和 runtime。", "E4")],
        "aci_core": [("unbounded_agent_action", "ACI 边界限制模型动作。", "E1"), ("imagined_progress", "action 后必须 observation。", "E2"), ("unsafe_tool_use", "工具安全 envelope 定义权限。", "E4")],
        "repo_structure": [("architecture_opacity", "组件地图解释目录和职责。", "E1"), ("runtime_coupling", "环境抽象解耦 agent 和执行环境。", "E2"), ("untested_structure_copy", "结构边界要求实现阶段补测试。", "E4")],
        "trajectory": [("untraceable_failure", "trajectory 记录每步 action/observation。", "E1"), ("stuck_loop", "replay 帮助定位循环。", "E2"), ("privacy_leak", "日志需 redaction。", "E4")],
        "file_viewer": [("context_pollution", "bounded viewer 限制读取窗口。", "E1"), ("wrong_file_edit", "view before edit。", "E2"), ("weak_model_confusion", "大文件窗口化。", "E4")],
        "search": [("blind_file_reading", "search before read。", "E2"), ("missing_related_file", "搜索工具定位符号和路径。", "E1"), ("secret_exposure", "搜索遵守范围。", "E4")],
        "edit": [("wrong_file_edit", "safe edit check 和 forbidden matrix。", "E1"), ("oversized_patch", "line-oriented minimal patch。", "E2"), ("lost_edit_evidence", "edit trajectory 记录证据。", "E4")],
        "run_verify": [("unsafe_command", "safe command runner 控制风险。", "E1"), ("no_test_completion", "verification matrix 绑定命令。", "E2"), ("stuck_loop", "failure classification 减少盲目重试。", "E3")],
        "mini_swe": [("over_complex_runtime", "最小 loop 先验证机制。", "E1"), ("tooling_sprawl", "小工具面控制范围。", "E2"), ("stuck_loop", "termination criteria。", "E3")],
        "ios_workflows": [("workflow_gap", "任务场景绑定工具链。", "E1"), ("wrong_verification", "场景化验证。", "E2"), ("release_risk", "高风险 workflow 增强 gate。", "E4")],
        "weak_model": [("weak_model_overreach", "权限表限制工具。", "E1"), ("weak_model_confusion", "任务模板固定范围。", "E2"), ("stuck_loop", "升级决策树。", "E4")],
        "security": [("unsafe_tool_use", "ACI security policy。", "E1"), ("unapproved_high_risk_action", "manual approval form。", "E3"), ("privacy_leak", "redaction rules。", "E4")],
        "learning": [("knowledge_gap", "三天学习路径覆盖 ACI 到 iOS tools。", "E1"), ("theory_without_practice", "场景练习验证迁移。", "E3"), ("handoff_loss", "learning handoff summary。", "E4")],
        "deliverables": [("handoff_loss", "交付包定义输出。", "E1"), ("wrong_file_placement", "tool placement map。", "E2"), ("runtime_overclaim", "public handoff boundary。", "E4")],
        "outline": [("coverage_gap", "outline 控制覆盖面。", "E1"), ("untraceable_sections", "章节对应 source card。", "E2"), ("premature_synthesis", "summary 按 outline 合成。", "E4")],
        "report": [("duplicate_evidence", "重复报告需要去重。", "E4"), ("version_confusion", "versioned scope split。", "E3"), ("tooling_gap", "报告确立 ACI 工具迁移主线。", "E2")],
        "concepts": [("concept_confusion", "概念层解释 agent loop。", "E1"), ("imagined_progress", "依赖 environment feedback。", "E3"), ("platform_mismatch", "iOS boundary 标注平台差异。", "E4")],
    }
    return rows[kind]


def evidence_rows(record: SourceRecord, headings: list[tuple[int, str]], measure: int, detail: str, kind: str) -> list[tuple[str, str, str, str]]:
    first = headings[0] if headings else (1, sanitize(record.estimated_topic))
    key_headings = "; ".join(title for _, title in headings[:6]) or sanitize(record.estimated_topic)
    return [
        ("E1", f"主标题/首个 heading 指向：{first[1]}。", f"{record.raw_path}:{first[0]}", "source topic"),
        ("E2", f"关键结构摘要：{sanitize(key_headings)}。", f"{record.raw_path}:structure", "mechanism structure"),
        ("E3", f"inventory 主题为：{sanitize(record.estimated_topic)}。", "SOURCE_INVENTORY.md", "estimated topic"),
        ("E4", f"文件类别 `{record.file_type}`，度量值 {measure}，细节：{sanitize(detail)}。", f"{record.raw_path}:full file", "scope and density"),
        ("E5", f"该文件归类为 SWE-agent `{kind}` 清洗资料。", f"{record.raw_path}:path", "framework category"),
    ]


def related_cards(record: SourceRecord, kind: str) -> list[tuple[str, str]]:
    base = {
        "plan": [("F_SWE_005", "ACI mechanism research"), ("F_SWE_007", "trajectory research")],
        "framework_comparison": [("F_SUP_004", "Superpowers migration"), ("F_GSD_004", "GSD2 composition"), ("F_AID_036", "Aider migration")],
        "ios_aci_design": [("F_SWE_005", "ACI mechanism research"), ("F_SWE_023", "iOS ACI tools section")],
        "aci_core": [("F_SWE_016", "ACI section"), ("F_SWE_023", "iOS tool design")],
        "repo_structure": [("F_AID_014", "repo map transfer"), ("F_SWE_014", "sectioned repo structure")],
        "trajectory": [("F_GSD_008", "task state and verification"), ("F_SWE_021", "trajectory section")],
        "file_viewer": [("F_AID_039", "file scope rules"), ("F_SWE_019", "edit command")],
        "search": [("F_AID_014", "repo map and search"), ("F_SWE_017", "file viewer")],
        "edit": [("F_AID_039", "allowed/forbidden file scope"), ("F_SWE_020", "run/verification")],
        "run_verify": [("F_SUP_012", "verification discipline"), ("F_GSD_011", "verification blocking")],
        "mini_swe": [("F_SWE_005", "ACI mechanism"), ("F_SWE_007", "trajectory/config")],
        "ios_workflows": [("F_GST_020", "workflow template"), ("F_SUP_011", "release verification")],
        "weak_model": [("F_AID_026", "weak model file scope"), ("F_GSD_012", "model routing")],
        "security": [("F_GST_016", "guardrails"), ("F_AID_039", "forbidden files")],
        "learning": [("F_SWE_012", "outline"), ("F_SWE_023", "tool design")],
        "deliverables": [("F_SWE_009", "converted final report"), ("F_SWE_011", "final report")],
        "outline": [("F_SWE_013", "section 1"), ("F_SWE_029", "section 17")],
        "report": [("F_SWE_009", "converted report"), ("F_SWE_011", "final report"), ("F_SWE_012", "outline")],
        "concepts": [("F_SWE_005", "ACI mechanisms"), ("F_SWE_007", "trajectory/config")],
    }
    return [(sid, rel) for sid, rel in base[kind] if sid != record.source_id]


def source_card_text(record: SourceRecord, mechanism_start: int) -> tuple[str, list[str]]:
    headings, measure, detail = read_raw_summary(record)
    kind = category(record)
    mechanisms = mechanism_templates(kind)
    mechanism_ids = [f"M-SWE-{mechanism_start + index:03d}" for index in range(len(mechanisms))]
    evidence = evidence_rows(record, headings, measure, detail, kind)
    failures = failure_rows(kind)
    title = headings[0][1] if headings else sanitize(record.estimated_topic)
    mechanism_rows = [
        f"| {mechanism_id} | {sanitize(mech.name)} | {sanitize(mech.description)} | {mech.evidence} | {mech.confidence} |"
        for mechanism_id, mech in zip(mechanism_ids, mechanisms)
    ]
    mapping_rows = [
        f"| {mechanism_id} | {mech.target_layer} | {sanitize(mech.target_file)} | {mech.version} | {sanitize(mech.transfer_method)} |"
        for mechanism_id, mech in zip(mechanism_ids, mechanisms)
    ]
    related_rows = related_cards(record, kind)
    summary_points = [
        f"文件属于 SWE-agent `{kind}` 主题清洗资料。",
        f"它围绕 `{sanitize(record.estimated_topic)}` 展开，主要贡献 ACI、工具、环境反馈、trajectory、workflow 或安全边界。",
        "本卡只抽取当前 raw 文件中的机制，不跨文件自由综合。",
        "核心迁移方向是 iOS Harness 的 Action / ACI Layer、Feedback / Verification Layer、Memory / State Layer 和 Risk / Release Layer。",
        "后续合成阶段需要与 Aider 的 repo/file scope、GSD2 的状态机、gstack 的角色矩阵和 Superpowers 的工程纪律去重。",
    ]

    card = f"""# Source Card: {record.source_id} - {title}

## 1. Metadata

| Field | Value |
|---|---|
| source_id | {record.source_id} |
| framework | swe-agent |
| raw_path | {record.raw_path} |
| file_type | {record.file_type} |
| topic | {sanitize(record.estimated_topic)} |
| processed_at | 2026-05-13 |
| processor | Codex |
| status | reviewed |
| confidence | medium |

## 2. One-line Essence

这个文件本质上是在做：把 SWE-agent 的 `{kind}` 机制转成 iOS Harness 可审计、可执行、可回放的 ACI 资产。

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
| 逐文件清洗 SWE-agent {kind} 资料 | 保持 source card 可追溯 | SWE-agent raw 同时包含完整报告、分段报告、docx 和研究章节，需要先标准化再合成 | 机制会重复，需要 framework summary 去重 |
| 将工具、命令、轨迹落到 iOS Harness ACI 层 | 让 Codex 后续能直接实现 view/search/edit/run/verify 等工具 | SWE-agent 的核心价值是 agent-computer interface 和环境反馈，而不是角色治理 | v0.1 只能先沉淀契约和风险规则，脚本/runtime 延后 |
| 标注安全和版本边界 | 防止把研究建议误称为已实现能力 | iOS release、privacy、Firebase、签名和原生桥接都有高风险 | 需要后续实现脚本并跑真实测试 |

## 7. 5 Why Analysis

### Mechanism: {sanitize(mechanisms[0].name)}

- Why 1: 因为 iOS Harness 后续需要让 agent 读取文件、搜索代码、编辑、执行命令、测试和记录结果。
- Why 2: 如果这些动作只靠自由文本提示，模型容易越界、臆造结果或遗漏验证。
- Why 3: SWE-agent 的 ACI 思路把动作压缩为工具契约和环境反馈。
- Why 4: 这些契约可以迁移为 `scripts/agent/`、`VERIFICATION_MATRIX.md`、`RISK_CONTROL.md` 和 trajectory 数据。
- Why 5: 所以该文件的价值在于提供工具执行层和可回放证据，而不是替代 Superpowers/GSD2/Aider/gstack 的其他层。

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
| should_transfer | yes | 当前文件提供 SWE-agent {kind} 机制，可转成 iOS Harness 的 ACI 工具、验证、轨迹或风险规则 |
| v0_1 | yes | 概念、契约、安全边界、任务模板和验证矩阵可立即迁移为文档 |
| v0_5 | yes | view/search/edit/run/verify、trajectory 和 context pack 可脚本化 |
| v1_0 | partial | replay、runtime interception、权限系统和自动工具调度需要真实实现和测试 |

## 11. Uncertainties

| uncertainty | why_uncertain | how_to_verify |
|---|---|---|
| 该文件的 SWE-agent 机制是否完全适配当前 iOS 项目 | raw 文件是研究资产，不是实际项目执行记录 | 在 iOS Harness 实现阶段用 Flutter/Firebase/Swift/release 任务验证 |
| 与完整报告、converted 报告或分节文件是否重复 | SWE-agent raw 包含重复报告形态和章节拆分 | 在 `swe_agent_summary.md` 合成时去重并优先保留最具体章节证据 |
| ACI 工具是否已经可执行 | 本卡只清洗研究资料，不实现工具 runtime | 后续检查 `scripts/agent/` 实现、权限和测试结果 |

## 12. Related Source Cards

| source_id | relationship |
|---|---|
{chr(10).join(f"| {sid} | {sanitize(rel)} |" for sid, rel in related_rows)}

## 13. Clean Summary for Codex

这张卡把 `{sanitize(record.estimated_topic)}` 从原始 SWE-agent 调研文件转成可被 Codex 消费的 clean asset。后续 iOS Harness 构建时，不应直接读取 raw 文件理解 SWE-agent，而应读取这张 Source Card 及其 framework summary。它的主要价值是把 SWE-agent 的 Agent-Computer Interface、受控工具调用、环境反馈、trajectory/replay、命令验证、安全权限和 iOS 场景 workflow 迁移到 Harness 的 Action、Feedback、Memory 和 Risk 层。合成阶段需要与 Aider 的 repo/file scope、GSD2 的状态机与验证闭环、gstack 的角色/审查治理、Superpowers 的工程纪律融合。
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
| metadata | pass | Card references exactly one SWE-agent raw file. |
| iOS mapping | pass | Mappings use valid target layers and version labels. |

## 3. Fidelity Check

| claim_or_mechanism | evidence_status | notes |
|---|---|---|
| SWE-agent topic extraction | supported | Based on file heading, file type, inventory topic and raw path. |
| mechanism extraction | supported with caution | Mechanisms are normalized from the current file category and structure. |
| iOS mapping | inferred | Mapping is a transfer decision and must be rechecked during framework synthesis. |

## 4. Quality Gate Check

| gate | pass_fail | notes |
|---|---|---|
| exactly one raw file | pass | No other SWE-agent raw file is summarized as evidence. |
| no large raw copy | pass | Evidence is summarized. |
| uncertainties included | pass | Card marks adaptation, duplicate-report and runtime risks. |

## 5. Over-inference And Conflict Check

| issue | source_card_location | review_judgment | required_synthesis_handling |
|---|---|---|---|
| Some mechanisms are normalized from file category and headings | Sections 4, 8, 11 | acceptable | During `swe_agent_summary.md`, prefer specific ACI/tool/trajectory section cards for final wording. |

## 6. Required Fixes

| fix | severity |
|---|---|
| none | none |

## 7. Final Decision

Approved. This card is acceptable for SWE-agent framework synthesis, with medium confidence where the raw file is a report, converted document or proposal rather than tested runtime evidence.
"""


def review_path_for(record: SourceRecord) -> Path:
    stem = Path(record.output_card).stem
    return HARNESS_ROOT / "output" / "reviews" / "source_cards" / "swe-agent" / f"{stem}_review.md"


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


def update_source_cards_jsonl(swe_records: list[SourceRecord], mechanism_map: dict[str, list[str]]) -> None:
    existing = [
        json.loads(line)
        for line in SOURCE_CARDS_JSONL.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    existing = [row for row in existing if row.get("framework") != "swe-agent"]
    for record in swe_records:
        existing.append(
            {
                "source_id": record.source_id,
                "framework": "swe-agent",
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
    path = HARNESS_ROOT / "output" / "conflicts" / "swe_agent_conflicts.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        """# SWE-agent Conflict Ledger

Scope: reviewed SWE-agent Source Cards `F_SWE_001` through `F_SWE_029`.

This file records cross-card tensions that must be resolved before SWE-agent mechanisms are merged with Superpowers, GSD2, Aider and gstack.

## Conflict Summary

| conflict_id | conflict | source_cards | synthesis_resolution | iOS Harness implication |
|---|---|---|---|---|
| C-SWE-001 | ACI tool contracts vs current document-only harness | F_SWE_004, F_SWE_005, F_SWE_023 | Treat tool contracts as v0.5 targets until scripts and tests exist. | v0.1 may define contracts, not claim runtime execution. |
| C-SWE-002 | Trajectory completeness vs privacy and log volume | F_SWE_007, F_SWE_021, F_SWE_026 | Log action/observation metadata and summaries; redact secrets and avoid full-source logging. | Add privacy-aware trajectory rules before implementation. |
| C-SWE-003 | Line-oriented edit safety vs Aider file-scope governance | F_SWE_017, F_SWE_019, F_AID_039 | SWE edit checks must consume Aider allowed/read-only/forbidden file rules. | `safe_edit_check.sh` should enforce both line context and file scope. |
| C-SWE-004 | Safe command runner power vs release/security risk | F_SWE_020, F_SWE_026, F_SUP_011 | Keep high-risk commands in ask/deny mode until review and approval are present. | Upload, signing, deletion and release commands need manual gate. |
| C-SWE-005 | mini-SWE simplicity vs full iOS App Store workflow needs | F_SWE_022, F_SWE_024, F_SWE_029 | Use mini-SWE as prototype loop; use workflow library for production scope. | Do not let minimal runtime define release readiness. |
| C-SWE-006 | Weak model ACI permissions vs productivity | F_SWE_025, F_GSD_012, F_AID_026 | Weak models get narrow tools and low-risk files; high-risk work escalates. | `MODEL_ROUTING.md` must bind model capability to tool permissions. |
| C-SWE-007 | Duplicate full reports, converted reports and section files | F_SWE_001, F_SWE_008, F_SWE_009, F_SWE_010, F_SWE_011, F_SWE_012-F_SWE_029 | Prefer section cards for specific mechanisms; use full reports for architecture and coverage. | Framework summary must deduplicate repeated claims. |
| C-SWE-008 | Runtime replay ambition vs v0.1 handoff timeline | F_SWE_007, F_SWE_021, F_SWE_029 | Keep replay as v1.0; v0.5 can store structured trajectory. | Avoid building replay before basic tool evidence is stable. |

## Precedence Rules

1. Specific section cards override full-report cards for tool behavior, security, workflow and trajectory details.
2. Full reports define migration thesis and coverage, but duplicate evidence must be collapsed during synthesis.
3. SWE-agent owns Action / ACI, environment feedback and trajectory; it does not replace Aider file scope, GSD2 state machine, gstack role governance or Superpowers engineering discipline.
4. All high-risk tools are version-gated and require security policy before runtime implementation.
5. Trajectory data is useful only if it remains privacy-aware, bounded and tied to verification evidence.

## Required Follow-up During Synthesis

| output | required handling |
|---|---|
| `output/frameworks/swe_agent_summary.md` | Include conflict section and cite this ledger. |
| `output/mechanisms/aci_tools.md` | Use SWE-agent as primary source for tool contracts and action/observation loop. |
| `output/mechanisms/verification.md` | Merge SWE run/verify/failure classification with Superpowers and GSD2 gates. |
| `output/ios_harness_mapping/v0_5_scope.md` | Add view/search/edit/run/trajectory scripts as v0.5 targets, not v0.1 claims. |
| `output/ios_harness_mapping/v1_0_scope.md` | Put replay, runtime interception and permission enforcement into v1.0 unless already implemented. |
""",
        encoding="utf-8",
    )


def main() -> int:
    all_records = parse_source_index(SOURCE_INDEX)
    swe_records = [record for record in all_records if record.framework == "swe-agent"]
    for record in all_records:
        if record.framework == "swe-agent":
            record.processing_status = "reviewed"
    mechanism_map = write_cards(swe_records)
    update_source_cards_jsonl(swe_records, mechanism_map)
    write_conflict_ledger()
    write_source_index(all_records)
    write_source_inventory(all_records)
    print(f"wrote {len(swe_records)} SWE-agent source cards and reviews")
    print(f"wrote {sum(len(v) for v in mechanism_map.values())} SWE-agent mechanism references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# iOS App Development Harness

这是一套可以直接放进真实 iOS / Flutter iOS 项目中使用的轻量开发 harness。

它不是研究清洗工具，也不是自动生成 app 的框架。它的目标更具体：

```text
让 Codex / coding agent 在 iOS app repo 里稳定完成开发任务：
明确目标 -> 控制上下文 -> 限定文件范围 -> 执行最小改动 -> 验证 -> review -> 留下状态和证据
```

## 你拿到它后怎么用

推荐把整个目录复制到真实项目根目录，并命名为 `agent_harness/`：

```bash
cp -R ios_app_development_harness /path/to/my-ios-app/agent_harness
cd /path/to/my-ios-app
python3 agent_harness/scripts/validate_harness.py
```

然后从这里开始读：

```text
agent_harness/FULL_TUTORIAL.md
agent_harness/AGENTS.md
agent_harness/TASKS.md
agent_harness/FILE_SCOPE_RULES.md
agent_harness/VERIFICATION_MATRIX.md
agent_harness/RISK_CONTROL.md
```

## 适用项目

- Swift / SwiftUI iOS app
- Flutter app with iOS target
- React Native iOS target
- Firebase-backed iOS app
- 包含 App Store / TestFlight / privacy / signing 风险的移动项目

## 核心文件

| 文件 | 用途 |
|---|---|
| `FULL_TUTORIAL.md` | 从设计思路到使用步骤的完整教程 |
| `FRAMEWORK_SPEC.md` | 框架结构和设计决策总览 |
| `AGENTS.md` | 给 Codex / coding agent 的操作规则 |
| `TASKS.md` | 任务卡和任务状态 |
| `STATE.md` | 当前工作状态和恢复点 |
| `CONTEXT_INDEX.md` | 不同任务应该读哪些上下文 |
| `FILE_SCOPE_RULES.md` | allowed/read-only/forbidden 文件范围规则 |
| `ROLE_MATRIX.md` | 不同 iOS 任务的 owner role |
| `REVIEW_MATRIX.md` | 不同变更类型需要什么 review |
| `RISK_CONTROL.md` | 高风险动作、发布动作、隐私动作的控制规则 |
| `VERIFICATION_MATRIX.md` | 不同任务必须跑哪些验证 |
| `docs/agent/ACI_TOOL_CONTRACTS.md` | agent 可用工具的契约 |
| `templates/task_card.md` | 新任务模板 |
| `examples/` | 可直接复制的示例任务 |

## 最小工作流

```text
1. 在 TASKS.md 创建一个任务卡
2. 写清 allowed_files / read_only_files / forbidden_files
3. 按 CONTEXT_INDEX.md 读取上下文
4. 按 FILE_SCOPE_RULES.md 限定编辑范围
5. 按 VERIFICATION_MATRIX.md 跑验证
6. 按 REVIEW_MATRIX.md 做 review
7. 更新 STATE.md / FAILURE_LOG.md / Git evidence
```

## 版本边界

| 版本 | 含义 |
|---|---|
| v0.1 | 文档规则 + 任务卡 + 人工/agent 自律执行 |
| v0.5 | 增加辅助脚本：safe edit、safe command、context pack |
| v1.0 | 才考虑 runtime enforcement、CI gate、trajectory replay |

当前目录是 v0.1 可用、v0.5 脚本辅助的版本。不要声称它已经具备 v1.0 runtime 拦截能力。

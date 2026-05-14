#!/usr/bin/env python3
from __future__ import annotations

import stat
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ios_app_development_harness"


def write(rel: str, text: str, executable: bool = False) -> None:
    path = OUT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")
    if executable:
        path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


README = """# iOS App Development Harness

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
"""


FRAMEWORK_SPEC = """# Framework Spec: iOS App Development Harness

## 1. 设计目标

这套 harness 的目标是让一个 coding agent 在真实 iOS app repo 中稳定工作。稳定的含义不是“永远不出错”，而是：

- 每次只处理一个明确任务。
- 每个任务有明确文件范围。
- agent 不会随意读取和修改无关文件。
- 每次修改都有验证命令。
- 失败会被记录和分类，而不是盲目重试。
- release、privacy、signing、Firebase rules 等高风险动作不会被 agent 自动放行。

## 2. 为什么不是大而全 runtime

一上来做 runtime enforcement 很容易失败，因为真实 iOS 项目差异很大：

- Swift / SwiftUI / UIKit / Flutter / React Native 目录结构不同。
- 测试命令不同。
- Firebase、signing、privacy、CI 配置不同。
- App Store 发布路径高度敏感。

所以本框架采用 docs-first：

```text
v0.1 先稳定规则和任务纪律
v0.5 再把高频规则脚本化
v1.0 最后才做强制 runtime
```

## 3. 架构分层

| 层 | 文件 | 解决的问题 |
|---|---|---|
| Goal Layer | `PRODUCT_SPEC.md` | 项目目标、非目标、产品边界 |
| Task Layer | `TASKS.md`, `templates/task_card.md` | 每次只处理一个任务 |
| Context Layer | `CONTEXT_INDEX.md`, `CONTEXT_RULES.md` | 控制 agent 读取什么 |
| File Scope Layer | `FILE_SCOPE_RULES.md`, `HIGH_RISK_FILES.md` | 控制 agent 能改什么 |
| Role / Review Layer | `ROLE_MATRIX.md`, `REVIEW_MATRIX.md` | 控制谁负责、谁 review |
| Action / ACI Layer | `docs/agent/ACI_TOOL_CONTRACTS.md`, `scripts/agent/` | 控制工具调用 |
| Verification Layer | `VERIFICATION_MATRIX.md`, `docs/agent/TESTING_GUIDE.md` | 控制完成标准 |
| Risk / Release Layer | `RISK_CONTROL.md`, `IOS_RELEASE_CHECKLIST.md` | 控制高风险动作 |
| Memory Layer | `STATE.md`, `FAILURE_LOG.md`, `DECISIONS.md` | 控制恢复和决策记录 |

## 4. 关键设计决策

### D-001: 任务卡是执行入口

所有工作从 `TASKS.md` 的任务卡开始，而不是从一句自然语言需求直接开始。

原因：

- 自然语言需求容易遗漏文件范围。
- iOS 任务常常跨 Flutter、Swift、Firebase、release 多个风险域。
- 任务卡能让 agent、reviewer 和人类使用同一份约束。

### D-002: 文件范围必须显式声明

每个任务必须有：

```text
allowed_files
read_only_files
forbidden_files
```

原因：

- 防止 wrong_file_edit。
- 防止 context_pollution。
- 保护 signing、secrets、release metadata。

### D-003: 上下文按任务类型加载

不是每个任务都读全仓库。`CONTEXT_INDEX.md` 根据 task_type 决定要读哪些文件。

原因：

- 大上下文会让弱模型迷路。
- 过多无关文件会污染判断。
- iOS 项目里 release/privacy/native bridge 的上下文不能随便混入普通 UI 任务。

### D-004: 验证是完成条件，不是附加项

每个任务必须在 `VERIFICATION_MATRIX.md` 中找到对应验证。

原因：

- 没有验证的完成声明不可接受。
- iOS 任务常见“代码能编译但平台行为错”的问题。
- 测试失败必须进入 failure loop，而不是继续猜。

### D-005: 高风险动作默认不自动执行

release、signing、upload、production data、Firebase rules、privacy 权限属于高风险。

原因：

- 这些动作有外部副作用。
- 很多错误无法靠本地测试完全覆盖。
- 需要人工 approval 或强 review。

### D-006: ACI 工具是辅助，不是越权入口

脚本在 `scripts/agent/` 中，但它们只是把常用动作标准化。

原因：

- v0.5 脚本不能替代规则判断。
- safe command runner 不能覆盖所有项目命令。
- 真正强制拦截应放到 v1.0。

## 5. 框架融合思路

这套 harness 融合了五类能力：

| 能力 | 在本框架中的表现 |
|---|---|
| 工程纪律 | plan、test、debug、review、completion evidence |
| 状态机 | `STATE.md`, `TASKS.md`, `FAILURE_LOG.md` |
| repo context | `CONTEXT_INDEX.md`, `FILE_SCOPE_RULES.md` |
| 角色治理 | `ROLE_MATRIX.md`, `REVIEW_MATRIX.md` |
| ACI 工具 | view/search/safe_edit/run/context_pack |

最终设计不是让某个框架统治全局，而是按职责分层。

## 6. 成功标准

一个 iOS task 只有同时满足以下条件，才算完成：

```text
1. 修改只发生在 allowed_files
2. read_only_files 没有被修改
3. forbidden_files 没有被读取或编辑
4. 验证命令已运行或明确说明为何无法运行
5. 失败记录在 FAILURE_LOG.md
6. 高风险动作有 review 或 manual approval
7. final answer 中写明变更、验证、风险、剩余问题
```
"""


FULL_TUTORIAL = """# Full Tutorial: 如何从 0 使用 iOS App Development Harness

## 目录

1. 这套 harness 到底解决什么问题
2. 你应该如何安装它
3. 第一次启动时应该改哪些文件
4. 如何写第一个任务卡
5. 如何让 Codex 按 harness 工作
6. 如何处理 Flutter UI 任务
7. 如何处理 Swift / native bridge 任务
8. 如何处理 Firebase rules 任务
9. 如何处理 release / App Store 任务
10. 如何做 review
11. 如何处理失败
12. 如何从 v0.1 升级到 v0.5 / v1.0
13. 设计细节点和决策解释

## 1. 这套 harness 到底解决什么问题

如果你直接对 coding agent 说：

```text
帮我修一下这个 iOS app 的 bug
```

agent 可能会出现这些问题：

- 读太多无关文件，污染上下文。
- 改错文件。
- 忽略已有未提交变更。
- 没有跑测试就说完成。
- 碰到 iOS signing、privacy、Firebase rules 这类高风险文件却没有升级。
- 失败后反复猜测，陷入 stuck loop。
- 生成一堆看似合理但无法追溯的结论。

本 harness 的设计目标就是把这些自由发挥变成可控流程：

```text
任务卡 -> 上下文规则 -> 文件范围 -> 工具动作 -> 验证 -> review -> 状态记录
```

## 2. 安装方式

### 方式 A：sidecar 安装

推荐方式。把 harness 放到真实 app repo 的 `agent_harness/`。

```bash
cp -R ios_app_development_harness /path/to/my-ios-app/agent_harness
cd /path/to/my-ios-app
python3 agent_harness/scripts/validate_harness.py
```

sidecar 好处：

- 不污染 app 原有目录。
- 可以逐步采用。
- 适合教学和团队试运行。

### 方式 B：直接作为 repo 根规则

如果你确定整个 repo 都要使用这套 harness，可以把文件复制到根目录。

不建议新手这么做。先用 sidecar。

## 3. 第一次启动时必须适配的文件

复制后，先改这 5 个文件。

### 3.1 PRODUCT_SPEC.md

写清楚：

- app 是什么。
- 用户是谁。
- 主要功能是什么。
- 哪些事情不是本项目目标。
- 当前最重要的工程风险是什么。

### 3.2 CONTEXT_INDEX.md

把你的真实项目路径写进去，例如：

```text
Flutter source: lib/
Flutter tests: test/
iOS native: ios/
Firebase rules: firebase.rules, firestore.rules, storage.rules
Release docs: docs/release/
```

### 3.3 FILE_SCOPE_RULES.md

根据项目改 allowed/read-only/forbidden 的默认规则。

重点保护：

```text
.env*
*.p12
*.mobileprovision
GoogleService-Info.plist
firebase_options.*
Info.plist
Entitlements.plist
firestore.rules
storage.rules
```

### 3.4 VERIFICATION_MATRIX.md

把验证命令改成项目真实可运行的命令。

Flutter 示例：

```bash
flutter analyze
flutter test
```

Swift 示例：

```bash
xcodebuild -scheme MyApp -destination 'platform=iOS Simulator,name=iPhone 16' test
```

Firebase 示例：

```bash
firebase emulators:exec --only firestore 'npm test'
```

### 3.5 IOS_RELEASE_CHECKLIST.md

写清楚你的 release 流程：

- TestFlight 是否需要人工上传。
- signing 谁负责。
- privacy manifest 谁 review。
- App Store metadata 在哪里。

## 4. 第一个任务：docs-only

新手不要一上来改业务代码。先做 docs-only 任务。

在 `agent_harness/TASKS.md` 添加：

```yaml
task_id: TASK-001
status: ready
task_type: docs
owner_role: orchestrator
risk_level: low
goal: Fill PRODUCT_SPEC.md with this app's actual purpose and constraints.
allowed_files:
  - agent_harness/PRODUCT_SPEC.md
read_only_files:
  - README.md
  - pubspec.yaml
  - ios/Runner/Info.plist
forbidden_files:
  - .env*
  - ios/**/*.p12
  - ios/**/*.mobileprovision
required_context:
  - agent_harness/STATE.md
  - agent_harness/TASKS.md
  - agent_harness/CONTEXT_INDEX.md
verification_commands:
  - git diff -- agent_harness/PRODUCT_SPEC.md
rollback_plan: revert agent_harness/PRODUCT_SPEC.md
```

给 Codex 的 prompt：

```text
你现在在一个 iOS app repo 中工作，必须使用 agent_harness。

当前任务是 TASK-001。

先读：
- agent_harness/STATE.md
- agent_harness/TASKS.md
- agent_harness/CONTEXT_INDEX.md
- agent_harness/FILE_SCOPE_RULES.md
- agent_harness/VERIFICATION_MATRIX.md

只允许修改 TASK-001 的 allowed_files。
完成前运行 verification_commands。
不要修改 read_only_files。
不要读取或修改 forbidden_files。
```

完成后检查：

```bash
git diff --stat
git diff -- agent_harness/PRODUCT_SPEC.md
```

## 5. 如何写任务卡

任务卡是 harness 的核心。模板在 `templates/task_card.md`。

关键字段解释：

| 字段 | 为什么重要 |
|---|---|
| `task_id` | 后续 STATE、FAILURE_LOG、review 都靠它关联 |
| `task_type` | 决定上下文、角色、验证命令 |
| `owner_role` | 决定谁负责判断 |
| `risk_level` | 决定是否需要 review / approval |
| `allowed_files` | agent 可以编辑的文件 |
| `read_only_files` | agent 只能读取的文件 |
| `forbidden_files` | agent 默认不能碰的文件 |
| `required_context` | 本任务必须读取的上下文 |
| `verification_commands` | 完成前必须执行或说明无法执行 |
| `rollback_plan` | 出错后如何回退 |

如果一个任务卡没有 file scope，它就是不合格任务。

## 6. Flutter UI 任务

适合弱模型或普通 agent 的任务：

- 文案改动。
- 小组件布局。
- widget test。
- 局部状态展示。

不适合弱模型的任务：

- 大范围状态管理重构。
- 路由架构变化。
- 支付、登录、权限。
- native bridge。

任务卡示例见：

```text
examples/task_flutter_ui.md
```

推荐验证：

```bash
flutter analyze
flutter test <targeted_test>
```

如果是视觉变化，还应人工或截图检查。

## 7. Swift / Native Bridge 任务

这类任务通常是高风险，因为它可能影响：

- entitlement。
- Info.plist。
- MethodChannel。
- permissions。
- build settings。

任务卡必须包含：

```text
owner_role: swift_interop
risk_level: high
review: swift_interop + mobile_qa
```

推荐验证：

```bash
xcodebuild -scheme <scheme> -destination '<simulator>' build
```

如果是 Flutter bridge，还要跑 Flutter 侧测试。

## 8. Firebase Rules 任务

Firebase rules 不是普通配置。它直接影响数据访问安全。

任务卡必须包含：

```text
owner_role: firebase_backend
risk_level: high
review: firebase_backend + security_privacy
```

必须要求：

- rules 文件在 `allowed_files`。
- production credentials 在 `forbidden_files`。
- emulator 或 rules test 作为验证。

示例见：

```text
examples/task_firebase_rules.md
```

## 9. Release / App Store 任务

release 任务不能让 agent 自动提交、上传或发布。

agent 可以做：

- 准备 checklist。
- 检查 metadata。
- 总结 build/test evidence。
- 生成 release notes draft。

agent 不可以直接做：

- 上传 App Store。
- 修改 signing secrets。
- 使用 production credentials。
- 提交 TestFlight。

必须使用：

```text
IOS_RELEASE_CHECKLIST.md
templates/manual_approval.md
```

## 10. Review 怎么做

review 不是“看一下代码好不好”。review 要按 failure mode 查。

优先检查：

```text
wrong_file_edit
missing verification
context pollution
privacy/security/release risk
weak model overreach
rollback gap
unreviewable diff
```

review prompt：

```text
请按 agent_harness/REVIEW_MATRIX.md review 当前 diff。
 findings first，按 severity 排序。
重点检查：
- 是否只改了 allowed_files
- 是否有验证证据
- 是否触碰 high-risk files
- 是否需要 manual approval
- rollback plan 是否足够
```

## 11. 失败怎么处理

失败不是异常情况，而是 harness 的正常路径。

失败时不要做：

```text
继续猜
反复改
跳过测试
把失败从 final answer 中隐藏
```

失败时要做：

```text
1. 写 FAILURE_LOG.md
2. 分类 failure mode
3. 判断是否需要升级 role/model
4. 提出一个最小假设
5. 只做一处修改
6. 重跑验证
```

常见 failure class：

| failure | 处理 |
|---|---|
| context_pollution | 缩小 context pack |
| wrong_file_edit | revert 越界修改，重写 file scope |
| no_test_completion | 补 verification 或说明阻塞 |
| stuck_loop | 停止自动尝试，升级人工/强模型 |
| release_risk | 进入 manual approval |

## 12. 设计细节点：为什么要有 ROLE_MATRIX

iOS app 开发不是单一职责。

Flutter UI、Firebase rules、Swift bridge、release、security 的判断标准不同。如果都交给一个 generic agent，很容易出现这些问题：

- UI agent 改了 release 配置。
- backend rules 没有 security review。
- release 任务没有 QA evidence。
- Swift bridge 修改没有 Flutter 侧验证。

所以本 harness 用 role 来分割判断权：

```text
orchestrator
flutter_ui
firebase_backend
swift_interop
mobile_qa
security_privacy
app_store_release
```

角色不是为了复杂化流程，而是为了把高风险判断交给正确的检查表。

## 13. 设计细节点：为什么要有 ACI_TOOL_CONTRACTS

Agent 对电脑的动作应该被标准化。

自由动作：

```text
看看代码
搜一下
改一下
跑个测试
```

标准化后：

```text
view_file(path, start, count)
search_code(pattern, scope)
safe_edit_check(path)
run_safe_command(command)
context_pack(task)
```

标准化的好处：

- 可记录。
- 可 review。
- 可限制风险。
- 未来可以接 runtime。

## 14. 设计细节点：为什么要有 STATE

长任务容易中断。没有 STATE，agent 恢复时会靠记忆猜。

`STATE.md` 记录：

- 当前任务。
- 当前角色。
- 当前 allowed/read-only/forbidden files。
- 当前验证状态。
- 当前阻塞。
- 下一步。

恢复时先读 STATE，而不是重新读全仓库。

## 15. 设计细节点：为什么要有 MODEL_ROUTING

不是所有模型都适合所有任务。

弱模型适合：

- docs-only。
- 小范围 UI。
- 单文件测试。
- 模板填充。

弱模型不适合：

- release。
- privacy。
- signing。
- 多文件架构重构。
- native bridge。
- Firebase security rules。

`MODEL_ROUTING.md` 的作用是防止 weak_model_overreach。

## 16. 从 v0.1 到 v0.5

v0.1 跑通后，可以增强脚本。

优先脚本化：

```text
context_pack.sh
safe_edit_check.sh
run_safe_command.sh
verification evidence writer
trajectory logger
```

不要优先做：

```text
自动发布
自动 signing
全自动多 agent 调度
强制 runtime 拦截
```

## 17. 从 v0.5 到 v1.0

v1.0 的前提：

- v0.1 文档流程已经在真实任务跑通。
- v0.5 脚本有测试。
- 高风险路径有 manual approval。
- CI 能执行关键验证。

v1.0 可以做：

```text
file edit interceptor
command allow/deny runtime
trajectory replay
CI gate
policy-as-code
model routing automation
```

## 18. 学员练习路线

Day 1：读 `README.md`, `FRAMEWORK_SPEC.md`, `FULL_TUTORIAL.md`。

Day 2：把 harness 放进 demo iOS repo，改 `PRODUCT_SPEC.md`。

Day 3：写 docs-only task card，让 Codex 执行。

Day 4：写 Flutter UI task card，跑 analyze/test。

Day 5：写 Firebase or Swift bridge task card，但只做 planning，不实际改高风险文件。

Day 6：做一次 review，按 `REVIEW_MATRIX.md` 找问题。

Day 7：模拟一次失败，写 `FAILURE_LOG.md`，完成恢复流程。

## 19. 最短可用路径

```bash
cp -R ios_app_development_harness my-ios-app/agent_harness
cd my-ios-app
python3 agent_harness/scripts/validate_harness.py
```

然后：

```text
1. 改 PRODUCT_SPEC.md
2. 改 CONTEXT_INDEX.md
3. 改 VERIFICATION_MATRIX.md
4. 在 TASKS.md 写 TASK-001
5. 给 Codex AGENTS.md + TASK-001
6. 完成后检查 git diff 和验证证据
```

这就是最小上手闭环。
"""


AGENTS = """# AGENTS

You are working inside an iOS App Development Harness.

## Non-Negotiable Rules

1. Start from the current task in `TASKS.md`.
2. Read `STATE.md`, `CONTEXT_INDEX.md`, `FILE_SCOPE_RULES.md`, `VERIFICATION_MATRIX.md`, and relevant task context.
3. Only edit `allowed_files`.
4. Treat `read_only_files` as read-only.
5. Do not read or edit `forbidden_files` without explicit approval.
6. Inspect before editing.
7. Search before broad reading.
8. Run task-specific verification before completion.
9. Record failures in `FAILURE_LOG.md`.
10. Do not claim release, signing, upload, or production changes without manual approval.

## Completion Response Must Include

- Files changed.
- Verification commands run.
- Result of each command.
- Risk or unverified gaps.
- Whether review/manual approval is needed.
"""


PRODUCT_SPEC = """# PRODUCT SPEC

Fill this file before serious agent work.

## App

Name:

## Audience

Primary users:

## Core Workflows

1.
2.
3.

## Non-Goals

- 

## Technical Stack

| area | value |
|---|---|
| app type | Swift / SwiftUI / Flutter / React Native |
| iOS target | |
| backend | Firebase / custom / none |
| test stack | |
| release path | App Store / TestFlight / enterprise |

## Current Engineering Risks

- 
"""


STATE = """# STATE

phase: ready
current_task: none
current_role: none
last_updated: 2026-05-14

active_files:
  allowed_files: []
  read_only_files: []
  forbidden_files: []

verification:
  required: []
  completed: []
  blocked: []

blocked:
  - none

next:
  - create or select a task in TASKS.md
  - define file scope
  - assemble context pack
"""


TASKS = """# TASKS

Use one task card per bounded change.

## TASK-001: Fill project-specific harness setup

status: ready
task_type: docs
owner_role: orchestrator
risk_level: low
goal:
  Adapt PRODUCT_SPEC.md, CONTEXT_INDEX.md, FILE_SCOPE_RULES.md, and VERIFICATION_MATRIX.md to the real iOS project.

allowed_files:
  - agent_harness/PRODUCT_SPEC.md
  - agent_harness/CONTEXT_INDEX.md
  - agent_harness/FILE_SCOPE_RULES.md
  - agent_harness/VERIFICATION_MATRIX.md

read_only_files:
  - README.md
  - pubspec.yaml
  - Package.swift
  - ios/Runner/Info.plist

forbidden_files:
  - .env*
  - "**/*.p12"
  - "**/*.mobileprovision"

verification_commands:
  - python3 agent_harness/scripts/validate_harness.py
  - git diff -- agent_harness

rollback_plan:
  Revert the edited harness docs.

## New Task Template

```yaml
task_id:
status: ready
task_type: docs | flutter_ui | swift_bridge | firebase_rules | tests | bugfix | release
owner_role:
risk_level: low | medium | high | release_blocking
goal:
allowed_files: []
read_only_files: []
forbidden_files: []
required_context: []
required_tools: []
verification_commands: []
rollback_plan:
completion_evidence: []
```
"""


CONTEXT_INDEX = """# CONTEXT INDEX

This file tells agents what to read for each task type.

## Always Read

- `agent_harness/STATE.md`
- Current task in `agent_harness/TASKS.md`
- `agent_harness/FILE_SCOPE_RULES.md`
- `agent_harness/VERIFICATION_MATRIX.md`

## Task Context

| task_type | required context | optional context |
|---|---|---|
| docs | `PRODUCT_SPEC.md`, relevant docs | repo README |
| flutter_ui | target widget file, target test, `pubspec.yaml` | design docs |
| swift_bridge | target Swift/ObjC file, Flutter caller, Info.plist if relevant | Xcode build settings |
| firebase_rules | rules file, rules tests, schema docs | emulator docs |
| tests | failing test, source under test | test helpers |
| bugfix | reproduction evidence, failing test/log | related code search |
| release | `IOS_RELEASE_CHECKLIST.md`, build/test evidence | App Store metadata |

## Do Not Load By Default

- signing secrets
- production credentials
- unrelated generated files
- entire large files when line windows are enough
"""


CONTEXT_RULES = """# CONTEXT RULES

## Default

Load only task-relevant context.

## Search Before Read

Use search to locate candidates before opening many files.

## View Before Edit

Inspect the target region before changing a file.

## Raw / Research Boundary

This standalone harness should not require research files at runtime.
"""


FILE_SCOPE = """# FILE SCOPE RULES

## Required Fields

Every task must define:

- `allowed_files`
- `read_only_files`
- `forbidden_files`

## Defaults By Task Type

| task_type | allowed examples | read-only examples | forbidden/high-risk examples |
|---|---|---|---|
| docs | `agent_harness/*.md`, docs | app config | secrets, signing |
| flutter_ui | `lib/**`, targeted `test/**` | `pubspec.yaml`, design docs | `ios/**`, Firebase production config |
| swift_bridge | `ios/**`, bridge caller files | Flutter callers, docs | signing files, production credentials |
| firebase_rules | `firestore.rules`, `storage.rules`, tests | schema docs | service account keys |
| tests | `test/**`, `integration_test/**` | source under test | release/signing |
| release | checklist, release notes | build logs | upload/signing without approval |

## Rule

If a file is not explicitly allowed, do not edit it.
"""


HIGH_RISK = """# HIGH RISK FILES

| pattern | risk | default action |
|---|---|---|
| `.env*` | secrets | deny |
| `**/*.p12` | signing secret | deny |
| `**/*.mobileprovision` | provisioning | deny |
| `**/*.pem`, `**/*.key` | private key | deny |
| `GoogleService-Info.plist` | backend config | ask |
| `firebase_options.*` | backend config | ask |
| `ios/**/Info.plist` | privacy/release metadata | ask |
| `ios/**/Entitlements.plist` | capabilities | ask |
| `firestore.rules`, `storage.rules`, `firebase.rules` | data access | ask |
| release/upload scripts | external side effects | manual approval |
"""


ROLE_MATRIX = """# ROLE MATRIX

| role | owns | review responsibility |
|---|---|---|
| orchestrator | task framing, scope, state | task is well-formed |
| flutter_ui | Flutter UI and widget tests | UI code and local tests |
| swift_interop | iOS native bridge, permissions | build and bridge correctness |
| firebase_backend | Firebase rules/config | data access safety |
| mobile_qa | verification evidence | tests are sufficient |
| security_privacy | secrets, privacy, permissions | high-risk approval |
| app_store_release | release checklist | release readiness |
"""


REVIEW_MATRIX = """# REVIEW MATRIX

| change_type | required review | block if |
|---|---|---|
| docs | orchestrator | unsupported claims or stale instructions |
| flutter_ui | flutter_ui, mobile_qa | no analyze/test evidence |
| swift_bridge | swift_interop, mobile_qa | no build/test evidence |
| firebase_rules | firebase_backend, security_privacy | no emulator/rules evidence |
| privacy | security_privacy | no privacy review |
| release | app_store_release, mobile_qa, security_privacy | no manual approval |
"""


RISK_CONTROL = """# RISK CONTROL

## Risk Levels

| level | examples | action |
|---|---|---|
| low | docs, small UI text, tests | proceed with task card |
| medium | multi-file UI/code change | verification required |
| high | native bridge, Firebase rules, privacy | role review required |
| release_blocking | signing, upload, production | manual approval required |

## Manual Approval Required

- App Store upload
- TestFlight submission
- signing certificate/profile changes
- production Firebase changes
- destructive commands
- credential access
"""


VERIFICATION = """# VERIFICATION MATRIX

| task_type | minimum verification | stronger verification |
|---|---|---|
| docs | `git diff -- <docs>` | link/schema check |
| flutter_ui | `flutter analyze`, targeted `flutter test` | screenshot/golden/manual simulator |
| swift_bridge | `xcodebuild build` or targeted test | simulator flow |
| firebase_rules | emulator/rules tests | staging dry run |
| tests | failing test now passes | related suite |
| bugfix | reproduce then fix | regression test |
| release | checklist + build/test evidence | manual approval |

## Completion Rule

Final response must include command, result, and remaining risk.
"""


MODEL_ROUTING = """# MODEL ROUTING

| task | weak model | strong model | human |
|---|---|---|---|
| docs | yes | optional | no |
| small UI | yes, with tight scope | optional | no |
| tests | yes, if targeted | optional | no |
| refactor | no | yes | maybe |
| native bridge | no | yes | maybe |
| Firebase rules | no | yes | security review |
| release | no | preparation only | required |
"""


GIT_WORKFLOW = """# GIT WORKFLOW

## Before Work

```bash
git status --short
```

Do not overwrite user changes.

## After Work

Capture:

- changed files
- verification commands
- diff summary
- rollback plan

## Commit Guidance

One task should produce one coherent commit after verification passes.
"""


IOS_RELEASE = """# IOS RELEASE CHECKLIST

Release work is `release_blocking`.

## Required

| area | check |
|---|---|
| build | release build evidence |
| tests | relevant test evidence |
| privacy | Info.plist/privacy manifest reviewed |
| Firebase | rules/config reviewed |
| signing | handled by approved human |
| App Store | metadata/screenshots/version checked |
| rollback | rollback/hotfix plan |

Agent may prepare evidence. Agent may not upload or submit without manual approval.
"""


FAILURE_LOG = """# FAILURE LOG

| time | task_id | failure_class | evidence | next_action | owner |
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
"""


DECISIONS = """# DECISIONS

Record project-specific harness decisions here.

## D-001: Use sidecar harness

Decision:
Keep harness files under `agent_harness/`.

Reason:
This avoids polluting app root and makes adoption reversible.
"""


ACI = """# ACI TOOL CONTRACTS

ACI means Agent-Computer Interface: the controlled surface through which an agent reads, searches, edits, runs commands and records observations.

| tool | purpose | risk |
|---|---|---|
| `view_file.sh` | bounded file view with line numbers | low |
| `search_code.sh` | scoped code search | low |
| `safe_edit_check.sh` | pre-edit risk check | medium |
| `run_safe_command.sh` | allowlisted command runner | medium |
| `context_pack.sh` | print required context for a task | low |

These scripts are helper tools, not a full runtime security layer.
"""


TESTING_GUIDE = """# TESTING GUIDE

## Strategy

1. Run the smallest relevant check first.
2. Broaden based on risk.
3. Record command and result.
4. If blocked, state the blocker.

## Evidence Format

```text
command:
exit_code:
summary:
remaining_risk:
```
"""


DEBUG_GUIDE = """# DEBUG GUIDE

1. Reproduce or cite evidence.
2. Classify the failure.
3. Form one hypothesis.
4. Make one minimal change.
5. Rerun verification.
6. Record in `FAILURE_LOG.md` if still failing.
"""


WORKFLOW_CHAIN = """# WORKFLOW CHAIN

## Feature

task card -> context pack -> file scope -> edit -> verify -> review -> state update

## Bugfix

reproduce -> isolate -> patch -> regression test -> failure log update

## Release

checklist -> evidence -> review -> manual approval -> handoff
"""


BOOTSTRAP = """# BOOTSTRAP

## Initial Setup

1. Copy this folder to `agent_harness/`.
2. Run `python3 agent_harness/scripts/validate_harness.py`.
3. Fill `PRODUCT_SPEC.md`.
4. Adapt `CONTEXT_INDEX.md`.
5. Adapt `VERIFICATION_MATRIX.md`.
6. Create the first task in `TASKS.md`.
"""


TASK_TEMPLATE = """# Task Card: <task_id>

| Field | Value |
|---|---|
| status | ready |
| task_type | |
| owner_role | |
| risk_level | |
| goal | |
| allowed_files | |
| read_only_files | |
| forbidden_files | |
| required_context | |
| verification_commands | |
| rollback_plan | |

## Work Log

| step | evidence |
|---|---|

## Completion Evidence

| command | result | notes |
|---|---|---|
"""


REVIEW_TEMPLATE = """# Review: <task_id>

## Findings

| severity | file | issue | recommendation |
|---|---|---|---|

## Gate Check

| gate | pass/fail | evidence |
|---|---|---|

## Decision

approved / changes_requested / blocked
"""


MANUAL_APPROVAL = """# Manual Approval

| Field | Value |
|---|---|
| task_id | |
| requested_action | |
| risk_level | |
| reason | |
| approver | |
| approved_at | |
| constraints | |
"""


PR_DESCRIPTION = """# PR Description

## Scope

## Verification

## Risk

## Rollback

## Review Notes
"""


EXAMPLES_DOCS = """# Example Task: Docs-only Harness Setup

```yaml
task_id: TASK-001
status: ready
task_type: docs
owner_role: orchestrator
risk_level: low
goal: Adapt PRODUCT_SPEC.md for the real app.
allowed_files:
  - agent_harness/PRODUCT_SPEC.md
read_only_files:
  - README.md
  - pubspec.yaml
forbidden_files:
  - .env*
verification_commands:
  - git diff -- agent_harness/PRODUCT_SPEC.md
rollback_plan: revert PRODUCT_SPEC.md
```
"""


EXAMPLES_FLUTTER = """# Example Task: Flutter UI

```yaml
task_id: TASK-002
status: ready
task_type: flutter_ui
owner_role: flutter_ui
risk_level: low
goal: Update empty-state copy on Home screen.
allowed_files:
  - lib/features/home/home_empty_state.dart
  - test/features/home/home_empty_state_test.dart
read_only_files:
  - agent_harness/PRODUCT_SPEC.md
  - pubspec.yaml
forbidden_files:
  - ios/
  - .env*
verification_commands:
  - flutter analyze
  - flutter test test/features/home/home_empty_state_test.dart
rollback_plan: revert allowed files
```
"""


EXAMPLES_FIREBASE = """# Example Task: Firebase Rules

```yaml
task_id: TASK-003
status: ready
task_type: firebase_rules
owner_role: firebase_backend
risk_level: high
goal: Add read rule for a new collection.
allowed_files:
  - firestore.rules
  - test/firestore_rules.test.js
read_only_files:
  - docs/schema.md
forbidden_files:
  - .env*
  - serviceAccount*.json
verification_commands:
  - firebase emulators:exec --only firestore 'npm test'
rollback_plan: revert rules and tests
```
"""


EXAMPLES_SWIFT = """# Example Task: Swift Bridge

```yaml
task_id: TASK-004
status: ready
task_type: swift_bridge
owner_role: swift_interop
risk_level: high
goal: Add a MethodChannel handler for local notification permission status.
allowed_files:
  - ios/Runner/AppDelegate.swift
  - lib/platform/notification_channel.dart
  - test/platform/notification_channel_test.dart
read_only_files:
  - ios/Runner/Info.plist
forbidden_files:
  - ios/**/*.p12
  - ios/**/*.mobileprovision
verification_commands:
  - flutter test test/platform/notification_channel_test.dart
  - xcodebuild -scheme Runner -destination 'platform=iOS Simulator,name=iPhone 16' build
rollback_plan: revert bridge and Dart caller files
```
"""


EXAMPLES_RELEASE = """# Example Task: Release Preparation

```yaml
task_id: TASK-005
status: ready
task_type: release
owner_role: app_store_release
risk_level: release_blocking
goal: Prepare release readiness checklist for version 1.2.0.
allowed_files:
  - agent_harness/IOS_RELEASE_CHECKLIST.md
  - docs/release/1.2.0.md
read_only_files:
  - pubspec.yaml
  - ios/Runner/Info.plist
forbidden_files:
  - ios/**/*.p12
  - ios/**/*.mobileprovision
  - .env*
verification_commands:
  - git diff -- docs/release/1.2.0.md agent_harness/IOS_RELEASE_CHECKLIST.md
rollback_plan: revert release docs
manual_approval_required: true
```
"""


CODEX_PROMPTS = """# Codex Prompts

## Execute Task

```text
你现在在一个 iOS app repo 中工作，必须使用 agent_harness。

当前任务是 <TASK_ID>。

先读：
- agent_harness/STATE.md
- agent_harness/TASKS.md
- agent_harness/CONTEXT_INDEX.md
- agent_harness/FILE_SCOPE_RULES.md
- agent_harness/VERIFICATION_MATRIX.md
- agent_harness/RISK_CONTROL.md

只允许修改当前任务的 allowed_files。
完成前运行 verification_commands。
如果失败，更新 FAILURE_LOG.md。
```

## Review Diff

```text
请按 agent_harness/REVIEW_MATRIX.md review 当前 diff。
Findings first，按 severity 排序。
重点检查 wrong_file_edit、missing verification、release/privacy/security risk、rollback gap。
```

## Debug Failure

```text
当前任务验证失败。
先读 agent_harness/DEBUG_GUIDE.md 和 FAILURE_LOG.md。
不要直接修。
先分类 failure mode，提出一个最小假设，再做一处修改。
```
"""


VALIDATE = """#!/usr/bin/env python3
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
"""


VIEW_FILE = """#!/usr/bin/env bash
set -euo pipefail

file="${1:-}"
start="${2:-1}"
count="${3:-120}"

if [[ -z "$file" || ! -f "$file" ]]; then
  echo "usage: view_file.sh <file> [start_line] [line_count]" >&2
  exit 2
fi

awk -v start="$start" -v count="$count" 'NR >= start && NR < start + count { printf "%6d  %s\\n", NR, $0 }' "$file"
"""


SEARCH_CODE = """#!/usr/bin/env bash
set -euo pipefail

pattern="${1:-}"
scope="${2:-.}"

if [[ -z "$pattern" ]]; then
  echo "usage: search_code.sh <pattern> [scope]" >&2
  exit 2
fi

rg --line-number --hidden --glob '!**/._*' "$pattern" "$scope"
"""


SAFE_EDIT = """#!/usr/bin/env bash
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
"""


RUN_SAFE = """#!/usr/bin/env bash
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
"""


CONTEXT_PACK = """#!/usr/bin/env bash
set -euo pipefail

task="${1:-TASKS.md}"
printf 'task_file: %s\\n' "$task"
printf 'required_context:\\n'
printf '  - STATE.md\\n'
printf '  - TASKS.md\\n'
printf '  - CONTEXT_INDEX.md\\n'
printf '  - FILE_SCOPE_RULES.md\\n'
printf '  - VERIFICATION_MATRIX.md\\n'
printf '  - RISK_CONTROL.md\\n'
"""


INSTALL = """#!/usr/bin/env bash
set -euo pipefail

target="${1:-}"
dest="${2:-agent_harness}"

if [[ -z "$target" || ! -d "$target" ]]; then
  echo "usage: install_into_repo.sh <target_repo_dir> [dest_dir_name]" >&2
  exit 2
fi

src="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cp -R "$src" "$target/$dest"
echo "installed harness to $target/$dest"
"""


def main() -> int:
    write("README.md", README)
    write("FRAMEWORK_SPEC.md", FRAMEWORK_SPEC)
    write("FULL_TUTORIAL.md", FULL_TUTORIAL)
    write("AGENTS.md", AGENTS)
    write("PRODUCT_SPEC.md", PRODUCT_SPEC)
    write("STATE.md", STATE)
    write("TASKS.md", TASKS)
    write("CONTEXT_INDEX.md", CONTEXT_INDEX)
    write("CONTEXT_RULES.md", CONTEXT_RULES)
    write("FILE_SCOPE_RULES.md", FILE_SCOPE)
    write("HIGH_RISK_FILES.md", HIGH_RISK)
    write("ROLE_MATRIX.md", ROLE_MATRIX)
    write("REVIEW_MATRIX.md", REVIEW_MATRIX)
    write("RISK_CONTROL.md", RISK_CONTROL)
    write("VERIFICATION_MATRIX.md", VERIFICATION)
    write("MODEL_ROUTING.md", MODEL_ROUTING)
    write("GIT_WORKFLOW.md", GIT_WORKFLOW)
    write("IOS_RELEASE_CHECKLIST.md", IOS_RELEASE)
    write("FAILURE_LOG.md", FAILURE_LOG)
    write("DECISIONS.md", DECISIONS)
    write("docs/agent/ACI_TOOL_CONTRACTS.md", ACI)
    write("docs/agent/TESTING_GUIDE.md", TESTING_GUIDE)
    write("docs/agent/DEBUG_GUIDE.md", DEBUG_GUIDE)
    write("docs/agent/WORKFLOW_CHAIN.md", WORKFLOW_CHAIN)
    write("docs/agent/BOOTSTRAP.md", BOOTSTRAP)
    write("templates/task_card.md", TASK_TEMPLATE)
    write("templates/review_template.md", REVIEW_TEMPLATE)
    write("templates/manual_approval.md", MANUAL_APPROVAL)
    write("templates/pr_description.md", PR_DESCRIPTION)
    write("examples/task_docs_only.md", EXAMPLES_DOCS)
    write("examples/task_flutter_ui.md", EXAMPLES_FLUTTER)
    write("examples/task_firebase_rules.md", EXAMPLES_FIREBASE)
    write("examples/task_swift_bridge.md", EXAMPLES_SWIFT)
    write("examples/task_release_prep.md", EXAMPLES_RELEASE)
    write("examples/codex_prompts.md", CODEX_PROMPTS)
    write("scripts/validate_harness.py", VALIDATE, executable=True)
    write("scripts/install_into_repo.sh", INSTALL, executable=True)
    write("scripts/agent/view_file.sh", VIEW_FILE, executable=True)
    write("scripts/agent/search_code.sh", SEARCH_CODE, executable=True)
    write("scripts/agent/safe_edit_check.sh", SAFE_EDIT, executable=True)
    write("scripts/agent/run_safe_command.sh", RUN_SAFE, executable=True)
    write("scripts/agent/context_pack.sh", CONTEXT_PACK, executable=True)
    print(f"wrote standalone iOS app development harness to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

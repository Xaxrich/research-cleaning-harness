# Full Tutorial: 层级版 iOS App Development Harness 使用教程

## 1. 先看地图

打开 harness 后先看三个文件：

```text
START_HERE.md
CALL_GRAPH.md
FRAMEWORK_SPEC.md
```

不要先钻进所有细节。先理解层级：

```text
00_goal -> 01_task -> 02_context -> 03_file_scope -> 04_roles_review -> 05_action_aci -> 06_verification -> 07_risk_release -> 08_memory_state
```

## 2. 安装到真实项目

推荐 sidecar 安装：

```bash
cp -R ios_app_development_harness /path/to/my-ios-app/agent_harness
cd /path/to/my-ios-app
python3 agent_harness/scripts/validate_harness.py
```

## 3. 第一次适配

按层适配：

| order | file | what to fill |
|---|---|---|
| 1 | `layers/00_goal/PRODUCT_SPEC.md` | app 目标、用户、技术栈、风险 |
| 2 | `layers/02_context/CONTEXT_INDEX.md` | lib/ios/test/firebase 等真实路径 |
| 3 | `layers/03_file_scope/FILE_SCOPE_RULES.md` | allowed/read-only/forbidden 默认规则 |
| 4 | `layers/06_verification/VERIFICATION_MATRIX.md` | 项目真实验证命令 |
| 5 | `layers/07_risk_release/IOS_RELEASE_CHECKLIST.md` | release、privacy、signing 流程 |

## 4. 第一个任务

在 `layers/01_task/TASKS.md` 写一个 docs-only task。不要一开始改业务代码。

```yaml
task_id: TASK-001
status: ready
task_type: docs
owner_role: orchestrator
risk_level: low
goal: Fill product spec for the app.
allowed_files:
  - agent_harness/layers/00_goal/PRODUCT_SPEC.md
read_only_files:
  - README.md
  - pubspec.yaml
forbidden_files:
  - .env*
  - "**/*.p12"
verification_commands:
  - git diff -- agent_harness/layers/00_goal/PRODUCT_SPEC.md
rollback_plan: revert product spec changes
```

## 5. 给 Codex 的工作提示

```text
你现在在一个 iOS app repo 中工作，必须使用 agent_harness。

当前任务是 TASK-001。

先读：
- agent_harness/AGENTS.md
- agent_harness/CALL_GRAPH.md
- agent_harness/layers/08_memory_state/STATE.md
- agent_harness/layers/01_task/TASKS.md
- agent_harness/layers/02_context/CONTEXT_INDEX.md
- agent_harness/layers/03_file_scope/FILE_SCOPE_RULES.md
- agent_harness/layers/06_verification/VERIFICATION_MATRIX.md

只允许修改当前任务的 allowed_files。
完成前运行 verification_commands。
```

## 6. 正常任务调用逻辑

```text
01_task/TASKS.md
  -> 02_context/CONTEXT_INDEX.md
  -> 03_file_scope/FILE_SCOPE_RULES.md
  -> 04_roles_review/ROLE_MATRIX.md
  -> 05_action_aci/ACI_TOOL_CONTRACTS.md
  -> 06_verification/VERIFICATION_MATRIX.md
  -> 08_memory_state/STATE.md
```

## 7. 失败任务调用逻辑

```text
06_verification/DEBUG_GUIDE.md
  -> 08_memory_state/FAILURE_LOG.md
  -> 04_roles_review/MODEL_ROUTING.md
  -> 07_risk_release/RISK_CONTROL.md
```

失败时不要盲目重试。先分类，再决定 retry、escalate 或 block。

## 8. 高风险任务调用逻辑

```text
03_file_scope/HIGH_RISK_FILES.md
  -> 07_risk_release/RISK_CONTROL.md
  -> 04_roles_review/REVIEW_MATRIX.md
  -> 07_risk_release/templates/manual_approval.md
```

release、signing、upload、production Firebase、privacy 权限都属于高风险。

## 9. 每层教学法

学员不要一次学完所有文件。按层练：

1. 00_goal：写产品目标。
2. 01_task：写任务卡。
3. 02_context：列出该读什么。
4. 03_file_scope：列出能改什么。
5. 04_roles_review：判断谁 review。
6. 05_action_aci：用 view/search/safe_edit/run。
7. 06_verification：跑验证。
8. 07_risk_release：判断是否升级。
9. 08_memory_state：记录状态和失败。

## 10. 判断学会的标准

学员能做到以下事情，才算真正会用：

- 解释每个 layer 的职责。
- 写一个合格 task card。
- 正确区分 allowed/read-only/forbidden。
- 从 CALL_GRAPH 走完整任务流程。
- 为 Flutter/Swift/Firebase/release 任务选择不同验证。
- 失败时写 FAILURE_LOG 而不是盲改。
- 知道 release_blocking 必须人工批准。

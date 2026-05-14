# Full Tutorial: 如何从 0 使用 iOS App Development Harness

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

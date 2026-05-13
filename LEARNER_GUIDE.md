# Learner Guide: 从 0 开始使用 Research Cleaning Harness 与 Lightweight iOS App Harness

这份文档面向第一次接触这套项目的学员。目标不是让你背诵五个框架，而是让你能够：

- 看懂这套 harness 为什么这样设计。
- 从 clean data 中追溯每条规则的来源。
- 用 `generated/ios_app_harness/` 管住一个真实 iOS/Flutter 项目的 agent 工作流。
- 知道什么时候该停在 v0.1 文档规则，什么时候可以进入 v0.5 脚本化，什么时候才考虑 v1.0 runtime。

## 0. 先建立正确心智模型

这不是一个“自动写 iOS App 的魔法工具”。它是一套让 Codex 或其他 coding agent 在 iOS 项目里稳定工作的轻量操作系统。

核心思想：

```text
raw research files
-> Source Cards
-> mechanism records
-> framework summaries
-> fused lightweight iOS harness
-> real iOS repo task execution
```

你应该把它理解成两层。

第一层是研究清洗层：

```text
research_cleaning_harness/
  SOURCE_INVENTORY.md
  output/source_cards/
  output/data/source_cards.jsonl
  output/data/mechanisms.jsonl
  output/frameworks/
  output/mechanisms/
  output/failure_modes/
  output/ios_harness_mapping/
```

这一层回答：

```text
我们从五个框架中到底抽取了什么？
每个结论来自哪个文件？
每个机制解决什么失败模式？
每个机制应该落到 iOS Harness 的哪个文件？
```

第二层是实际使用层：

```text
generated/ios_app_harness/
  README.md
  AGENTS.md
  TASKS.md
  STATE.md
  CONTEXT_INDEX.md
  CONTEXT_RULES.md
  FILE_SCOPE_RULES.md
  ROLE_MATRIX.md
  REVIEW_MATRIX.md
  RISK_CONTROL.md
  VERIFICATION_MATRIX.md
  docs/agent/
  scripts/agent/
  templates/
  data/
```

这一层回答：

```text
当我真的要让 agent 改一个 iOS 项目时，agent 应该读什么？
可以改什么文件？
谁负责 review？
跑哪些测试？
失败了如何恢复？
什么时候必须人工确认？
```

## 1. 五个框架各自贡献什么

不要把五个框架混成一锅。它们在这套 harness 里各自负责不同层。

| framework | 主要贡献 | 在 harness 中的落点 |
|---|---|---|
| Superpowers | 工程纪律：planning、TDD、debugging、review、completion verification | `AGENTS.md`, `docs/agent/TESTING_GUIDE.md`, `docs/agent/DEBUG_GUIDE.md` |
| GSD2 | 状态管理、任务状态机、失败恢复、模型路由 | `STATE.md`, `TASKS.md`, `FAILURE_LOG.md`, `MODEL_ROUTING.md` |
| Aider | repo context、明确文件范围、read-only context、Git/验证闭环 | `CONTEXT_INDEX.md`, `FILE_SCOPE_RULES.md`, `GIT_WORKFLOW.md` |
| gstack | 角色治理、review matrix、workflow、risk/blocking rights | `ROLE_MATRIX.md`, `REVIEW_MATRIX.md`, `RISK_CONTROL.md` |
| SWE-agent | ACI tools、action/observation、safe command、trajectory/replay | `docs/agent/ACI_TOOL_CONTRACTS.md`, `scripts/agent/`, `data/mechanism_targets.jsonl` |

一句话：

```text
Superpowers 管工程习惯
GSD2 管状态和恢复
Aider 管 repo 上下文和文件范围
gstack 管角色和审查
SWE-agent 管工具执行接口
```

## 2. 从 0 克隆和验证

先拿到项目：

```bash
git clone git@github.com:Xaxrich/research-cleaning-harness.git
cd research-cleaning-harness
```

如果你没有 SSH 权限，也可以用 HTTPS：

```bash
git clone https://github.com/Xaxrich/research-cleaning-harness.git
cd research-cleaning-harness
```

先不要改任何文件。先验证项目是否完整：

```bash
python3 generated/ios_app_harness/scripts/validate_harness.py
python3 scripts/validate_source_cards.py
python3 scripts/validate_yaml.py
python3 scripts/validate_clean_data.py
python3 -m unittest discover tests
```

你应该看到类似结果：

```text
validated ios_app_harness, failures: 0
validated 134 source card(s), failures: 0
validated 1 yaml file(s), failures: 0
validated clean data, failures: 0
Ran 14 tests ... OK
```

如果验证不通过，不要继续做合成或应用。先修验证问题。

## 3. 第一次应该读哪些文件

新学员按这个顺序读，效率最高。

第一组：了解项目状态。

```text
README.md
PROGRESS.md
STATE.md
VALIDATION_LOG.md
```

第二组：理解 clean data。

```text
SOURCE_INVENTORY.md
output/data/source_cards.jsonl
output/data/mechanisms.jsonl
output/ios_harness_mapping/coverage_matrix.md
output/ios_harness_mapping/source_to_harness_trace.md
```

第三组：开始使用轻量 harness。

```text
generated/ios_app_harness/README.md
generated/ios_app_harness/AGENTS.md
generated/ios_app_harness/TASKS.md
generated/ios_app_harness/CONTEXT_INDEX.md
generated/ios_app_harness/FILE_SCOPE_RULES.md
generated/ios_app_harness/VERIFICATION_MATRIX.md
generated/ios_app_harness/RISK_CONTROL.md
```

第四组：需要深入时再读。

```text
output/frameworks/
output/mechanisms/
output/failure_modes/
output/source_cards/<framework>/
```

默认不要回读 raw。这个公开仓库也没有发布 raw。raw 是证据矿石，不是日常 agent 工作上下文。

## 4. 如何“榨干”数据而不是只看总结

这套项目的关键不是有一份总结，而是每条 harness 规则都能追溯到 clean source。

最重要的两个文件：

```text
generated/ios_app_harness/data/source_to_harness_trace.jsonl
generated/ios_app_harness/data/mechanism_targets.jsonl
```

如果你想知道“某个 Source Card 被用到了哪里”，看：

```bash
python3 - <<'PY'
import json
from pathlib import Path

path = Path("generated/ios_app_harness/data/source_to_harness_trace.jsonl")
for line in path.read_text(encoding="utf-8").splitlines():
    row = json.loads(line)
    if row["source_id"] == "F_SWE_023":
        print(json.dumps(row, ensure_ascii=False, indent=2))
PY
```

如果你想知道“某个 harness 文件背后有哪些机制”，看：

```bash
python3 - <<'PY'
import json
from pathlib import Path

target = "VERIFICATION_MATRIX.md"
path = Path("generated/ios_app_harness/data/mechanism_targets.jsonl")
for line in path.read_text(encoding="utf-8").splitlines():
    row = json.loads(line)
    if row["harness_file"] == target:
        print(row["mechanism_id"], row["source_framework"], row["source_file_id"], row["mechanism_name"])
PY
```

如果你想用人类可读的方式审计覆盖，看：

```text
output/ios_harness_mapping/source_to_harness_trace.md
output/ios_harness_mapping/file_placement_map.md
```

学习重点：

```text
不要问“这条规则我喜不喜欢”
要问“这条规则来自哪些 Source Card，解决什么 failure mode，落在哪个 harness 文件”
```

## 5. 把 generated harness 用到真实 iOS 项目

推荐先用 sidecar 模式，不要一上来把所有文件散落到真实 app repo 根目录。

假设你的真实项目是：

```text
my-ios-app/
  ios/
  lib/
  test/
  pubspec.yaml
```

建议复制为：

```text
my-ios-app/
  agent_harness/
    README.md
    AGENTS.md
    TASKS.md
    STATE.md
    CONTEXT_INDEX.md
    FILE_SCOPE_RULES.md
    VERIFICATION_MATRIX.md
    RISK_CONTROL.md
    ...
```

复制命令示例：

```bash
cp -R generated/ios_app_harness ../my-ios-app/agent_harness
cd ../my-ios-app
```

然后先做项目适配：

```text
agent_harness/PRODUCT_SPEC.md
agent_harness/CONTEXT_INDEX.md
agent_harness/FILE_SCOPE_RULES.md
agent_harness/VERIFICATION_MATRIX.md
agent_harness/IOS_RELEASE_CHECKLIST.md
```

必须改的内容：

| 文件 | 需要适配什么 |
|---|---|
| `PRODUCT_SPEC.md` | 你的 app 是什么、用户是谁、核心功能是什么 |
| `CONTEXT_INDEX.md` | 你的 Flutter/iOS/Firebase 目录和规范文件 |
| `FILE_SCOPE_RULES.md` | 哪些文件可编辑、只读、禁止 |
| `VERIFICATION_MATRIX.md` | 你的项目真实可跑的命令 |
| `IOS_RELEASE_CHECKLIST.md` | 你的发布流程、签名、隐私要求 |

不要立刻启用自动脚本改文件。先让 docs-first v0.1 跑通。

## 6. 第一个任务：从 docs-only 开始

新学员的第一个任务不要直接改业务代码。建议做一个 docs-only 任务，熟悉 harness 流程。

在真实项目的 `agent_harness/TASKS.md` 里添加：

```yaml
task_id: TASK-001
status: ready
task_type: docs
owner_role: orchestrator
risk_level: low
goal: Fill PRODUCT_SPEC.md with the actual iOS app purpose, audience, and non-goals.
allowed_files:
  - agent_harness/PRODUCT_SPEC.md
read_only_files:
  - README.md
  - pubspec.yaml
  - ios/Runner/Info.plist
forbidden_files:
  - .env*
  - ios/**/*.mobileprovision
  - ios/**/*.p12
required_context:
  - agent_harness/STATE.md
  - agent_harness/TASKS.md
  - agent_harness/CONTEXT_INDEX.md
verification_commands:
  - git diff -- agent_harness/PRODUCT_SPEC.md
completion_evidence: []
rollback_plan: revert PRODUCT_SPEC.md changes
```

然后给 Codex 的工作提示可以这样写：

```text
你现在在一个 iOS app repo 中工作，请使用 agent_harness。

当前任务是 TASK-001。

必须先读：
- agent_harness/STATE.md
- agent_harness/TASKS.md
- agent_harness/CONTEXT_INDEX.md
- agent_harness/FILE_SCOPE_RULES.md
- agent_harness/VERIFICATION_MATRIX.md

只允许修改 TASK-001 的 allowed_files。
完成前运行 verification_commands，并更新 STATE.md。
不要读取 raw research。
```

完成后，你要检查三件事：

```text
1. 是否只改了 allowed_files
2. 是否有验证证据
3. 是否更新了 STATE.md 或任务状态
```

## 7. 第二个任务：小范围 Flutter UI 改动

熟悉 docs-only 后，再做一个低风险 Flutter UI 任务。

任务卡示例：

```yaml
task_id: TASK-002
status: ready
task_type: flutter_ui
owner_role: flutter_ui
risk_level: low
goal: Adjust the empty-state copy on the home screen.
allowed_files:
  - lib/features/home/home_empty_state.dart
  - test/features/home/home_empty_state_test.dart
read_only_files:
  - agent_harness/PRODUCT_SPEC.md
  - agent_harness/CONTEXT_INDEX.md
  - pubspec.yaml
forbidden_files:
  - ios/
  - firebase*
  - .env*
required_context:
  - agent_harness/FILE_SCOPE_RULES.md
  - agent_harness/VERIFICATION_MATRIX.md
  - agent_harness/docs/agent/TESTING_GUIDE.md
required_tools:
  - search_code
  - view_file
  - safe_edit_check
verification_commands:
  - flutter analyze
  - flutter test test/features/home/home_empty_state_test.dart
rollback_plan: revert the two allowed files
```

执行原则：

- 先搜索，不要直接打开一堆文件。
- 编辑前先 view 目标区域。
- 只改 allowed files。
- 测试失败写 `FAILURE_LOG.md`，不要反复盲改。
- 完成回答必须写明跑过哪些命令。

## 8. 日常使用流程

每个任务都按这 9 步走。

1. 定义任务。
2. 判断 task type 和 risk level。
3. 写 allowed/read-only/forbidden files。
4. 按 `CONTEXT_INDEX.md` 组装上下文。
5. 按 `ROLE_MATRIX.md` 选择 owner role。
6. 按 `RISK_CONTROL.md` 判断是否需要人工确认。
7. 执行最小改动。
8. 按 `VERIFICATION_MATRIX.md` 验证。
9. 更新 `STATE.md`、`TASKS.md`、`FAILURE_LOG.md`、Git evidence。

对应文件：

| 步骤 | 看哪个文件 |
|---|---|
| 定义任务 | `TASKS.md`, `templates/task_card.md` |
| 上下文 | `CONTEXT_INDEX.md`, `CONTEXT_RULES.md` |
| 文件范围 | `FILE_SCOPE_RULES.md`, `HIGH_RISK_FILES.md` |
| 角色 | `ROLE_MATRIX.md`, `REVIEW_MATRIX.md` |
| 风险 | `RISK_CONTROL.md`, `IOS_RELEASE_CHECKLIST.md` |
| 验证 | `VERIFICATION_MATRIX.md`, `docs/agent/TESTING_GUIDE.md` |
| 失败恢复 | `FAILURE_LOG.md`, `docs/agent/DEBUG_GUIDE.md` |
| 工具契约 | `docs/agent/ACI_TOOL_CONTRACTS.md` |

## 9. 如何选择风险等级

低风险：

```text
docs-only
小范围 UI 文案
测试文件补充
非发布路径的轻微样式调整
```

中风险：

```text
多文件 UI 改动
状态管理改动
依赖版本变更
网络请求逻辑
数据模型变化
```

高风险：

```text
Firebase rules
iOS native bridge
Info.plist / entitlements
权限、隐私、登录、支付
Crashlytics / Analytics 配置
```

release_blocking：

```text
签名证书
provisioning profile
App Store upload
TestFlight 发布
生产 Firebase 或线上数据
```

高风险和 release_blocking 默认要 review 或人工确认。

## 10. 如何使用 scripts/agent

v0.1 里脚本是辅助工具，不是强制 runtime。

可用脚本：

```text
scripts/agent/view_file.sh
scripts/agent/search_code.sh
scripts/agent/safe_edit_check.sh
scripts/agent/run_safe_command.sh
scripts/agent/context_pack.sh
```

示例：

```bash
agent_harness/scripts/agent/search_code.sh "HomeEmptyState" lib
agent_harness/scripts/agent/view_file.sh lib/features/home/home_empty_state.dart 1 120
agent_harness/scripts/agent/safe_edit_check.sh lib/features/home/home_empty_state.dart
agent_harness/scripts/agent/run_safe_command.sh flutter analyze
```

注意：

- `safe_edit_check.sh` 只能做基础风险提示，不能替代人工判断。
- `run_safe_command.sh` 只 allowlist 一些安全命令，遇到 release/upload 会要求确认。
- 真正的 v1.0 runtime enforcement 还没有实现。

## 11. 如何读 framework summaries

如果你想理解某个框架如何影响 harness，读：

```text
output/frameworks/superpowers_summary.md
output/frameworks/gsd2_summary.md
output/frameworks/aider_summary.md
output/frameworks/gstack_summary.md
output/frameworks/swe_agent_summary.md
```

建议顺序：

1. `superpowers_summary.md`：理解工程纪律。
2. `aider_summary.md`：理解文件范围和 repo context。
3. `gsd2_summary.md`：理解状态和恢复。
4. `gstack_summary.md`：理解角色和 review。
5. `swe_agent_summary.md`：理解 ACI tools。

读的时候不要只看结论，要看 `Source Coverage` 和 `Evidence Pull`。

## 12. 如何读 mechanism docs

如果你关心“机制”，而不是框架来源，读：

```text
output/mechanisms/skills_and_process.md
output/mechanisms/task_state_machine.md
output/mechanisms/agent_roles.md
output/mechanisms/repo_context.md
output/mechanisms/aci_tools.md
output/mechanisms/verification.md
output/mechanisms/risk_gate.md
```

这些文件回答：

```text
一个 iOS agent harness 到底需要哪些机制？
每个机制由哪些框架共同贡献？
应该落到哪些 harness 文件？
```

## 13. 如何读 failure modes

如果你关心“这套系统防什么错”，读：

```text
output/failure_modes/
```

重点文件：

```text
context_pollution.md
wrong_file_edit.md
no_test_completion.md
stuck_loop.md
release_risk.md
weak_model_overreach.md
privacy_leak 相关内容在 risk/privacy 文件中体现
```

学习方法：

```text
先读 failure mode
再看 primary guard files
再回到 generated/ios_app_harness 对应文件
```

这样你会知道每条规则不是为了好看，而是为了防具体失败。

## 14. 什么时候看 Source Card

日常使用不需要总看 Source Card。只有这些场景需要看：

```text
1. 你怀疑某条 harness 规则过度推断
2. 你要修改某个机制
3. 你要向别人解释这条规则来源
4. 你要合并新的框架或新研究
```

Source Card 路径：

```text
output/source_cards/superpowers/
output/source_cards/gsd2/
output/source_cards/aider/
output/source_cards/gstack/
output/source_cards/swe-agent/
```

Source Card 里最重要的段落：

```text
4. Core Mechanisms Extracted
5. Failure Modes Addressed
8. Evidence Snippets
9. iOS Harness Mapping
10. Transfer Decision
11. Uncertainties
13. Clean Summary for Codex
```

## 15. 学员 7 天训练路线

Day 1：理解项目结构。

- 读 `README.md`
- 读 `generated/ios_app_harness/README.md`
- 跑所有 validation
- 解释五个框架各自贡献

Day 2：理解 trace。

- 读 `source_to_harness_trace.md`
- 找 3 个 Source Card，追踪它们落到哪些 harness 文件
- 找 3 个 harness 文件，反查它们由哪些机制支持

Day 3：理解 task discipline。

- 读 `TASKS.md`
- 读 `FILE_SCOPE_RULES.md`
- 写一个 docs-only task card

Day 4：理解 verification。

- 读 `VERIFICATION_MATRIX.md`
- 读 `docs/agent/TESTING_GUIDE.md`
- 为一个 Flutter UI task 写验证命令

Day 5：理解 risk/review。

- 读 `ROLE_MATRIX.md`
- 读 `REVIEW_MATRIX.md`
- 读 `RISK_CONTROL.md`
- 判断 5 个任务的风险等级

Day 6：接入真实 repo。

- 把 `generated/ios_app_harness/` 复制到真实项目的 `agent_harness/`
- 改 `PRODUCT_SPEC.md`
- 改 `CONTEXT_INDEX.md`
- 改 `VERIFICATION_MATRIX.md`

Day 7：完成一个真实小任务。

- 选一个低风险 docs 或 Flutter UI 任务
- 写 task card
- 执行
- 验证
- 写 completion evidence

## 16. 常见错误

错误 1：直接让 agent 读所有文件。

正确做法：

```text
按 CONTEXT_INDEX.md 只读必要上下文。
```

错误 2：没有 allowed_files 就开始改。

正确做法：

```text
每个任务必须先写 allowed/read-only/forbidden files。
```

错误 3：测试失败后盲目重试。

正确做法：

```text
先写 FAILURE_LOG.md，再分类失败，再决定下一步。
```

错误 4：把 v0.5/v1.0 当成已经实现。

正确做法：

```text
v0.1 是文档规则。
v0.5 是脚本辅助。
v1.0 才是 runtime enforcement。
```

错误 5：把 raw research 当日常上下文。

正确做法：

```text
默认读 clean outputs。只有证据缺失时才考虑 raw。
```

错误 6：发布相关任务没有人工确认。

正确做法：

```text
release/signing/upload 永远走 manual approval。
```

## 17. 如何让 Codex 使用这套 harness

给 Codex 的推荐总控 prompt：

```text
你现在在一个 iOS app repo 中工作，必须使用 agent_harness。

每个任务必须遵守：
1. 先读 agent_harness/STATE.md 和当前 task card。
2. 只读取 CONTEXT_INDEX.md 允许的上下文。
3. 只修改 allowed_files。
4. read_only_files 只能读，不能改。
5. forbidden_files 不能读也不能改，除非我明确批准。
6. 编辑前先查看目标区域。
7. 完成前按 VERIFICATION_MATRIX.md 跑验证。
8. 失败必须记录 FAILURE_LOG.md。
9. 不要声称完成，除非有验证证据。

当前任务是：<task_id>
```

review prompt：

```text
请按 agent_harness/REVIEW_MATRIX.md review 当前 diff。

优先找：
- wrong_file_edit
- missing verification
- context pollution
- release/privacy/security risk
- weak model overreach
- rollback gap

输出 findings first，按严重程度排序。
```

debug prompt：

```text
当前任务验证失败。

请先读：
- agent_harness/FAILURE_LOG.md
- agent_harness/docs/agent/DEBUG_GUIDE.md
- 失败命令输出

不要直接修。
先分类 failure mode，提出最小验证假设，再做一处修改。
```

## 18. 如何维护和升级这套 harness

### 修改 v0.1 文档

当你发现某条规则不适合真实项目，不要直接删。先做三件事：

```text
1. 找到对应 harness 文件
2. 在 source_to_harness_trace 中找到来源 Source Card
3. 判断是迁移不适配，还是真实项目有特殊约束
```

然后在 `DECISIONS.md` 记录：

```md
## D-XXX: <decision title>

Decision:

Reason:

Source trace:

Implication:
```

### 进入 v0.5

只有当 v0.1 文档规则在真实任务中跑通，才进入 v0.5。

v0.5 可以做：

```text
context_pack.sh 更智能
safe_edit_check.sh 接入真实 allowed_files
run_safe_command.sh 接入项目测试命令
trajectory.jsonl 自动记录
verification evidence 自动写入
```

不要一开始就做 runtime。

### 进入 v1.0

v1.0 才考虑：

```text
强制文件编辑拦截
命令权限系统
trajectory replay
CI gate
agent runtime / worker lease
自动模型路由
```

进入 v1.0 的条件：

```text
1. v0.1 已在多个真实任务跑通
2. v0.5 脚本有测试
3. 高风险路径有人工审批机制
4. release/privacy/security 的边界清楚
```

## 19. 如何加入新的研究资料

如果以后你要继续研究新框架，不要直接改 generated harness。

正确流程：

```text
1. 把 raw 资料放到 raw/ 或本地 evidence 目录
2. 更新 SOURCE_INVENTORY.md
3. 每个 raw 文件生成一张 Source Card
4. review Source Card
5. 更新 output/data/source_cards.jsonl
6. 更新 output/data/mechanisms.jsonl
7. 重新生成 summaries / mechanisms / harness mapping
8. 运行 validators
9. 再生成 generated/ios_app_harness
```

原则：

```text
raw 不直接影响 harness
Source Card 才能影响 harness
reviewed Source Card 才能进入 synthesis
```

## 20. 学员完成标准

一个学员算真正会用这套 harness，不是看他读了多少文档，而是看他能不能完成下面 8 件事：

1. 跑通所有 validation。
2. 解释五个框架各自贡献。
3. 从一个 Source Card 追踪到 harness 文件。
4. 从一个 harness 文件反查到 Source Card。
5. 写一个合格 task card。
6. 正确区分 allowed/read-only/forbidden files。
7. 为一个 iOS 任务选择合理 verification commands。
8. 完成一个低风险真实任务，并留下状态、验证和 Git evidence。

## 21. 最短使用路径

如果你只想最快开始，用这个顺序：

```bash
git clone https://github.com/Xaxrich/research-cleaning-harness.git
cd research-cleaning-harness
python3 generated/ios_app_harness/scripts/validate_harness.py
cp -R generated/ios_app_harness ../my-ios-app/agent_harness
cd ../my-ios-app
```

然后：

```text
1. 改 agent_harness/PRODUCT_SPEC.md
2. 改 agent_harness/CONTEXT_INDEX.md
3. 改 agent_harness/VERIFICATION_MATRIX.md
4. 写 TASK-001 docs-only task
5. 让 Codex 按 AGENTS.md 执行
```

不要跳过 task card。不要跳过 file scope。不要跳过 verification。

这三件事是这套 harness 的底线。

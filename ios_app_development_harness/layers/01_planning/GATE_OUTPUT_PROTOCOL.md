# GATE OUTPUT PROTOCOL

Purpose: make each harness interaction feel like a clear Chinese checkpoint instead of an internal status dump.

The agent must use this protocol whenever it asks the user to confirm product, plan, task breakdown, verification strategy, acceptance, waiver, or high-risk action.

## Core Rule（核心规则）

User-facing gate replies must be written in Chinese by default. Keep file paths, commands, code identifiers, and internal status values in monospace when needed, but do not expose English field labels such as `Gate`, `Stage`, `Status`, `Review document`, `Decision record target`, `What is being confirmed`, or `Decision needed`.

One response may ask for exactly one user action.
When a user action is required, put it in the final block of the response.

Allowed user actions:

- answer one blocking question
- confirm one gate
- request changes to one gate
- waive one verification or risk gate
- approve one high-risk action

Do not ask the user to confirm a gate while also saying there are unresolved decisions inside that same gate.

Do not lead with the requested decision. First give the user the gate status and the evidence needed to understand the decision. End with the decision request.

Every confirmation request must make the navigation obvious:

- 当前阶段
- 你要看的文档
- 回答后会写入的文档
- 本次确认什么

## Gate States（内部状态值）

Use these states consistently inside documents:

```text
not_started
collecting_input
draft_ready
needs_user_decision
needs_user_confirmation
changes_requested
confirmed
blocked
waived_by_user
```

When speaking to the user, translate the meaning:

| internal state | user-facing wording |
|---|---|
| `collecting_input` | 正在收集信息 |
| `draft_ready` | 草稿已就绪 |
| `needs_user_decision` | 需要你做一个决定 |
| `needs_user_confirmation` | 需要你确认 |
| `changes_requested` | 需要修改 |
| `confirmed` | 已确认 |
| `blocked` | 被阻塞 |

## Required Response Shape（用户可见模板）

Use this Chinese shape for every gate response:

```markdown
## 当前门禁：<中文门禁名>
当前阶段：<中文阶段名，必要时附层级，例如 00_goal / 开发前最小确认>
当前状态：<中文状态，可在括号里保留内部状态值>

本次要解决：<一句话说明这次只解决什么>

你要看的文档：`<path>`
回答后会写入：`<path>`
本次确认什么：<具体字段、规则或章节>

### 已经确定
- <只写已经确定的事实>

### 还卡住什么
- <只写当前唯一阻塞点；没有就写“无”>

### 本次不处理
- <明确哪些内容不会在本轮决定，避免混在一起>

### 文件变动
- <文件路径或“无”>

### 验证
- <命令与结果，或“未运行：原因”>

### 确认后下一步
- <用户回答后 agent 会做什么>

## 需要你决定
请只做一件事：<一个问题或一个确认请求。必须写清楚文档路径和要确认的具体项。>
```

If there is no file update, write `无`.
If there is no verification, write `未运行：<reason>`.

If no user decision is needed, omit `## 需要你决定` and end with:

```markdown
## 下一步
- 
```

Do not put any additional sections after `## 需要你决定`.

## Confirmation Rules（确认规则）

### Product Brief Gate

Ask for `confirmed` only when:

- product problem is clear
- MVP scope is clear
- non-goals are clear
- privacy/data boundary is clear
- platform assumptions are clear
- no open item is marked as blocking

If any of those are unresolved, ask one blocking question instead of asking for confirmation.

### Solution Plan Gate

Ask for confirmation only when:

- architecture is selected
- module order is listed
- verification level is mapped per module
- risk and review gates are explicit
- alternatives are summarized

### Task Breakdown Gate

Ask for confirmation only when every proposed task has:

- dependency
- allowed files
- read-only files
- forbidden files
- acceptance criteria
- verification level
- simulator/device requirement

## Anti-patterns（反例）

Do not write:

```text
还有两个问题没定。请回复 confirmed。
```

Do write:

```text
## 当前门禁：需求澄清
当前阶段：开发前最小确认（00_goal）
当前状态：需要你做一个决定（needs_user_decision）

本次要解决：确定跨日打卡应该归属到哪一天。

你要看的文档：`layers/00_goal/DISCOVERY_GATE.md`
回答后会写入：`layers/00_goal/MVP_APP_BRIEF.md`
本次确认什么：跨日班次的日期归属规则。

### 已经确定
- “补偿节点”只是用户自定义名称和日期的个人里程碑。
- 产品不计算赔偿金、不承诺 N+1、不提供法律判断。

### 还卡住什么
- 上班和下班跨自然日时，今日工时、连续天数、月统计应该按哪一天计算。

### 本次不处理
- Flutter 架构、Firebase 范围、通知策略、任务卡拆分。

### 文件变动
- 无

### 验证
- 未运行：本轮只是需求确认，还没有改文件。

### 确认后下一步
- 把跨日规则写入 `layers/00_goal/MVP_APP_BRIEF.md`，再继续产品简报确认。

## 需要你决定
请只回复 A / B / C / D：A. 归属到上班打卡日期；B. 归属到下班打卡日期；C. 拆成两天不完整记录；D. 其他规则，并用一句话说明。
```

Do not combine:

- product brief confirmation and solution planning
- solution planning and task creation
- task completion and next task confirmation
- validation output and an unrelated product decision

## Status Report Placement（信息顺序）

Files changed and validation results are evidence. Put them before the final `## 需要你决定` block.

The first three visible lines must tell the user:

1. 当前门禁
2. 当前阶段
3. 当前状态

Before evidence sections, the response must tell the user:

- 你要看的文档
- 回答后会写入的文档
- 本次确认什么

The final block must tell the user what one thing they need to answer and repeat the relevant document path when the path matters.

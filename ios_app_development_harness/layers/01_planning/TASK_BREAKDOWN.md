# TASK BREAKDOWN

Use this file to convert a confirmed solution plan into executable task cards.

## Principles

- One task should change one coherent module or behavior.
- A task must define exact `allowed_files`, `read_only_files`, and `forbidden_files`.
- A task must name its verification level.
- A task should produce a user-reviewable result.
- Do not batch unrelated UI, data, permissions, and release work into one task.

## Recommended Granularity

| module type | task size |
|---|---|
| product/docs | one decision or brief update |
| pure logic | one model, service, or algorithm |
| data/storage | one persistence path or migration |
| UI screen | one screen or one focused flow |
| permission/system API | one permission or integration boundary |
| release | one checklist stage |

## Output

Before editing `TASKS.md`, produce:

- module list
- task list
- dependency order
- acceptance criteria per task
- verification command per task
- whether simulator/device testing is required

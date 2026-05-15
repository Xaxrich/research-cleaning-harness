# Task Card: <task_id>

| Field | Value |
|---|---|
| status | ready |
| task_type | |
| module | |
| depends_on | |
| product_brief_status | draft \| needs_user_confirmation \| confirmed \| superseded |
| solution_plan_status | draft \| needs_user_confirmation \| confirmed \| superseded |
| user_confirmed_plan | true \| false |
| owner_role | |
| risk_level | |
| goal | |
| acceptance_criteria | |
| verification_level | diff \| unit \| build \| simulator \| device \| manual |
| simulator_required | true \| false |
| device_required | true \| false |
| review_required | true \| false |
| allowed_files | |
| read_only_files | |
| forbidden_files | |
| required_context | |
| verification_commands | |
| rollback_plan | |
| trace_file | |

## Done Definition

- Only `allowed_files` changed.
- Required verification level is met or explicitly blocked.
- Simulator/device evidence exists when required.
- Failures are recorded in `FAILURE_LOG.md`.
- Run trace is updated.
- `STATE.md` points to the next step.

## Work Log

| step | evidence |
|---|---|

## Completion Evidence

| command | result | notes |
|---|---|---|

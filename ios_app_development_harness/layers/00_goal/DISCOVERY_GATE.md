# DISCOVERY GATE

Purpose: prevent the agent from turning a raw idea into implementation too early.

Before writing or executing task cards, the agent must produce a discovery summary and ask the user to confirm it.

## Required Questions

The agent must clarify:

1. User and problem:
   - Who is the primary user?
   - What painful workflow or unmet need is being solved?
   - What does the user do today instead?

2. MVP scope:
   - What is the smallest useful product?
   - What must be excluded from the MVP?
   - Which workflow proves the product is valuable?

3. Platform and constraints:
   - Native SwiftUI, Flutter, React Native, or another stack?
   - iPhone only or iPad too?
   - Online-only, local-first, or cloud-backed?

4. Privacy and system permissions:
   - Does the app need location, contacts, camera, files, notifications, background execution, HealthKit, or other sensitive APIs?
   - What data must stay local?
   - What data must never be collected?

5. Success criteria:
   - What should be true after the first working build?
   - What should be testable in the simulator?
   - What evidence will convince the user that the module is done?

## Output

The agent must output:

- confirmed facts
- assumptions
- non-goals
- open questions
- risk notes
- proposed next gate

The output must follow `layers/01_planning/GATE_OUTPUT_PROTOCOL.md` when asking the user for a decision or confirmation.

## Blocking Rule

If material product assumptions are unresolved, do not create implementation task cards. Create only a discovery or documentation task.

If material assumptions are unresolved, do not ask the user to reply `confirmed`. Ask the next blocking question instead.

# SIMULATOR TEST POLICY

Simulator testing is required when a task changes user-visible iOS behavior.

## Required

Run simulator verification when a task changes:

- SwiftUI/UIKit screens
- navigation
- onboarding
- settings
- permission prompts
- local notification flows
- location simulation flows
- camera/photo/file picker flows where simulator support is sufficient
- any user-visible regression fix

## Not Required By Default

Simulator testing is not required for:

- documentation-only changes
- pure model or utility logic with unit tests
- scripts that do not affect app runtime
- release notes

## Evidence

Record at least one:

- simulator build and launch command
- XCUITest result
- screenshot path
- manual smoke checklist result
- explicit blocked reason

## Waiver

If simulator testing is skipped for a user-visible change, record:

- who waived it
- why it is acceptable
- what weaker verification was run
- residual risk

# Lab 00 — Bench-only ritual

**Goal:** prove the stack works without spinning props.

## Baseline

Use a whoop-class teaching rig similar to a BETAFPV Air65 with ELRS. This lab is still valid on other small FPV rigs, but the artifact standard stays the same.

## Required setup

- props removed before power
- Betaflight Configurator available
- assigned radio model identified
- screenshot or note-taking path ready
- `templates/air65-bench-proof-checklist.md` open

## Proof questions

Before touching settings, each student should be able to answer:

1. what is the control path?
2. what is the video path?
3. what does the craft do if the radio link disappears?

## Steps
1. Props off. Verify.
2. Power-up with current limiting / smoke stopper.
3. Connect to configurator; verify receiver channels move.
4. Verify failsafe.
5. Verify telemetry output exists and is parsable.
6. Save screenshots or config diff before disconnecting.

## Observe
- Values change when you move the radio sticks.
- Disarm state is unambiguous.
- No unexpected motor output.
- Link-loss behavior is not being guessed at.

## Why
Bench-first makes every later step safer and more debuggable.

## Artifact
- completed bench-proof checklist
- screenshot set + saved config diff
- one paragraph stating what is proven and what still needs proof

## Stop conditions

Pause and escalate if:

- the rig reports unexpected arming behavior
- receiver motion does not match stick motion
- signal-loss behavior is unclear
- any motor output happens while students are not intentionally testing it

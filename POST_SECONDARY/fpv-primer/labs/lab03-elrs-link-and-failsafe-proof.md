# Lab 03 — ELRS link and failsafe proof

**Goal:** prove that the Air65-class control path behaves predictably before any live-prop work.

## Required setup

- props removed
- correct radio model selected
- Betaflight Configurator connected
- `templates/air65-bench-proof-checklist.md` open

## Steps

1. Confirm the receiver protocol is set correctly for the rig.
2. Verify stick movement and AUX switch movement in the Receiver tab.
3. Confirm the intended arm path and any PREARM logic.
4. Observe a control-link health field such as link quality.
5. Perform a deliberate signal-loss test on the bench.
6. Record what the craft does when the link disappears.
7. Restore normal link state and confirm the system recovers as expected.

## Observe

- Betaflight receives the expected channels from the intended radio model.
- Link state is visible rather than assumed.
- Failsafe behavior matches the team’s written expectation.

## Why

Students regularly say "ELRS is bound" when what they mean is "the radio looked alive for a moment." This lab requires proof of the actual control path and its failure behavior.

## Artifact

- completed ELRS section of the bench-proof checklist
- screenshot set from Receiver, Modes, and Failsafe views
- one short written statement beginning with:
  - "When the control link disappeared, the craft..."

## Stop conditions

Do not advance to live-prop work if:

- channel motion is inconsistent
- students cannot explain the failsafe result they observed
- the control-link field and the student narrative disagree

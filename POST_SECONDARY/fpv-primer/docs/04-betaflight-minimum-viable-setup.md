# Betaflight: minimum viable setup (telemetry-first)

Goal: produce a stable, documented configuration that is safe enough to bench-prove and simple enough to log.

## 1. Firmware target and board orientation

Confirm:

- the FC target is correct
- Betaflight version is noted in the log
- board orientation matches physical build

Proof:

- Setup tab model moves in the same direction as the craft

## 2. Receiver setup

Use the Receiver tab to confirm:

- the receiver protocol is correct
- channel map matches the transmitter
- stick centers and endpoints are sane
- AUX switches move the intended channels

Conservative default:

- do not “fix” weird stick behavior in your head
- fix it in channel map or radio setup

## 3. Modes and arming

Minimum viable modes:

- ARM
- one beginner or stable mode if appropriate to the vehicle and teaching context
- optional PREARM if your workflow benefits from it

The point is not mode abundance. The point is predictable behavior.

## 4. Failsafe

Betaflight’s own guidance is clear: prove failsafe before flight.

For a first-pass bench-safe setup:

- configure flight-controller-based failsafe behavior
- make sure the receiver does not hide signal loss by sending fake-valid values
- test the signal-loss path intentionally on the bench

For racers and small park craft, “drop” behavior is common, but only after you have actually verified what the rig does.

## 5. Motor test

Props off.

Verify:

- correct motor order
- correct direction
- clean startup
- no rubbing or unexpected noise

Do not move on just because “something spun.”

## 6. Rates and expo

Keep rates conservative at first.

You are not trying to find the final tune here. You are trying to establish:

- predictable stick response
- repeatable comparison state
- a baseline you can return to

## 7. OSD

If video is part of the workflow, enable at least:

- warnings
- battery voltage
- timer
- link-quality or equivalent fields where supported

The OSD should help the pilot decide, not decorate the screen.

## 8. Logging

If the FC supports blackbox or another useful log path:

- enable it early
- note the storage medium
- record one short known-good file

Even when you are not “tuning” yet, a working log path matters.

## Minimum viable output artifact

Each setup pass should end with:

- a saved diff or full config export
- screenshots of key tabs:
  - Setup
  - Receiver
  - Modes
  - Failsafe
  - Motors
  - OSD or logging config if relevant
- one written note describing what was proven

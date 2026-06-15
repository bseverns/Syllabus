# Tiny Whoop Troubleshooting Decision Tree

Use this when a whoop is not ready to fly. Move slowly. Change one thing at a time.

## First Question

Is this a safety issue?

- Battery is puffy, hot, damaged, or smells strange: **ground it and tell the instructor.**
- Prop is cracked, badly bent, or rubbing: **bench-check before flight.**
- Frame, duct, antenna, camera, or battery lead is loose or damaged: **bench-check before flight.**
- Unknown behavior after a hard crash: **complete crash recovery before flight.**

## Will Not Connect to Betaflight

Check in this order:

1. Is the USB cable data-capable?
2. Is the USB connector seated correctly?
3. Does another cable or port work?
4. Is the correct port selected in Betaflight?
5. Does the flight controller power up by USB?
6. Is this a driver/permission issue on the computer?
7. Does the instructor need to inspect the board or firmware target?

While waiting: use VelociDrone, inspect props/frame, or update your tune log.

## Will Not Bind or Radio Does Not Talk

Check in this order:

1. Is the radio on and on the correct model memory?
2. Is the whoop powered correctly?
3. Is the receiver type known: ELRS, SPI, external receiver, or other?
4. Does the radio show link quality or telemetry?
5. Does the Receiver tab move when sticks move?
6. Is the channel map wrong?
7. Does the instructor need to run a hardware-specific bind process?

While waiting: complete simulator stick drills and write down which stick controls roll, pitch, yaw, and throttle.

## Wrong Stick Response

Check in this order:

1. Move one stick at a time in the Receiver tab.
2. Confirm roll, pitch, yaw, and throttle each move the correct bar.
3. Record the channel map.
4. Fix channel map only under instructor direction.
5. Re-test all sticks after any change.

Do not fly if throttle, roll, pitch, or yaw is mapped incorrectly.

## Will Not Arm

Check in this order:

1. Props off if on the bench.
2. Radio is on and linked.
3. ARM switch range is correct in Modes.
4. Flight mode is expected.
5. Throttle is low.
6. Quad is level and still.
7. Read arming flags or warnings.
8. Ask the instructor before changing unrelated settings.

Write down the arming flag:

```text

```

## Failsafe Is Not Verified

Do not proceed to real flight until the instructor verifies failsafe.

Check in this order:

1. Props off.
2. Instructor directs the signal-loss test.
3. Signal loss is detected.
4. Motors stop/drop behavior is correct.
5. Quad does not restart unexpectedly.

Student explanation:

```text
When the radio conversation goes silent, the whoop should...
```

## Flies Rough or Feels Wrong

Check in this order:

1. Props chipped, bent, loose, or installed wrong?
2. Hair, thread, carpet fiber, or tape in a motor?
3. Duct or frame cracked?
4. Battery weak, damaged, or sagging?
5. Camera angle shifted?
6. Correct rate profile active?
7. Did a setting change since the last good flight?

If unsure, stop flying and compare against the last saved backup or tune note.

## Video Issue

Check in this order:

1. Goggles or receiver powered?
2. Correct channel?
3. VTX powered?
4. Camera connected and aimed correctly?
5. Antenna attached and routed normally?
6. VTX power/channel set by class plan?

Do not raise VTX power casually. Ask the instructor.

## No Simulator Station Available

You are still learning. Choose one:

- Complete the Betaflight worksheet.
- Inspect your quad with the crash-recovery checklist.
- Update your tune log.
- Observe a pilot and record one control habit.
- Help run timing, scoring, or heat sheets.
- Coach a peer using the decision tree.

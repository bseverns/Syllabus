# Betaflight Configuration Worksheet

Use this worksheet during Weeks 1-5 whenever you connect a whoop to Betaflight.

**Student:** ___________________________

**Drone name / number:** ___________________________

**Radio model:** ___________________________

**Date:** ___________________________

## Safety Before Anything Else

- [ ] Props are removed.
- [ ] Battery is disconnected unless the instructor says otherwise.
- [ ] Radio is on.
- [ ] Arm switch is off.
- [ ] Workspace is clear.

Betaflight is where we make sure the machine tells the truth before we ask it to fly.

## 1. Backup

Before changing anything, save a backup.

Backup method used:

- [ ] Presets / Backup tab
- [ ] CLI `diff all`
- [ ] Other: ___________________________

| Item | Value |
| --- | --- |
| Backup saved? | Yes / No |
| Backup file name | |
| Backup location | |
| Firmware target, if visible | |
| Betaflight version, if visible | |

## 2. Setup Tab: Board Orientation

Place the whoop level on the table. Tilt it gently and watch the model.

| Test | Pass? | Notes |
| --- | --- | --- |
| Nose down = model nose down | [ ] | |
| Roll left = model rolls left | [ ] | |
| Yaw left/right looks correct | [ ] | |
| Board orientation looks correct | [ ] | |

Do not continue to real flight if the digital model does not match the real quad.

## 3. Ports / Receiver

Your receiver setup depends on your hardware.

| Item | Setting / Observation | Verified |
| --- | --- | --- |
| Receiver type | Serial / SPI / other: __________ | [ ] |
| Serial provider, if used | CRSF / SBUS / IBUS / other: __________ | [ ] |
| UART Serial RX, if used | UART _____ | [ ] |
| Radio link appears healthy | Yes / No | [ ] |

Notes:

```text

```

## 4. Receiver Tab: Sticks and Switches

Move one stick or switch at a time. The correct bar should move.

| Control | Correct channel moves? | Low | Center | High | Notes |
| --- | --- | --- | --- | --- | --- |
| Roll | [ ] | ~1000 | ~1500 | ~2000 | |
| Pitch | [ ] | ~1000 | ~1500 | ~2000 | |
| Yaw | [ ] | ~1000 | ~1500 | ~2000 | |
| Throttle | [ ] | ~1000 | n/a | ~2000 | |
| Arm switch | [ ] | ~1000 | n/a | ~2000 | |
| Flight mode switch | [ ] | | | | |
| Beeper or extra switch | [ ] | | | | |

Channel map: ___________________________

ARM channel / AUX: ___________________________

Mode channel / AUX: ___________________________

## 5. Modes Tab

| Mode | Switch / Channel | Range or Position | Verified |
| --- | --- | --- | --- |
| ARM | | | [ ] |
| ANGLE | | | [ ] |
| ACRO / AIR, if used | | | [ ] |
| BEEPER, if used | | | [ ] |
| FLIP OVER AFTER CRASH, if teacher-approved | | | [ ] |

My arm switch is: ___________________________

My beginner flight mode is: ___________________________

## 6. Failsafe: What Happens When the Radio Goes Silent?

Failsafe tells the quad what to do if the radio link is lost. For beginner indoor whoops, the expected behavior is usually:

```text
Signal lost = stop/drop/disarm quickly.
```

Test only with props off and only when the instructor directs the test.

| Failsafe checkpoint | Pass? | Notes |
| --- | --- | --- |
| Instructor approved test conditions | [ ] | |
| Props are off | [ ] | |
| Radio-off or signal-loss test observed | [ ] | |
| Signal loss is detected | [ ] | |
| Motors stop / drop behavior is correct | [ ] | |
| Quad does not restart unexpectedly | [ ] | |

In my own words, failsafe means:

```text

```

## 7. Motors Tab

Teacher-led only. Props off. Battery connected only when instructed.

| Motor | Correct motor spins? | Correct direction? | Notes |
| --- | --- | --- | --- |
| 1 | [ ] | [ ] | |
| 2 | [ ] | [ ] | |
| 3 | [ ] | [ ] | |
| 4 | [ ] | [ ] | |

Prop direction:

- [ ] Props in
- [ ] Props out
- [ ] Manufacturer default: ___________________________

## 8. Battery and OSD

| Item | Setting / Observation |
| --- | --- |
| Battery type | 1S LiPo / 1S LiHV / other: __________ |
| Warning voltage | |
| Minimum voltage | |
| Flight timer rule | |
| OSD voltage visible | Yes / No |
| OSD timer visible | Yes / No |
| OSD warnings visible | Yes / No |
| Flight mode visible, if used | Yes / No |

Class landing rule:

```text
Land at ______ minutes OR when low-voltage warning appears, whichever comes first.
```

## 9. Rates and Feel

| Profile | Purpose | Roll | Pitch | Yaw | Expo | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Gentle / practice | | | | | |
| 2 | Medium / responsive | | | | | |
| 3 | Advanced / optional | | | | | |

Preferred profile today: ___________________________

Why?

```text

```

## Instructor Signoff

- [ ] Backup saved
- [ ] Orientation verified
- [ ] Receiver verified
- [ ] Modes verified
- [ ] Failsafe verified
- [ ] Motors verified
- [ ] Battery/OSD readable
- [ ] Approved for next flight step

Instructor initials: ___________________________

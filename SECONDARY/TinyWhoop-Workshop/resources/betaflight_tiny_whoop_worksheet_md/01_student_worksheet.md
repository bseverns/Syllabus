# Betaflight Tiny Whoop Demo Worksheet

**Course:** Drone Course  
**Student:** ___________________________  
**Drone name / number:** ___________________________  
**Radio model:** ___________________________  
**Date:** ___________________________

## Big Safety Rule

**Props off. Battery only when instructed. Arm switch off.**

Betaflight is powerful. Tiny whoops are small, but they are still flying machines with spinning blades, batteries, radios, and software decisions that have real consequences.

Today’s goal:

> Make the drone tell the truth before we ask it to fly beautifully.

---

## Part 1 — Backup First

Before changing anything, save a backup.

Open the **CLI** tab and run:

```text
diff all
```

Copy and save the result.

Backup saved? ☐ Yes

File name:

```text
DroneNumber_StudentName_before_config.txt
```

Notes:

```text

```

---

## Part 2 — Setup Tab: Does the Digital Drone Match the Real Drone?

Place the whoop level on the table.

1. Click **Calibrate Accelerometer**.
2. Tilt the drone forward, back, left, and right.
3. Watch the 3D model.

The model should move the same way as the real drone.

| Test | Pass? | Notes |
|---|---:|---|
| Nose down = model nose down | ☐ | |
| Roll left = model rolls left | ☐ | |
| Yaw left/right looks correct | ☐ | |
| Board orientation correct | ☐ | |

**Do not continue until this is correct.**

---

## Part 3 — Ports / Receiver: Can the Radio Talk to the Drone?

Your receiver setup depends on your hardware.

Common modern tiny whoop setups include:

- **ExpressLRS over UART**
- **Built-in SPI receiver**
- Other receiver protocols depending on the board

| Item | Setting | Verified |
|---|---|---:|
| Receiver type | Serial / SPI / other: __________ | ☐ |
| Serial provider, if used | CRSF / SBUS / IBUS / other: __________ | ☐ |
| Correct UART Serial RX | UART _____ | ☐ |
| Telemetry | On / Off | ☐ |

Notes:

```text

```

---

## Part 4 — Receiver Tab: Do the Sticks Mean What They Say?

Move each stick and switch. Watch the bars.

| Control | Correct channel moves? | Low | Center | High |
|---|---:|---:|---:|---:|
| Roll | ☐ | ~1000 | ~1500 | ~2000 |
| Pitch | ☐ | ~1000 | ~1500 | ~2000 |
| Yaw | ☐ | ~1000 | ~1500 | ~2000 |
| Throttle | ☐ | ~1000 | — | ~2000 |
| Arm switch | ☐ | ~1000 | — | ~2000 |
| Flight mode switch | ☐ | | | |

**The throttle stick must move throttle. Roll must move roll. Pitch must move pitch. Yaw must move yaw.**

If the map is wrong, the drone becomes a small angry ceiling-seeking mythology object.

---

## Part 5 — Modes Tab: What Can the Pilot Ask the Drone To Do?

Recommended beginner tiny whoop modes:

| Mode | Setting | Verified |
|---|---|---:|
| ARM | AUX1, 2-position switch | ☐ |
| ANGLE | Beginner/self-level mode | ☐ |
| ACRO / AIR | Advanced mode, optional | ☐ |
| BEEPER | Find the whoop | ☐ |
| FLIP OVER AFTER CRASH | Optional, teacher-approved | ☐ |
| OSD PROFILE | Optional | ☐ |

My arm switch is: ___________________________

My flight mode switch is: ___________________________

---

## Part 6 — Failsafe: What Happens When the Radio Disappears?

For indoor tiny whoops, the beginner-safe default is usually:

> Signal lost = drop / disarm quickly.

Test with **props off**.

| Failsafe test | Pass? | Notes |
|---|---:|---|
| Signal loss detected | ☐ | |
| Motors stop / drop behavior | ☐ | |
| Drone recovers only when safe | ☐ | |

Notes:

```text

```

---

## Part 7 — Motors Tab: Do the Motors Match Reality?

**Props off. Battery connected only when the teacher says.**

Check:

1. Motor order
2. Motor direction
3. Prop direction

| Motor | Correct motor spins? | Correct direction? | Notes |
|---|---:|---:|---|
| 1 | ☐ | ☐ | |
| 2 | ☐ | ☐ | |
| 3 | ☐ | ☐ | |
| 4 | ☐ | ☐ | |

Class decision:

☐ Props in  
☐ Props out  
☐ Match manufacturer default

**Do not freestyle motor order or direction. This is not taste; this is gravity negotiation.**

---

## Part 8 — Power & Battery: When Should the Drone Come Home?

| Battery item | Setting / observation |
|---|---|
| Battery type | 1S LiPo / 1S LiHV / 2S / other |
| Max cell voltage | __________ |
| Warning voltage | __________ |
| Minimum voltage | __________ |
| OSD voltage visible | ☐ Yes / ☐ No |
| Flight timer visible | ☐ Yes / ☐ No |

Class rule:

```text
Land at ______ minutes OR when low-voltage warning appears, whichever comes first.
```

Notes:

```text

```

---

## Part 9 — OSD: What Does the Pilot Need To See?

Required:

☐ Battery voltage  
☐ Flight time  
☐ Warnings  
☐ Link quality / RSSI, if supported  
☐ Flight mode  
☐ Craft name or drone number  

Optional:

☐ Throttle position  
☐ Timer style  
☐ Crosshair  
☐ OSD layout  
☐ Pilot name / craft name  

My OSD design choices:

```text

```

---

## Part 10 — PID / Filters / Presets

For first flights, do not manually tune PID or filters.

Use one of these:

1. Manufacturer defaults for the exact whoop.
2. A known-good class `diff all`.
3. A carefully chosen preset approved by the teacher.

| Area | Teacher locked? | Student tunable? |
|---|---:|---:|
| PID profile | ☐ Yes | ☐ Later |
| Filter settings | ☐ Yes | ☐ Later |
| Dynamic idle | ☐ Yes | ☐ Later |
| RPM filtering | ☐ Yes | ☐ Later |
| Motor protocol | ☐ Yes | ☐ No beginner changes |
| Presets | ☐ Teacher only | ☐ Observe only |

---

## Part 11 — Rates: The Student Tuning Sandbox

Rates decide how stick movement becomes rotation speed.

Try three profiles:

### Profile 1 — Library Mouse

For first hover, gates, slow turns.

### Profile 2 — Hallway Fox

For students who can fly a square, figure-eight, and land intentionally.

### Profile 3 — Arcade Goblin

For confident pilots only.

| Test | Profile 1 | Profile 2 | Profile 3 |
|---|---:|---:|---:|
| Can hover in one tile? | ☐ | ☐ | ☐ |
| Can fly a square? | ☐ | ☐ | ☐ |
| Can fly a figure-eight? | ☐ | ☐ | ☐ |
| Can land on target? | ☐ | ☐ | ☐ |
| Feels too twitchy? | ☐ | ☐ | ☐ |
| Feels too sluggish? | ☐ | ☐ | ☐ |

Reflection:

```text
The drone felt twitchy when...

The drone felt slow when...

The setting I changed was...

The result was...

Next time I would...
```

# Teacher Guide: Betaflight Tiny Whoop Configuration Demo

## Course Goal

Every student should leave with a whoop that is:

- safe
- recoverable
- readable
- personally flyable

The class should understand this sequence:

1. Backup
2. Orientation
3. Receiver
4. Modes
5. Failsafe
6. Motors
7. Battery
8. OSD
9. Rates

The poetic version:

> First the machine must tell the truth. Then the pilot can teach it a voice.

---

## Settings Students Must Nail

These are teacher-verified and should not be improvised by beginner students.

| Category | Why it matters |
|---|---|
| Props off safety | Prevents injury and panic |
| Backup / `diff all` | Allows recovery |
| Board orientation | The drone’s sense of up must match reality |
| Receiver protocol | Radio must talk clearly to the flight controller |
| Channel map | Sticks must mean the right thing |
| ARM switch | Everyone needs the same emergency reflex |
| Failsafe | Lost signal must become safe behavior |
| Motor order | Flight controller commands must reach the correct motor |
| Motor direction | Wrong direction causes immediate chaos |
| Prop direction | Wrong props cause flips, skids, and ceiling impacts |
| Battery warning | Protects batteries and keeps flight predictable |
| VTX channel/power, if analog | Prevents students from stomping on each other’s video feeds |

---

## Settings Students Can Tune

These are good beginner tuning areas because they give students agency without risking the core safety of the aircraft.

| Category | Why it is good for learning |
|---|---|
| Rates | Direct connection between settings and feel |
| Expo / center sensitivity | Teaches precision vs responsiveness |
| Throttle limit or throttle curve | Makes power manageable |
| OSD layout | Builds cockpit awareness |
| Craft name | Ownership without risk |
| Angle vs Acro experience | Teaches control modes as different languages |
| Flight timer habit | Turns battery care into ritual |
| Beeper / crash recovery use | Practical field skill |

---

## Save for Advanced Students

| Category | Reason to wait |
|---|---|
| PID tuning | Easy to make worse without diagnosis |
| Filter tuning | Requires understanding noise, heat, and oscillation |
| Dynamic idle | Useful, but depends on ESC support and setup |
| RPM filtering | Powerful, but hardware/firmware dependent |
| ESC firmware changes | Too easy to create recovery work |
| CLI-only changes | Good later, dangerous early |
| Firmware flashing | Better as a separate recovery lab |

---

## Suggested 45–60 Minute Demo Flow

| Time | Activity |
|---:|---|
| 5 min | Safety ritual: props off, arm switch off, battery rules |
| 5 min | Connect to Betaflight App and save backup |
| 5 min | Setup tab: orientation and accelerometer |
| 10 min | Receiver tab: sticks, channel map, switches |
| 10 min | Modes: ARM, Angle, Acro, Beeper |
| 10 min | Motors tab: motor order/direction, teacher-led only |
| 5 min | Battery + OSD |
| 10 min | Student rate profile comparison |

---

## Teacher Defaults to Consider

These should be adapted to the exact tiny whoop model.

### Modes

- ARM on AUX1
- ANGLE mode available for beginners
- ACRO/AIR mode available only when appropriate
- BEEPER on a memorable switch
- FLIP OVER AFTER CRASH only after explicit safety discussion

### Battery

For 1S whoops, voltage sag is real. Teach students to use both:

- OSD voltage warning
- flight timer

Example classroom rule:

```text
Land at 2:30–3:00 minutes OR when low-voltage warning appears, whichever comes first.
```

### Rates

Use three named profiles:

- Library Mouse — slow, soft, stable
- Hallway Fox — medium, responsive, class progression
- Arcade Goblin — lively, advanced, earned through control

---

## Demo Language

Useful framing phrases:

- “We are not tuning performance yet. We are verifying truth.”
- “The arm switch is the emergency brake.”
- “Failsafe is what the drone does when the conversation with the radio goes silent.”
- “OSD is the pilot’s dashboard, not a decoration contest.”
- “Rates are where the drone’s personality begins.”
- “PID tuning is not a first-flight toy. It is a diagnosis tool.”

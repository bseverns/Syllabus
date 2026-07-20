# Week 08 — LED feedback as interface language

## Goals
- Make state legible without relying on color alone.
- Separate decorative animation from actionable feedback.
- Test whether a first-time user can interpret three states.

## Session arc (165 minutes)

1. Critique ambiguous status lights (15 min).
2. Define three states, meanings, and non-color cues (20 min).
3. Power-off wire three discrete LEDs with current-limiting resistors (30 min).
4. Flash `week08_led_feedback`; inspect pot-to-state thresholds (25 min).
5. Break and power-down reset (10 min).
6. Design/test steady, blink, label, or position cues (30 min).
7. Silent peer interpretation test and revision (25 min).
8. Save state table, evidence, and reflection (10 min).

## Minimum evidence

State/meaning/action table, safe wiring, observed state log, non-color cue, and peer interpretation note.

## Recovery

Use the three-discrete-LED baseline, onboard LED plus Serial labels, or a paper interface. NeoPixels are optional.

## Links
- Firmware: `firmware/week08_led_feedback/`
- Lab: `labs/week08_led_design.ipynb`
- HW: `assignments/hw08_leds.md`

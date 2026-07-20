# Final Build — Small Controller (12-week capstone)

## Brief
Build a small physical controller that feels playable:
- 4 knobs (analog)
- 4 buttons (digital)
- some form of feedback (LEDs or small display)
- a host-facing output (Serial required; MIDI optional)

## Requirements
- Non-blocking loop (millis-based timing)
- Debounced buttons
- Smoothed analog controls + deadband
- At least 2 modes (state machine)
- Document wiring + firmware so someone else can rebuild it

## Deliverables
- A 2–4 minute demo video (or live demo)
- Repo with:
  - `hardware/` wiring notes and photos
  - `firmware/` build sketch
  - `export/` CSV logs + at least one plot
  - a short `REPORT.md` explaining design decisions

Use `firmware/week12_controller/` as the Uno-compatible baseline, `hardware/WIRING_BASELINE.md` as the default pin plan, and `assignments/hw12_build.md` for the exact proof and handoff requirements. An approved two-knob/two-button reduction is complete when debounce, deadband, non-blocking scheduling, two modes, visible feedback, host messages, recovery testing, and documentation remain evident.

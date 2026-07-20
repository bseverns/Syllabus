# Week 12 — Integrated controller build and proof

## Goals
- Integrate four knobs, four buttons, three feedback states, and Serial output.
- Demonstrate debouncing, deadband, non-blocking behavior, and modes together.
- Produce rebuild, test, and recovery evidence.

## Session arc (165 minutes)

1. Freeze scope and run power/pin-budget review (15 min).
2. Build from known-good subsystems with power-off inspection gates (40 min).
3. Flash integrated baseline and prove one control at a time (25 min).
4. Break and power-down reset (10 min).
5. Run bench checklist, event log, mode and recovery tests (30 min).
6. Peer rebuild/documentation test or wiring-diagram audit (20 min).
7. Demo/critique with private or live option (15 min).
8. Final power-down, inventory, archive, and reflection (10 min).

## Minimum evidence

Pin/wiring map, compiled firmware, control/event log, two modes, visible feedback, failure/recovery test, rebuild notes, and final reflection.

## Recovery

A reduced two-knob/two-button controller can be complete when all required systems reasoning and evidence remain. Paper/recorded demonstration is available after hardware failure.

## Links
- Firmware: `firmware/week12_controller/`
- Lab: `labs/week12_build_week.ipynb`
- Project: `project/PROJECT_BRIEF.md`
- HW: `assignments/hw12_build.md`

# Week 09 — State machines and modes

## Goals
- Draw explicit states, events, transitions, and outputs.
- Build a mode button that changes behavior once per press.
- Make the current mode and recovery path visible.

## Session arc (165 minutes)

1. Act out a three-state machine with event cards (15 min).
2. Draw the supplied `IDLE / PLAY / CONFIG` transition table (20 min).
3. Reuse inspected button/pot/LED wiring; flash Week 9 (30 min).
4. Log transitions and try invalid/unexpected event sequences (25 min).
5. Break and power-down reset (10 min).
6. Add or revise one state on paper, then in code (30 min).
7. Peer test current-state clarity and reset behavior (25 min).
8. Save diagram, log, code, and reflection (10 min).

## Minimum evidence

State diagram/table, event log showing valid transitions, visible state feedback, and reset/unknown-state explanation.

## Recovery

Run the full state machine with cards and a saved trace if hardware is unavailable.

## Links
- Firmware: `firmware/week09_state_machine/`
- Lab: `labs/week09_state_machines.ipynb`
- HW: `assignments/hw09_states.md`

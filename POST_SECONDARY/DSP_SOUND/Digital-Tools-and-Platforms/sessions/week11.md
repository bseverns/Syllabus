# Week 11 — MIDI or host-control messages

## Goals
- Map a stable control value to a documented 0–127 message.
- Distinguish Serial evidence from actual USB MIDI transport.
- Prevent message flooding with change thresholds.

## Session arc (165 minutes)

1. Read a MIDI CC message as channel/number/value (15 min).
2. Verify board capability and choose Serial-required or USB-MIDI extension route (20 min).
3. Flash Week 11; observe mapped changes and message rate (25 min).
4. Log a slow/fast control gesture and inspect duplicates/flooding (25 min).
5. Break and device reset (10 min).
6. Route to MIDI monitor/approved host if supported; otherwise simulate from Serial (30 min).
7. Tune deadband and document receiver behavior/dropout (25 min).
8. Save contract, log, and reflection (15 min).

## Minimum evidence

Message contract, stable 0–127 mapping, rate/deadband evidence, and either verified MIDI monitor output or clearly labeled Serial simulation.

## Recovery

Serial message output is the complete baseline. Do not imply USB MIDI on an unsupported board.

## Links
- Firmware: `firmware/week11_usb_midi/`
- Lab: `labs/week11_midi_basics.ipynb`
- HW: `assignments/hw11_midi.md`

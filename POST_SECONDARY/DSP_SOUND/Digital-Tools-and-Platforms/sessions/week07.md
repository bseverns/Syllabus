# Week 07 — Multiplexing and settling time

## Goals
- Explain how three select bits choose one of eight channels.
- Scan a CD4051-class mux without hiding channel order or settling time.
- Detect cross-talk, floating inputs, or pinout mismatch from evidence.

## Session arc (165 minutes)

1. Select-channel paper truth table (15 min).
2. Exact-part datasheet orientation and voltage briefing (20 min).
3. Power-off wiring, continuity/pin check, and instructor gate (35 min).
4. Flash scanner; prove grounded/high/reference channels first (25 min).
5. Break and power-down reset (10 min).
6. Scan/log eight channels; vary settling delay (30 min).
7. Plot by channel and identify one artifact (20 min).
8. Save exact chip marking, wiring, data, and reflection (10 min).

## Minimum evidence

Exact-part pin map, select truth table, eight-channel log/plot, chosen settling delay, and one artifact explanation.

## Recovery

Use a paper mux, instructor capture, or direct A0 readings from several sources. Do not guess a substitute chip's pinout.

## Links
- Firmware: `firmware/week07_mux_scan/`
- Lab: `labs/week07_mux_scan.ipynb`
- HW: `assignments/hw07_mux.md`

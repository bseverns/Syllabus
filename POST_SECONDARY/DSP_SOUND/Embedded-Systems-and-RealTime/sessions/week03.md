# Week 03 — Inputs I: debouncing + edge events

## Goals
- Produce clean DOWN/UP events from a button.
- Measure false triggers before/after debouncing.
- Define what you want to guarantee to downstream code.

## Session arc
1. Warm-up: tap test: what counts as ‘one press’?
2. Mini-lecture: bounce physics, edge detection, event semantics
3. Build: implement debounce + event printing
4. Measure: stress test with rapid taps; count false edges
5. Critique: compare debounce thresholds and tradeoffs
6. Close: preview ADC stability

## Links
- `firmware/week03_button_debounce_events/`
- `bench/CHECKLIST.md`

# Week 02 — Non-blocking loops + cooperative scheduling

## Goals
- Replace delay-based timing with task cadences.
- Run 3–4 tasks without starving any of them.
- Explain why ‘cadence’ is part of feel.

## Session arc
1. Warm-up: spot the hidden delays in a code snippet
2. Mini-lecture: cooperative scheduling, timers, micros wraparound
3. Build: adapt scheduler sketch for your inputs
4. Measure: confirm each task runs at intended rate
5. Critique: what did you prioritize and why?
6. Close: preview debouncing as converting noise → events

## Links
- `firmware/week02_cooperative_scheduler/`
- `resources/DESIGN_PATTERNS.md`

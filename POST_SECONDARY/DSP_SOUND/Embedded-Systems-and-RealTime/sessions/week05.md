# Week 05 — Event routing: queues + priorities

## Goals
- Implement a ring buffer queue.
- Decide and document drop policies.
- Show a case where your system stays usable under spam.

## Session arc
1. Warm-up: host flood demo: what do you drop first?
2. Mini-lecture: queues, priorities, loss policies, backpressure
3. Build: modify queue sketch: add your real events
4. Measure: simulate overload and confirm priority behavior
5. Critique: tradeoffs: lossless vs responsive
6. Close: preview state machines

## Links
- `firmware/week05_event_queue_priority/`
- `resources/DESIGN_PATTERNS.md`

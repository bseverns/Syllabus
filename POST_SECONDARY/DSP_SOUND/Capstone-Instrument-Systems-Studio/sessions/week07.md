# Week 07 — Integration week: edge cases + overload

## Goals
- Find what breaks first and fix it.
- Define drop policies and priorities.
- Stabilize timing under load.

## Studio
Stress test: maximum input spam, extreme parameter settings, worst-case scenes.

## Critique prompt
What’s the system’s ‘breaking voice’? Can you recognize it early?

## Deliverables
- Stress test report
- Overload policy documented
- Bug triage list

## Optional lane notes
- Instrument: ensure button edges never lost.
- Plugin: ensure CPU stable across buffer sizes.
- Installation: ensure network dropouts don’t freeze the scene.

# Week 05 — Reliability pass

## Goals
- Implement safe defaults and recovery.
- Handle bad inputs and corrupted config.
- Make failure legible (diagnostics).

## Studio
Add SAFE mode + INFO/self-test. Add persistence versioning if applicable.

## Critique prompt
What happens on the worst day? How does the device apologize?

## Deliverables
- Safe mode path documented
- Diagnostics command/API
- Bench checklist v1

## Optional lane notes
- Instrument: hold button on boot → safe mode.
- Plugin: guard NaNs, clamp parameters.
- Installation: fallback behaviors when sensors disappear.

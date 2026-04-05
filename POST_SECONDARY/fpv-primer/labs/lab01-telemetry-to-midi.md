# Lab 01 — Telemetry → MIDI (minimal)

**Goal:** turn one telemetry signal into one stable MIDI CC.

## Recommended starting signals

For an Air65-class ELRS baseline, good first signals are:

- `throttle_command`
- `battery_voltage`
- `link_quality`

Avoid using a poorly understood derived value just because it looks dramatic.

## Pre-lab rule

Do not start this lab until the group can explain:

- what the source signal means
- when the signal is valid
- what should happen if the signal disappears

## Steps
1. Pick one telemetry channel (e.g., throttle, pitch rate, battery voltage).
2. Define semantics + range in `docs/06-telemetry-semantics.md`.
3. Apply deadband + smoothing from `docs/07-mapping-cookbook.md`.
4. Output one CC to a MIDI monitor.
5. Replay the same capture twice and confirm the output behaves the same way.

## Observe
- CC moves smoothly.
- When telemetry drops, CC behaves safely (holds/decays/zeros).
- The output is boring in a good way: stable, inspectable, and repeatable.

## Why
One channel done well is better than ten channels that lie.

## Artifact
- completed `templates/mapping-sheet.md`
- mapping YAML snippet + short screen capture of MIDI monitor
- one note describing the chosen dropout behavior

## Extension

Swap to a second source signal only after the first mapping is documented and replayable.

# Lab 01 — Telemetry → MIDI (minimal)

**Goal:** turn one telemetry signal into one stable MIDI CC.

## Steps
1. Pick one telemetry channel (e.g., throttle, pitch rate, battery voltage).
2. Define semantics + range in `docs/06-telemetry-semantics.md`.
3. Apply deadband + smoothing from `docs/07-mapping-cookbook.md`.
4. Output one CC to a MIDI monitor.

## Observe
- CC moves smoothly.
- When telemetry drops, CC behaves safely (holds/decays/zeros).

## Why
One channel done well is better than ten channels that lie.

## Artifact
- mapping YAML snippet + short screen capture of MIDI monitor

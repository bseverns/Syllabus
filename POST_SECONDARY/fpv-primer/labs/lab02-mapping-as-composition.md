# Lab 02 — Mapping as composition (three “feels”)

**Goal:** make the same telemetry input feel like three different instruments.

## Input discipline

Use the same source signal and the same replay capture for all three presets. If you change the source data between tests, you are no longer comparing mappings cleanly.

## Steps
1. Choose one source signal (same as Lab 01).
2. Create three mappings:
   - Feather: S-curve + smoothing
   - Blade: piecewise + minimal smoothing
   - Ritual: quantized steps + hysteresis
3. Test each against the same bench replay capture.
4. Name each preset according to behavior, not mood alone.

## Observe
- The *gesture* feels different without changing the raw telemetry.
- Differences are traceable to shaping choices, not hidden source changes.

## Why
This is where control becomes an instrument.

## Artifact
- one completed mapping sheet per preset family
- three mapping presets + A/B clip per preset
- short comparison note explaining which shaping move changed the feel most

# Week 10 — Calibration and persistence

## Goals
- Capture a bounded input range and map it to a useful output.
- Store calibration with a validity marker and safe defaults.
- Prove power-cycle recovery and a recalibration route.

## Session arc (165 minutes)

1. Compare raw ranges from two controls/sensors (15 min).
2. Explain calibration, validity marker, EEPROM wear, and fallback defaults (25 min).
3. Flash Week 10; record default behavior (20 min).
4. Hold calibration input during reset; sweep full intended range (25 min).
5. Break and power-down reset (10 min).
6. Power-cycle and prove stored range; test narrow/failed calibration (30 min).
7. Document recalibration/reset instructions for a peer (25 min).
8. Save logs and reflection (15 min).

## Minimum evidence

Raw min/max, mapped output, saved/reloaded proof, invalid-calibration fallback, and user-facing reset instructions.

## Recovery

Use calibration values in RAM or a paper mapping table when local storage differs or cannot be safely tested.

## Links
- Firmware: `firmware/week10_calibration_eeprom/`
- Lab: `labs/week10_calibration.ipynb`
- HW: `assignments/hw10_calibration.md`

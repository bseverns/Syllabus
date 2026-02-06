# Week 04 — Inputs II: ADC stability + calibration

## Goals
- Implement smoothing for a knob.
- Implement calibration and store min/max.
- Decide where calibration lives (boot, command, UI) and justify.

## Session arc
1. Warm-up: listen: does your knob feel like sand or silk?
2. Mini-lecture: ADC noise, sampling cadence, drift, why calibration is compassion
3. Build: flash calibration sketch; add your own reporting
4. Measure: capture raw vs EMA vs calibrated mapping
5. Critique: what counts as ‘truth’ for a sensor?
6. Close: preview event queues + overload

## Links
- `firmware/week04_adc_calibration/`
- `labs/week04_adc_filtering.ipynb`
- `resources/DONT_BRICK.md`

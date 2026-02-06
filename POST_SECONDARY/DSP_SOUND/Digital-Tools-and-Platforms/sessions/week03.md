# Week 03 — Analog inputs (pots) + mapping + smoothing

## Goals
- Read analog values and understand resolution.
- Map raw readings to meaningful ranges (PWM / 0–127).
- Stabilize output with smoothing and deadband.

## Session arc (timed)
1. Warm-up (10 min): turn a knob and narrate what you expect the numbers to do
2. Mini-lecture (20–30 min): ADC, noise, quantization, mapping
3. Build + flash (40–60 min): flash Week03 sketch; drive LED by pot
4. Observe + log (20 min): log raw vs smoothed; plot and compare
5. Share-out (15 min): tradeoffs: stability vs responsiveness
6. Close (10 min): preview: non-blocking timing

## Prep (instructor)
- Ensure you have enough pots.
- Discuss 3.3V vs 5V rails for the cohort.

## Links
- `hardware/week03_pot.md`
- `firmware/week03_pot_pwm/`
- `labs/week03_analog_mapping.ipynb`
- `assignments/hw03_analog.md`

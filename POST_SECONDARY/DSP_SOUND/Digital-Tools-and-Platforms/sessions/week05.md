# Week 05 — Sensors, thresholds, and hysteresis

## Goals
- Read an analog sensor as data rather than a magic trigger.
- Compare one threshold with an on/off hysteresis pair.
- Define safe behavior for missing or implausible readings.

## Session arc (165 minutes)

1. Observe a noisy sensor trace and predict chatter (15 min).
2. Demonstrate threshold versus hysteresis with a drawn state diagram (20 min).
3. Power-off build and inspection: sensor or potentiometer fallback on A0, LED on D9 through a resistor (30 min).
4. Flash `week05_sensor_threshold`; inspect the Serial contract (25 min).
5. Break and power-down reset (10 min).
6. Log a slow sweep across both thresholds; plot raw/state data (35 min).
7. Tune thresholds from measured range, then test dropout/extreme values (20 min).
8. Save wiring, code, CSV, plot, and reflection (10 min).

## Minimum evidence

Measured sensor range, stated on/off thresholds, a plot showing stable state through the hysteresis band, and one failure/default behavior.

## Recovery

If the sensor is incompatible or unreliable, use a 10k potentiometer as the complete input route. The learning target is threshold/state design.

## Links
- Firmware: `firmware/week05_sensor_threshold/`
- Lab: `labs/week05_thresholds.ipynb`
- HW: `assignments/hw05_sensors.md`

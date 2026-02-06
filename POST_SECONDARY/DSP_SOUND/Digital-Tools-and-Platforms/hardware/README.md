# Hardware Notes

This course avoids preciousness: build with what you have.

Common parts:
- breadboard + jumper wires
- 1× microcontroller
- 4–10× LEDs + 220Ω resistors
- 2–6× buttons (momentary)
- 2–6× potentiometers (10k is common)
- optional: photoresistor, distance sensor

## Wiring conventions
- Always share ground between sensors and board.
- Prefer internal pullups for buttons (wire to GND).
- Keep analog wires short. Add a 0.1uF cap near sensors if noisy.

## Week-by-week wiring
See `hardware/weekXX_*.md`.

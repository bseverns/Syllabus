# Hardware Notes

This course avoids preciousness: build with what you have.

Common parts:
- breadboard + jumper wires
- 1× microcontroller
- 4–10× LEDs + 220Ω resistors
- 2–6× buttons (momentary)
- 2–6× potentiometers (10k is common)
- optional: photoresistor, distance sensor

**CC orientation reference:** Project the [Arduino Uno board image](../../../../SECONDARY/robotic-vibes/assets/hardware-references/arduino-uno.jpg) once before the first bench build to name the USB connector, reset button, and power/digital/analog headers. It is not a wiring diagram; local board labels and the week's wiring file control. Its [CC BY 2.0 attribution](../../../../SECONDARY/robotic-vibes/assets/hardware-references/README.md) is maintained with the asset.

## Wiring conventions
- Always share ground between sensors and board.
- Prefer internal pullups for buttons (wire to GND).
- Keep analog wires short. Add a 0.1uF cap near sensors if noisy.

## Week-by-week wiring
See `hardware/weekXX_*.md`.

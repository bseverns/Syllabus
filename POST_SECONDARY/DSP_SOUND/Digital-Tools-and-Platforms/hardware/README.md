# Hardware Notes

The required Uno-compatible route is defined in [BOM and Kit](BOM_AND_KIT.md) and [Wiring Baseline](WIRING_BASELINE.md). Build identical labeled team kits from that baseline, preserve a known-good reference rig, and document every substitution before delivery.

Optional sensors, native USB-MIDI boards, addressable LEDs, and expanded multiplexers are extensions only after the core route passes local preflight. A potentiometer, discrete current-limited LEDs, and Serial messages provide the complete fallback route.

**CC orientation reference:** Project the [Arduino Uno board image](../../../../SECONDARY/robotic-vibes/assets/hardware-references/arduino-uno.jpg) once before the first bench build to name the USB connector, reset button, and power/digital/analog headers. It is not a wiring diagram; local board labels and the week's wiring file control. Its [CC BY 2.0 attribution](../../../../SECONDARY/robotic-vibes/assets/hardware-references/README.md) is maintained with the asset.

## Wiring conventions
- Always share ground between sensors and board.
- Prefer internal pullups for buttons (wire to GND).
- Keep analog wires short. Add a 0.1uF cap near sensors if noisy.

## Week-by-week wiring

Use [Wiring Baseline](WIRING_BASELINE.md) as the authoritative weekly pin table. The focused Week 2, Week 3, and Week 7 notes add build detail; local board labels and exact component datasheets still control.

# Wiring Patterns (quick notes)

## Pots
- 3-wire: 3.3V/5V, GND, wiper to analog
- add 0.01uF–0.1uF capacitor from wiper to GND if jitter is stubborn
- avoid long unshielded runs near LED power lines

## Buttons
- use INPUT_PULLUP and wire to GND
- keep wires short; consider twisted pair with GND for long runs

## LEDs (WS2812 etc.)
- keep LED power separate from analog reference when possible
- add bulk capacitance near strip
- add a resistor on data line (~220–470Ω) near MCU

## Grounding
Star-ish grounding helps:
- analog ground cleanliness matters for feel

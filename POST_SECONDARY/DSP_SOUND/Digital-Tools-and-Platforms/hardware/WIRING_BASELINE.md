# Uno-Compatible Wiring Baseline

This is the default pin plan used by the supplied firmware. The exact local board labels, voltage limits, and datasheets override it. Power off before changing wiring and request the required instructor inspection before first power.

| Week | Input wiring | Output/other wiring | Required check |
| --- | --- | --- | --- |
| 1 | None | Onboard `LED_BUILTIN`; USB data cable | Correct board/port and known-good upload |
| 2 | Button D2 ↔ GND; firmware uses `INPUT_PULLUP` | Onboard LED optional | Pressed reads LOW; no floating input |
| 3 | Pot outer legs GND/board logic reference; wiper A0 | D9 → resistor → LED → GND | Rail matches board; wiper never exceeds ADC voltage |
| 4 | None | Onboard LED | Serial baud 115200; no output actuator |
| 5 | Sensor/divider output A0, or Week 3 pot fallback | D9 → resistor → LED → GND | Measured sensor output stays in ADC range |
| 6 | Optional pot/sensor A0 | Onboard LED; USB Serial | Commands cannot directly create unsafe output |
| 7 | Mux select S0/S1/S2 to D2/D3/D4; common signal to A0; enable state and rails per exact datasheet | Mux channel inputs use known references/sensors | Exact part pinout, supply, enable, and input range inspected |
| 8 | Pot A0 | D9/D10/D11 each → resistor → LED → GND | Current limiting present; cues do not rely on color alone |
| 9 | Button D2 ↔ GND; pot A0 | Three LEDs as Week 8 | State LEDs and button do not conflict |
| 10 | Calibration button D2 ↔ GND; pot/sensor A0 | Serial output | Storage behavior and safe defaults verified for exact board |
| 11 | Pot A0 | USB Serial required; native USB MIDI only on supported/configured board | Board USB mode documented; MIDI monitor sees expected device |
| 12 | Pots A0–A3; buttons D2–D5 ↔ GND | D9–D11 each with LED resistor | Pin map frozen; each subsystem proven before integration |

## Power-off inspection order

1. Board and team ID match the firmware target.
2. No second power source is attached.
3. Ground and logic-reference rails are correctly labeled.
4. LED resistors are present.
5. Potentiometer/sensor output goes to the intended analog pin.
6. Buttons go to ground only under the `INPUT_PULLUP` baseline.
7. IC notch/pin 1, supply, enable, common, and select pins match the exact datasheet.
8. Loose wire ends and conductive debris are removed.
9. Instructor approves first power for new circuits.

## Safe reduction routes

- Use one pot instead of a sensor or mux.
- Use onboard LED plus explicit Serial text instead of external feedback.
- Use two knobs/two buttons in the capstone while retaining debounce, deadband, modes, event output, test evidence, and documentation.
- Use saved CSV and a de-energized board/paper pin map when a board or port fails.

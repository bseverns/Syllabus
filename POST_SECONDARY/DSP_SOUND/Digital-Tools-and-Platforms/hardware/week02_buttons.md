# Week 02 Wiring — Button(s)

## Recommended wiring (internal pullup)
- Button one leg to **GND**
- Button other leg to a digital pin (e.g. D2)
- Firmware uses `pinMode(pin, INPUT_PULLUP)`

This creates a stable default HIGH state and a LOW when pressed.

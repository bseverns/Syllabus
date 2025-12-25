# Extension: Base + CV summing (optional)

If you want the rate knob to set a “home” and CV to modulate around it, build a CTRL_MIX node:
- Rate pot wiper → 100k → CTRL_MIX
- Vref → 47k → CTRL_MIX
- CV atten pot wiper → 100k → CTRL_MIX
- CTRL_MIX → 10k → 555 pin 5
- 100nF: CTRL_MIX → GND
- 10nF: pin 5 → GND
- Clamp diodes at pin 5

This makes CV influence bounded and musical.

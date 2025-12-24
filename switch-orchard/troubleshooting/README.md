# Troubleshooting — Switch Orchard

## Silent module (nothing passes)
- Check CD4051 power: VDD=+5V, VSS=0V, VEE=0V
- INH must be LOW (tie to GND)
- Confirm Z and X pins: are you routing the direction you think?

## Wrong channel / unpredictable switching
- Address lines floating: A/B/C must be tied to defined states
- Add 100k pull-downs if needed
- Keep A/B/C wires short

## Clicking / pops in audio switching
- Hard switching causes clicks (normal). Reduce by:
  - switching at zero crossings (hard)
  - switching CV instead of audio
  - adding a tiny RC smoothing on Z (10nF to GND) as experiment

## Scanner doesn’t step
- Verify clock signal at 4017 clock pin
- RESET must be low (100k to GND)
- 4017 enable/inhibit pins must be set correctly (per datasheet)
- Confirm diode directions in the A/B encoder:
  - anode at Q output, cathode at A_NODE/B_NODE

## Manual selector feels “stuck”
- Verify threshold dividers (T1/T2) are correct voltages
- Put LEDs on A/B to see if they change

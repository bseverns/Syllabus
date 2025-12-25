# Troubleshooting (fast)

## If nothing works
1. Measure +5V on every IC power pin.
2. Measure Vref (~2.5V).
3. Verify clock at 555 pin 3.
4. Verify clock at 40106 output.

## If clock works but crusher is silent
- Confirm CD4051:
  - VDD to +5V, VSS to GND
  - A/B/C tied to GND
  - X0 is the channel you actually wired
- Confirm hold cap goes to Vref (not GND).

## If you hear clock ticks in the audio
- Add/confirm decoupling caps near the ICs.
- Keep CLK wire short and away from SAMP_NODE.
- Try moving the hold cap closer to CD4051 Z pin.
- Add 100nF from +5 to GND near CD4051 and op-amp.

## If CV breaks the clock
- Confirm the 47k series resistor from CV socket.
- Confirm clamp diodes at 555 pin 5.
- Turn CV amount pot down; then reintroduce modulation.

# Teacher Quickstart — Maker Track (teen/early‑college)

**Hardware baseline (Uno):** encoders/pots, buttons, LEDs, DIN‑5 parts (optional).  
**Software:** Arduino IDE (Maker) / PlatformIO (Studio); serial monitor; MIDI monitor or Processing visualizer.

Project the [MIDI controller knob reference](../shared/assets/midi-controller-knobs.jpg) while naming physical controls; its [CC BY 2.0 attribution](../shared/assets/README.md) is maintained with the asset.
Project the [Arduino Uno orientation reference](../../robotic-vibes/assets/hardware-references/arduino-uno.jpg) before the smoke test to name board regions; it is not a wiring diagram. Its [CC BY 2.0 attribution](../../robotic-vibes/assets/hardware-references/README.md) is maintained with the asset.

**Smoke test**
1. Open `examples_global/MIDI_Serial_Test/` and upload.
2. Confirm serial bytes appear; if bridged, verify MIDI monitor receives CCs.
3. Wire one encoder → map to CC #1; verify 0–127 sweep.

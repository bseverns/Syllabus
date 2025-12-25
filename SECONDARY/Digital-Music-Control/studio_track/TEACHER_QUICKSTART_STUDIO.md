# Teacher Quickstart — Studio Track (upper/advanced)

**Hardware baseline (Uno):** encoders/pots, buttons, LEDs, DIN‑5 parts (optional).  
**Software:** Arduino IDE (Maker) / PlatformIO (Studio); serial monitor; MIDI monitor or Processing visualizer.

**Smoke test**
1. Open `examples_global/MIDI_Serial_Test/` and upload.
2. Confirm serial bytes appear; if bridged, verify MIDI monitor receives CCs.
3. Wire one encoder → map to CC #1; verify 0–127 sweep.

---
### Board Choice Notes
- Start with **Uno** to stabilize classroom wiring and logic.
- Switch to **ATmega32u4** when you want **native USB-MIDI** (no serial bridge).
- Use **Teensy** when you need more IO, higher scan rates, or audio/DSP; set **USB Type: MIDI** (or MIDI+Serial) in tools or via PlatformIO `-DUSB_MIDI`.

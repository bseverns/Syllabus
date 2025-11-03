# Level 2: Object‑Oriented Control — 4×2h (Studio Track (upper/advanced))

## Week 1 — Orientation + Core Concept
- Flash a working baseline (Blink→MIDI serial bytes on Uno)
- Pin map, inputs/outputs, analog → mapped control
- Goal set: what will your controller *do*?

## Week 2 — Focused Build
- Add encoders/pots and map to CCs
- Test with a MIDI monitor (serial‑bridge) or Processing visualizer
- Document decisions (CC map, ranges)

## Week 3 — Expansion & Customization
- Add a scene/state and a status LED pattern
- Refactor into functions (Maker) / classes (Studio)
- Mid‑demo and peer debug

## Week 4 — Showcase + Reflection
- Perform a short demo
- Summarize what worked and what you'd change
- Tag release in repo (v0.1)
        
**Focus:** Abstractions: Encoder, LED, MIDISender; object arrays; header/impl separation; PlatformIO workflow.

---

## Why consider ATmega32u4 or Teensy?
- **ATmega32u4 (Leonardo/Micro):** Native USB enables **true USB‑MIDI device** mode without host bridges; lower latency and cleaner DAW integration.
- **Teensy (3.x/4.x):** Far more CPU/RAM; built‑in **USB types** (MIDI/Serial/Audio); **hardware DAC** (on some models) and the Teensy Audio library for real‑time DSP; large ISR headroom for encoders/LEDs.
- **Tradeoffs:** cost, 3.3V logic on many Teensy boards (level shifting), different cores/toolchains; but better long‑term headroom for complex controllers.

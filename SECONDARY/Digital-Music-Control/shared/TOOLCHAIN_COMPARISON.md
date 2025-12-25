# Toolchain Comparison (Arduino IDE vs PlatformIO vs CMake)

- **Arduino IDE**: lowest friction, great for classrooms; single‑file sketches; Library Manager.
- **PlatformIO (VS Code)**: multiple environments, reproducible builds, CI; recommended for multi‑file OOP projects.
- **CMake / Makefiles**: advanced/custom toolchains; useful for non‑Arduino cores and desktop tools.

**Recommendation**: Start in Arduino IDE for Maker Track; migrate to PlatformIO for Studio Track and for multi‑module firmware.

---
## Boards vs. USB stacks (advanced)
- **Uno/ATmega328P:** simplest classroom baseline; use Serial‑to‑MIDI bridge or DIN‑5 hardware MIDI @ 31250 baud.
- **ATmega32u4:** native USB → enumerate as MIDI without drivers (HID/MIDI composite possible).
- **Teensy:** select USB type (**MIDI**) in tools; gain access to Audio library; excellent for high‑channel controllers.

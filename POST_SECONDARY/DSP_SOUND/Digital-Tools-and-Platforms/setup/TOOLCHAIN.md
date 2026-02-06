# Toolchain Setup

This course assumes Arduino-style development.

## Option A — Arduino IDE (recommended for mixed cohorts)
1. Install Arduino IDE.
2. Install board support:
   - Arduino: via Board Manager
   - Teensy: install Teensyduino add-on
   - Pico: install RP2040 boards package (optional)
3. Confirm you can upload a Blink sketch.

## Option B — PlatformIO (nice for versioning + CI)
- Use VS Code + PlatformIO.
- See `setup/PLATFORMIO_NOTES.md`.

## Serial port sanity
- macOS: /dev/cu.usbmodem* or /dev/cu.usbserial*
- Linux: /dev/ttyACM* or /dev/ttyUSB*
- Windows: COM3, COM4, ...

## Safety
Before powering anything:
- confirm 5V vs 3.3V logic
- confirm grounds are shared
- confirm no shorts on rails
See `resources/SAFETY.md`.

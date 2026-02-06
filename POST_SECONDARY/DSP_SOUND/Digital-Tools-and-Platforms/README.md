# Digital Tools and Platforms — microcontrollers as creative material (12 weeks)

This module is the *hands-on bridge* between “signals on paper” and “signals in the world.”

We treat microcontrollers as tiny, honest computers:
- they read messy inputs (buttons, pots, sensors),
- they respond in real time (LEDs, sound, motors),
- they speak in protocols (Serial, MIDI, I2C),
- and they demand good habits (debounce, timing, state machines).

This course is built to be cloned as a repo and lived inside.

## What students will leave with
By the end of 12 weeks, students can:
- wire and program a microcontroller safely and repeatably
- read digital + analog inputs and smooth noisy data
- design non-blocking timing loops (no “delay jail”)
- build small state machines for modes + behaviors
- send *real* control data to a host (Serial and/or MIDI)
- document circuits + firmware so others can rebuild them

## Target hardware (pick one)
- **Teensy 4.0/4.1** (ideal if you want USB MIDI without drama)
- **Arduino Uno / Nano / compatible** (good for fundamentals)
- **Raspberry Pi Pico** (optional alt; if you already love it)

The repo includes Arduino-style sketches. Teensy works in Arduino IDE with the Teensyduino add-on.

## Repo map
- `syllabus/` → course description + weekly schedule
- `sessions/` → week-by-week lesson plans
- `firmware/` → Arduino sketches + PlatformIO notes
- `hardware/` → wiring diagrams + parts lists (markdown)
- `labs/` → Jupyter notebooks for logging + analysis (Serial → CSV → plot)
- `assignments/` → prompts + rubrics + submission
- `project/` → capstone build brief
- `setup/` → environment + toolchain setup
- `scripts/` → serial logger + helpers
- `resources/` → glossary + safety notes + protocol cheat sheets

## Quick start (instructor)
1. Install Arduino IDE + board support (see `setup/TOOLCHAIN.md`)
2. For Python logging: `pip install -r requirements.txt`
3. Flash Week 01 sketch: `firmware/week01_blink_hello/week01_blink_hello.ino`
4. In a terminal: `python scripts/serial_logger.py --port YOUR_PORT --baud 115200 --outfile export/week01.csv`
5. Open the lab notebook: `labs/week01_serial_basics.ipynb`

## Licensing
- Course text + prompts: **CC BY 4.0** (`LICENSES/CC-BY-4.0.txt`)
- Code: **MIT** (`LICENSES/MIT.txt`)

_Last updated: 2026-02-05_

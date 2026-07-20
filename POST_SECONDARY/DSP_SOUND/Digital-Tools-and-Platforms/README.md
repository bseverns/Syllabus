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

## Hardware baseline

- **Required reference route:** Arduino Uno / Nano / compatible, using the documented pin plan and Serial messages.
- **Optional native USB-MIDI route:** Teensy 4.x or another board only after its board package, USB mode, pin map, and all affected sketches pass local preflight.
- **Alternate-board port:** Raspberry Pi Pico or another Arduino-compatible target is an instructor adaptation, not a drop-in substitution.

The supplied sketches compile for the Uno reference route. Freeze one local board family before enrollment; see the bill of materials and facilitator launch guide.

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
1. Freeze the local board baseline and complete `FACILITATOR_LAUNCH_GUIDE.md` plus `PREFLIGHT_RECORD.md`.
2. Build team kits from `hardware/BOM_AND_KIT.md` and verify `hardware/WIRING_BASELINE.md` on one reference bench.
3. Install Arduino IDE + board support (see `setup/TOOLCHAIN.md`) and compile every sketch with `bash tests/compile_firmware.sh`.
4. For Python logging: `pip install -r requirements.txt`.
5. Flash `firmware/week01_blink_hello/week01_blink_hello.ino`.
6. Capture with `scripts/serial_logger.py`, then use `labs/week01_serial_basics.ipynb` or the structured route in `labs/README.md`.

## Learner and delivery support

- Give students `STUDENT_START_HERE.md` before the first bench build.
- Use the detailed `sessions/` and exact `assignments/` files for Weeks 1–12.
- Keep `STUDENT_PROGRESS_TRACKER.md` with each board/team folder.
- Serial, discrete LEDs, and Uno-compatible core APIs are the required route; native USB MIDI, addressable LEDs, and alternate sensors are extensions.
- Hardware failure does not end the learning path: de-energized boards, saved logs, paper protocols/state diagrams, and reference captures preserve the same evidence targets.

## Licensing
- Course text + prompts: **CC BY 4.0** (`LICENSES/CC-BY-4.0.txt`)
- Code: **MIT** (`LICENSES/MIT.txt`)

_Last updated: 2026-07-19_

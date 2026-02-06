# Embedded Systems + Real-Time Instruments (12 weeks)

This module is about **making firmware that survives contact with reality**:
- timing that stays stable under load,
- inputs that don't chatter,
- outputs that don't glitch,
- memory that doesn't corrupt,
- and a device that can explain itself when it’s confused.

If #4 was about mapping + protocol contracts, #5 is about the **machine underneath**:
architecture, scheduling, and the quiet craft of reliability.

## Outcomes
Students can:
- build non-blocking firmware loops and cooperative schedulers
- measure latency and jitter (and reduce both)
- design debounced buttons + stable ADC reads
- implement event routing + mode/state machines
- handle persistence (EEPROM/flash) with versioning + safe defaults
- design calibration routines (and store results)
- design *failure modes* (safe mode, factory reset, diagnostics)
- ship a small embedded instrument with documentation + bench tests

## Recommended hardware
- Teensy 4.x (fast, USB MIDI easy) **or** Arduino-class board
- 4–8 potentiometers, 4–8 buttons
- optional: multiplexers (CD74HC4067), LED strip (WS2812), OLED display

## Repo map
- `syllabus/` • `sessions/` • `assignments/`
- `firmware/` scaffolds + patterns (scheduler, event bus, persistence, calibration)
- `labs/` notebooks for timing/memory analysis
- `bench/` test procedures + checklists
- `hardware/` wiring patterns + noise mitigation notes
- `resources/` design patterns + “don’t brick the device” guidelines
- `project/` final build brief + report template
- `setup/` tools and environment

## Quick start (host + logging)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python host/serial_probe.py --port YOUR_PORT --baud 115200 --cmd INFO
```

_Last updated: 2026-02-05_

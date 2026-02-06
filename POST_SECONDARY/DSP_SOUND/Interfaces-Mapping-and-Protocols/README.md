# Interfaces, Mapping, and Protocols — turning gestures into meaning (12 weeks)

This module is where **control becomes instrument**.

We take the raw stuff of interaction — knobs, buttons, sensors, timing — and forge:
- **protocols** (Serial, MIDI, OSC),
- **mapping** (curves, scaling, quantization, hysteresis),
- **feedback** (LED language, states, affordances),
- **configuration** (end-user clarity without breaking the machine).

## Outcomes
Students can:
- design behavior as states + transitions
- choose protocol(s) and justify tradeoffs
- build mapping layers (smoothing, deadband, curves, quantization)
- rate-limit and prioritize events
- design feedback that teaches device state
- design a config model + safe config workflow
- ship a small controller + mapping layer others can use

## Repo map
- `syllabus/` • `sessions/` • `labs/`
- `firmware/` embedded scaffolds (Serial + MIDI)
- `host/` bridges + tools (Serial→CSV, Serial→MIDI, OSC send, config schema)
- `assignments/` • `project/` • `resources/` • `setup/`

## Quick start
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python host/serial_logger.py --port YOUR_PORT --baud 115200 --outfile export/week01.csv
```

_Last updated: 2026-02-05_

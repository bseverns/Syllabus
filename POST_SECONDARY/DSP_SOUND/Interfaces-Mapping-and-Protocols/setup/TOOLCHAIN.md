# Toolchain Setup

## Microcontroller lane
- Arduino IDE baseline.
- Teensy users: install Teensyduino.

## Python lane
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name interfaces --display-name "Interfaces & Mapping"
```

## Optional lanes
- MIDI: enable a virtual port if needed (IAC/loopMIDI).
- OSC: TouchDesigner/Max/SC/Python as receiver.
- WebSerial UI: Chrome/Edge.

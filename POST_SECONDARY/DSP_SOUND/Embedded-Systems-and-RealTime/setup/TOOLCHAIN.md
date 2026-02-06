# Toolchain Setup

## Embedded lane
- Arduino IDE (baseline)
- Teensy users: Teensyduino
- Optional: PlatformIO (recommended for larger projects)

## Python lane (measurement tools)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name embedded --display-name "Embedded RT"
```

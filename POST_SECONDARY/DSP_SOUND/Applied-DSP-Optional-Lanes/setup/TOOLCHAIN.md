# Toolchain

## Core
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name applied_dsp --display-name "Applied DSP"
```

## Optional lane: Plugin (JUCE)
Keep JUCE projects local; this repo provides checklists and contracts.

## Optional lane: Embedded
Prototype in host lane first, then port to Teensy/Daisy/etc.

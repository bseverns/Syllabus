# Environment Setup

This course uses Python + Jupyter. Keep it boring and reproducible.

## 1) Create a virtual environment

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name foundations-signals --display-name "Foundations: Signals"
```

### Windows (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name foundations-signals --display-name "Foundations: Signals"
```

## 2) Audio playback notes
- If `sounddevice` fails, install system audio backends or use exported `.wav` files and listen in Audacity.
- You can complete the course without live playback: plots + saved clips are enough.

## 3) Generate sample audio
```bash
python scripts/generate_samples.py
```

## 4) Launch JupyterLab
```bash
jupyter lab
```

## Troubleshooting
See `setup/TROUBLESHOOTING.md`.

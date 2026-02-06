# Troubleshooting

## Jupyter won't open
- Confirm venv is active.
- Reinstall: `pip install -r requirements.txt`
- Try: `python -m jupyterlab`

## `sounddevice` can't find an output device
- That's okay. Export `.wav` from notebooks and listen in Audacity.
- On Linux you may need PortAudio dev libraries.

## Audio file errors
- Run `python scripts/generate_samples.py` to create `data/audio_samples/`.

## Plots not showing
- Ensure notebook kernel is set to `Foundations: Signals` (or your env kernel).
- Restart kernel and run cells in order.

## Students on Chromebooks
- Option A: run notebooks via a hosted Jupyter service (institutional).
- Option B: run locally on lab machines and submit via Git.

# Applied DSP: Effects, Synthesis, and Optimization
**Single track with optional lanes** • 12 weeks • advanced high school / undergrad

Build DSP that **ships**: stable, measurable, musical, and documented.

## Optional lanes (choose later)
- `lanes/host/` — reference lane (fast iteration, always works)
- `lanes/plugin/` — JUCE/VST3/AU notes + TODO checklist
- `lanes/embedded/` — embedded constraints + scaffolds

Everyone shares the same DSP core in `dsp/`.

## Outcomes
- implement classic blocks (filters, delay, distortion, dynamics, modulation)
- design parameter feel (tapers, smoothing, bounds)
- measure + listen (golden files, plots, basic spectral checks)
- profile + optimize (no allocations in hot path, predictable CPU)
- ship presets/settings + docs + release notes

## Quick start (host lane)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python tests/gen_tones.py
python lanes/host/run_block.py --block waveshaper --in tests/assets/sine_440.wav --out export/out.wav
python tests/analyze_wav.py export/out.wav
```

_Last updated: 2026-02-05_

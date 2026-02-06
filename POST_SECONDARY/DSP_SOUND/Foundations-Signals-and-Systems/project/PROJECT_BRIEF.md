# Final Project — Make a Filter (or Analysis Tool) You Can Explain

## Brief
Build a small, reproducible DSP tool that takes an input signal (audio or sensor-like data),
does something meaningful to it, and produces:
- an **output signal**
- at least **two visualizations** (time + frequency / spectrogram / response curve)
- a short written explanation a curious peer can follow

You can make:
- an audio effect (echo, lo-fi, EQ, tremolo, compressor-ish)
- an analysis tool (spectrum / spectrogram inspector)
- a denoiser / smoother for sensor streams
- a hybrid (analysis → control mapping)

## Constraints (on purpose)
- Your project must run on a fresh install following `setup/ENVIRONMENT.md`.
- You must include a “parameter sweep” showing what changes when you tweak a knob.
- You must include a *failure mode*: what breaks if parameters go too far?

## Suggested timeline
- Week 8: choose direction + write a proposal
- Week 9–10: implement core DSP + visuals
- Week 11: polish + document
- Week 12: demo + critique

## Deliverables
- `project/REPORT.md` (1–2 pages)
- `project/demo.ipynb` (runnable)
- `export/` with plots + any audio clips
- Short README update at repo root linking to your project

# Foundations of Signals and Systems — a DSP on-ramp (12 weeks)

A scrappy, hands-on signals course for advanced high school + undergrad makers.

This folder is meant to be *picked up*, remixed, and re-run. It’s part studio notebook, part teaching zine:
- We learn by **listening, plotting, breaking**, and rebuilding.
- We keep math honest, but we keep it **useful**.
- We treat DSP as a language for *making* (music, sensing, media), not just passing tests.

## What students will leave with
By the end of 12 weeks, students can:
- describe and classify common signals (periodic / transient / noisy) in time + frequency
- explain sampling + aliasing with experiments (not vibes)
- analyze basic LTI systems using convolution and frequency response
- build small FIR + IIR filters and explain what they do
- use FFT-based tools to inspect real audio and sensor data
- document their work in a reproducible repo (plots, code, and reflection)

## How to navigate
Start here, then zoom inward:
- `syllabus/` → course map, policies, weekly schedule
- `sessions/` → week-by-week lesson plans (timed arcs)
- `labs/` → Jupyter notebooks (the core experiments)
- `assignments/` → prompts + rubrics + submission notes
- `project/` → final project brief + checklists
- `setup/` → install notes + troubleshooting
- `scripts/` → small utilities (generate sample audio, etc.)
- `resources/` → readings, glossary, math primer

## Tooling (free + cross-platform)
- Python 3.10+ + JupyterLab
- NumPy / SciPy / Matplotlib
- `soundfile` + `sounddevice` (or alternatives)
- Audacity (for quick listening/annotation)
- Git (for submissions + reproducibility)

## Quick start
1. Create a venv and install deps:
   - see `setup/ENVIRONMENT.md`
2. Run sample generation:
   - `python scripts/generate_samples.py`
3. Launch Jupyter:
   - `jupyter lab`
4. Open `labs/week01_signals_basics.ipynb`

## Course launch

1. Instructors complete `FACILITATOR_LAUNCH_GUIDE.md`, including the full notebook smoke test on the actual student environment.
2. Give learners `STUDENT_START_HERE.md`; run the Week 0 bridge for students new to Python or notebooks.
3. Use the frozen executed notebooks, saved clips/data, and private file-submission route whenever live audio, Git, or local installation is unavailable.

During delivery, use `FACILITATOR_WEEKLY_FIELD_GUIDE.md` for prep/evidence/recovery and give learners `STUDENT_PROGRESS_TRACKER.md` to make milestones and support requests visible.

## Notes for instructors
- This course is designed to flex. Each week includes **core** + **extension** tracks.
- You can run it as a seminar (discussion-heavy) or a lab (hands-on-heavy).
- If your class is more art/creative-tech: lean on the “Listen → Plot → Modify → Explain” loop.

## Licensing
- Course text + prompts: **CC BY 4.0** (see `LICENSES/CC-BY-4.0.txt`)
- Code: **MIT** (see `LICENSES/MIT.txt`)

_Last updated: 2026-02-05_

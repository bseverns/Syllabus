# NeoTrellis M4 Lo‑Fi Sampler — case study

This case study packages a compact sampler as a **teachable system** inside DSP_SOUND.

The sampler is deliberately designed around three ideas:
- **Clock is the spine** (global MIDI clock; deterministic stepping).
- **Constraints create motion** (equal slices + unequal source lengths → phase drift).
- **Expression without side effects** (velocity/probability lanes + stutter over a stable grid).
- **Recovery is part of the instrument** (undo/reslice/factory restore; “don’t brick” mindset).

## What you can teach with this
- **Signals as objects** (phase, sampling, quantization):  
  - `../../Foundations-Signals-and-Systems/sessions/week01.md`  
  - `../../Foundations-Signals-and-Systems/sessions/week07.md`  
  - `../../Foundations-Signals-and-Systems/assignments/hw07_sampling.md`
- **Mapping + feedback + protocol contracts**:  
  - `../../Interfaces-Mapping-and-Protocols/resources/MAPPING_PATTERNS.md`  
  - `../../Applied-DSP-Optional-Lanes/resources/PARAMETER_FEEL.md`  
  - `../../Interfaces-Mapping-and-Protocols/resources/CONFIG_GUIDELINES.md`
- **Real‑time discipline + robustness** (“boring ISR”, cadence, loss policies):  
  - `../../Embedded-Systems-and-RealTime/resources/DESIGN_PATTERNS.md`  
  - `../../Embedded-Systems-and-RealTime/resources/DONT_BRICK.md`  
  - `../../Embedded-Systems-and-RealTime/sessions/week01.md`

## How to run the demo
Use the stand‑alone, repeatable exercises:

- `DEMO_EXERCISES.md` — Goal → Steps → Observe → Why
- `MODULE_CROSSWALK.md` — which DSP_SOUND docs to point at for each exercise
- `VIDEO_COMPANION.md` — an 8–10 minute video plan + overlays + chapters

> Note: this case study assumes the sampler’s own repo contains the helper scripts
> referenced in Preflight (e.g. demo generators and a MIDI clock sender). If you
> teach from this folder alone, treat those scripts as “external tooling” and
> swap in your preferred clock source.

## Suggested “one‑sentence thesis” for a walkthrough
**Keep the music surface the music surface:** no menus, no hidden pages, no surprise state.

_Last updated: 2026-02-08_

# Week 03 — LTI systems and convolution (discrete)

## Goals
- Explain LTI behavior using impulse responses.
- Compute convolution (by hand for tiny signals, by code for real signals).
- Interpret convolution as filtering / smoothing / echoing.

## Session arc (suggested timing)
1. **Warm-up (10 min)** — students clap once; discuss “room response” as an impulse response metaphor
2. **Mini-lecture (25 min)** — linearity + time invariance; impulse response; convolution sum idea
3. **Guided lab (60–80 min)** — manual convolution on toy sequences; then apply to audio and observe effects
4. **Share-out (15 min)** — students demo: their favorite filter kernel and what it did
5. **Close (10 min)** — introduce final project idea seeds: filters as creative tools

## Prep (instructor)
- Prepare 3 example kernels: moving average, edge-ish, echo tap.
- Keep the first convolution examples very small (length 5–9).

## Materials
- Whiteboard for manual sums
- JupyterLab + Python env
- Headphones

## Extensions (if time / advanced track)
- Compare convolution vs correlation.
- Discuss computational cost and why FFT convolution exists (preview only).

## Exit ticket (5 min)
In your own words: *What is the impulse response telling you about a system?*

## Links
- Lab notebook: `labs/week03_convolution.ipynb`
- Assignment: `assignments/hw03_convolution.md`

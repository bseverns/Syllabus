# Build Step 05 — Sample/Hold crusher (CD4051)

## Goal
Turn clock into texture by sampling the audio at the clock rate.

## Wire
- CD4051 select: A=B=C=GND to lock channel X0
- X0 ← AUDIO_BIASED
- Z → SAMP_NODE
- Hold cap: 100nF from SAMP_NODE → Vref (place close)
- INH ← CLK (try CLK_INV if it feels inverted)

## Check
- Slow clock: stepped waveform / “freeze”
- Fast clock: gritty aliasing

## Experiment
Swap hold cap:
- 10nF (bright/crisp)
- 100nF (classic mush)
- 10uF (slow CV-like hold)

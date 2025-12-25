# Fold & Fire
**Single-supply wave shaping + distortion + bonus gates** (AE Modular BRAEDBOARD)  
2-session lab workshop (90–120 min each)

This workshop builds a compact **op-amp + diode** distortion circuit on 5V single-supply.
Students learn how a signal can be **biased**, **amplified**, and **bent** into new harmonic shapes.

**Bonus outputs:** a **CD40106 Schmitt trigger** turns the distorted waveform into **gates** (edge/threshold extraction),
so the distortion becomes a control signal as well as a sound.

**IC count:** 2–3  
- **MCP602** (dual op-amp: buffer + gain/clipping)  
- **CD40106** (optional: gate extraction + cleanup)  

## What students will build
- Vref (2.5V “floating ground”) for audio on single-supply
- Input bias + buffer (dry out)
- Gain stage with **soft clip** (diodes in feedback)
- Optional **asymmetry** (different diode counts) for “character”
- Bonus: gate outs from the distorted signal (1–2 thresholds)

See `syllabus/2-session-block.md`.

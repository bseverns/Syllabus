# Fold & Fire — Two-Session Lab Block

**Format:** 2 sessions × 90–120 minutes  
**Platform:** Tangible Waves AE Modular BRAEDBOARD (0–5V)  
**Core:** MCP602 bias/buffer + diode feedback clipper, optional CD40106 gate extraction

## Course description
This lab explores **nonlinearity** as a musical material. Students build a distortion stage that lives on a 5V single-supply by creating a mid-rail reference (**Vref ≈ 2.5V**). Then they add diode feedback to sculpt the waveform: soft clip, asymmetry, and “fold-like” compression.

A bonus stage uses a Schmitt trigger (40106) to convert the distorted waveform into **rhythmic gates**, turning timbre into control voltage.

## Learning outcomes
Students will:
1. Build a stable Vref and explain why single-supply audio needs a midpoint.
2. AC-couple and bias an input so silence sits at Vref instead of ground.
3. Build an op-amp gain stage and add diode feedback clipping.
4. Compare symmetric vs asymmetric clipping and describe sonic differences.
5. Extract gates from audio using a Schmitt trigger threshold.
6. Debug by measuring Vref, buffer output, and clipper output around Vref.

## Materials (per pair)
- ICs: MCP602, CD40106 (bonus)
- Resistors: 1k, 10k, 47k, 100k
- Caps: 100nF (decouple), 10nF/100nF (coupling/filter)
- Diodes: 1N4148 (4–8)
- LEDs + 1k (2 recommended)
- 50k pot (optional “drive”)

---

## Session 1 — “Bias & Burn”
Build Vref, input bias, buffer, and a clean gain stage (no diodes yet).

**Checkpoints**
- Vref ~2.5V stable
- BUF idles near Vref
- Gain stage increases level without gross oscillation

## Session 2 — “Fold & Speak”
Add diode feedback clipping + asymmetry option + bonus gate extraction.

**Checkpoints**
- Distorted output: low drive mostly clean, higher drive adds harmonics
- Gate output fires cleanly on peaks (LED confirms)
- Students can patch audio and gates simultaneously

**Assessment**
Photo of build + patch diagram + short demo recording + reflection.

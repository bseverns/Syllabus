# Troubleshooting — Fold & Fire

- Vref wrong? Fix divider + 100nF.
- BUF not near Vref at rest? Check IN_AC pull to Vref and op-amp pins.
- Output stuck near rail? Ensure 10k from (−) node to Vref.
- Gate chatter? Add/verify 100k series into 40106 input; use EDGE RC.
- Ticking in audio? Keep gate wiring away from audio nodes; decouple ICs.

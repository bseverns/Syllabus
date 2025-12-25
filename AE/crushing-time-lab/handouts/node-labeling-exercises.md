# Node Labeling Exercises: Crushing Time Lab

Use this as a "read the circuit" activity. Do it before wiring, or while debugging.

## Exercise 1 — Name the nodes (and expected measurements)

1. +5V: _______________________________   Expected: ~5.0V
2. GND: _______________________________   Expected: 0V
3. Vref: ______________________________   Expected: ~2.5V
4. AUDIO_IN: ___________________________
5. IN_AC (after coupling cap): _________
6. AUDIO_BIASED (buffer out): __________ Expected (idle): near Vref
7. CLK_RAW (555 out): __________________ Expected: 0-5V
8. CLK (40106 out): ____________________ Expected: clean 0-5V
9. SAMP_NODE (4051 Z): _________________ Expected (idle): near Vref
10. OUT_DRY: ___________________________
11. OUT_CRUSH: _________________________

## Exercise 2 — Trace the signal
Draw arrows on the schematic showing:
- AUDIO_IN → OUT2 (dry)
- AUDIO_IN → OUT1 (crushed)

What part of the circuit does time slicing? ____________________________________

## Exercise 3 — Find the sensitive places
Circle three places where wiring sloppiness hurts most.

Write your top 3 and why:

1) __________________________ because ________________________________________
2) __________________________ because ________________________________________
3) __________________________ because ________________________________________

## Exercise 4 — Symptom to likely cause

A) Dry works, crushed silent:
☐ CD4051 not powered  ☐ A/B/C not tied low  ☐ INH stuck wrong  ☐ hold cap to GND  ☐ X0/Z swapped

B) Both outputs silent:
☐ MCP602 not powered  ☐ rails broken  ☐ Vref wrong  ☐ no patch into AUDIO_IN

C) Loud ticking in audio:
☐ missing decoupling  ☐ CLK routed over SAMP_NODE  ☐ hold cap too far  ☐ add +5 decoupling near 555

Pick one symptom you saw (or imagine) and list the checks you would do first:

Symptom: ______________________
Checks: _________________________________________________________________

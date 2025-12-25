# Step 06 — Bonus gates (CD40106)

Power:
- pin 14 +5V, pin 7 GND, 100nF near pins

Gate1:
- 100k: DIST_OUT → pin 1
- pin 2 → GATE1_OUT (LED via 1k optional)

Gate2 (optional filtered):
- 47k: DIST_OUT → EDGE
- 10nF: EDGE → GND
- 100k: EDGE → pin 3
- pin 4 → GATE2_OUT

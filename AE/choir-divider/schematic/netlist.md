# Choir Divider — Pin-Accurate Netlist

## U1 NE555 (optional)
- 8 +5V, 1 GND, 4 +5V
- 2 tied to 6
- 47k: +5V → 7
- 50k pot: 7 ↔ (2/6 node)
- 10uF: (2/6 node) → GND (+ to node)
- 3 → CLK_RAW
- 10nF: 5 → GND
- 100nF: +5V ↔ GND near U1
If internal: CLK_IN = CLK_RAW

## U2 CD40106 (optional)
- 14 +5V, 7 GND, 100nF near pins
- 1 ← CLK_IN
- 2 → CLK_CLEAN
If skipped: CLK_CLEAN = CLK_IN

## U3 CD4017
- 16 +5V, 8 GND, 100nF near pins
- 13 → GND (enable)
- 15 ← RESET (default low)
- 14 ← CLK_CLEAN

Q outputs:
Q0 pin 3, Q1 pin 2, Q2 pin 4, Q3 pin 7, Q4 pin 10,
Q5 pin 1, Q6 pin 5, Q7 pin 6, Q8 pin 9, Q9 pin 11

Early reset:
Qn → diode (anode at Qn, cathode at RESET)
100k: RESET → GND

Pattern OR:
Qn → diode (anode at Qn, cathode at PATTERN)
100k: PATTERN → GND

# Switch Orchard — Netlist (4-channel build, expandable)

## Key nodes
+5V, GND, Z, X0..X7, A, B, C, INH, VSEL, CLK, A_NODE, B_NODE

---

## U1 CD4051 (analog switch)
**Power**
- VDD → +5V
- VSS → GND
- VEE → GND (single-supply)
- 100nF: VDD ↔ VSS close to chip

**Control**
- INH → GND (enabled)
- A, B, C → address lines (C tied to GND for 4-channel mode)

**Signals**
- Z = common
- Use X0–X3 for the workshop core (X4–X7 optional)

> Note: CD4051 pin numbering differs slightly between drawings. Use the notch/dot orientation and a datasheet pinout when wiring.
> In the lab, we identify pins by *label* (A/B/C, INH, Z, X0..X7) rather than number.

---

## U2 CD40106 (Schmitt inverter) — optional but recommended
- pin 14 → +5V
- pin 7 → GND
- 100nF near pins 14/7

Uses:
- Clean/shape A and B signals (and/or build RC oscillator clock)

---

## Manual thresholds (no extra ICs)
- VSEL = pot wiper (pot between +5 and GND)
- T1 divider: 100k (+5→T1), 47k (T1→GND)
- T2 divider: 47k (+5→T2), 100k (T2→GND)

---

## Scanner option
### U3 CD4017
- VDD (+5), VSS (GND), 100nF decouple
- CLK → clock input
- RESET pulled low (100k to GND)

Use Q0–Q3 (1-hot) to build A_NODE and B_NODE via diodes:
- A_NODE = OR(Q1, Q3) with diodes, 100k pull-down
- B_NODE = OR(Q2, Q3) with diodes, 100k pull-down
Then invert to get logic-high sense if needed (40106).

---

## Outputs
- Z jack
- optional: bring X0–X3 to jacks for demux experiments

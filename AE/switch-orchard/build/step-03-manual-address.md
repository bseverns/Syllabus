# Step 03 — Manual addressing (selector knob → A/B/C)

Goal: turn one knob into a stepped selection.

## Simple, robust classroom method
Use **two Schmitt thresholds** to carve the knob into regions.
We’ll build a **4-channel selector** using only A and B (leave C = 0).

### Wiring
- Selector pot: +5V ↔ pot ↔ GND, wiper = VSEL

Create two thresholds with dividers:
- T1 ≈ 1/3 Vcc: 100k from +5 to T1, 47k from T1 to GND  (≈ 1.6V)
- T2 ≈ 2/3 Vcc: 47k from +5 to T2, 100k from T2 to GND (≈ 3.4V)

Use CD40106 as comparators-ish:
- Feed VSEL into two 40106 inputs through 100k (limits current).
- For each comparator, bias against T1/T2 using a resistor mix:
  - Practical build: make two nodes:
    - VSEL_MINUS_T1 (VSEL via 100k, T1 via 100k into same node)
    - VSEL_MINUS_T2 (VSEL via 100k, T2 via 100k into same node)
  - Feed those nodes into 40106 inputs; outputs become BITS.

**Result (coarse):**
- B = (VSEL > T1)
- A = (VSEL > T2)

Set:
- C = 0 (tie to GND)

This yields a simple 4-step walk across X0–X3.

## Check
- Put LEDs on A and B (via 1k) and sweep the knob.
- You should see A and B change state at two points.

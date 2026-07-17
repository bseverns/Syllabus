# Step 02 — Clock: internal 555 (or external AE)

## Breadboard placement map
![Top-down 555 clock breadboard layout](../assets/555-clock-breadboard-layout.svg)

This original map covers the optional internal 555 clock on a standard 17-column mini breadboard. The instructor-approved AE BRAEDBOARD power points, board orientation, and measurements override the map; power off before moving wires.

## Internal NE555 astable (standalone)
- pin 8 → +5V
- pin 1 → GND
- pin 4 → +5V
- tie pin 2 ↔ pin 6
- 47k: +5V → pin 7
- 50k pot: pin 7 ↔ (pins 2/6 node) as variable resistor
- 10uF: (pins 2/6 node) → GND (electrolytic + to node)
- pin 3 = CLK_RAW
- 10nF: pin 5 → GND
- 100nF: +5V ↔ GND near chip

Clock LED:
CLK_RAW → 1k → LED → GND

## External AE clock
Patch AE CLK into CLK_IN node and skip the 555.

Check: you can see pulses on CLK_IN/CLK_RAW.

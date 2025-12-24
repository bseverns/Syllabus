# Step 04 — Scanner mode (optional): clocked stepping

This section turns the selector into a walking router.

## Clock source
Use an AE clock input, or build a simple clock:
- CD40106 RC oscillator (one gate):
  - 100k from output to input
  - 100nF from input to GND
  - output is CLK
(If your kit already has a 555 clock workshop, you can reuse it.)

## Step counter (CD4017)
- Power 4017 (+5V/GND + 100nF).
- CLK → 4017 clock pin
- Keep RESET low with 100k to GND.
- Take Q0–Q3 as 1-hot stepping.

## Translate 1-hot → 2-bit address (A/B)
We need A/B to represent 0–3. Easiest: diode OR encoding.

- A should be HIGH on steps 1 and 3:
  - Q1 → diode → A_NODE
  - Q3 → diode → A_NODE
  - 100k pull-down A_NODE → GND
  - A_NODE → 40106 inverter → A

- B should be HIGH on steps 2 and 3:
  - Q2 → diode → B_NODE
  - Q3 → diode → B_NODE
  - 100k pull-down B_NODE → GND
  - B_NODE → 40106 inverter → B

C stays 0 (GND).

## Mode switch
Use your slide switch to choose:
- Manual A/B from knob, or
- Scanner A/B from the 4017 encoder.

## Check
- LEDs on A/B should cycle through 00, 01, 10, 11 with the clock.

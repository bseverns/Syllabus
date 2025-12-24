# Step 02 — CD4051 core wiring (router)

## Power pins (CD4051)
- VDD → +5V
- VSS → GND
- VEE → GND (for single-supply operation)
- 100nF decoupler near VDD/VSS

## Control pins
- INH (inhibit) → GND  (enabled)
- A, B, C will be wired later

## Signal pins
Pick a direction for your module:

### Mode A: 8-to-1 MUX (many inputs → one output)
- Z = output (goes to AE destination)
- X0..Xn = inputs (signals to select)

### Mode B: 1-to-8 DEMUX (one input → many outputs)
- Z = input
- X0..Xn = outputs

Start with 4 channels (X0–X3) so the lab stays finishable.

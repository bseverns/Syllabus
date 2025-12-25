# Step 03 — Drive stage (MCP602 U1B) clean first

- pin 5 (+) → BUF
- pin 6 (−) = DRIVE_NEG
- 10k: DRIVE_NEG → Vref
- 100k (or pot): pin 7 (OUT) → DRIVE_NEG
- pin 7 → DIST_OUT
Check: DIST_OUT louder, still centered at Vref.

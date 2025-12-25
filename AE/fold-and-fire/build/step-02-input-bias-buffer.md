# Step 02 — Input bias + buffer (MCP602 U1A)

- Audio IN → 100nF → IN_AC
- 100k: IN_AC → Vref

MCP602 power:
- pin 8 +5V, pin 4 GND, 100nF near pins

U1A follower:
- pin 3 → IN_AC
- pin 2 tied to pin 1
- pin 1 → BUF (DRY)
Check: BUF idles near Vref.

# Step 04 — CD4017 counting

Power:
- pin 16 → +5V
- pin 8 → GND
- 100nF near pins 16/8

Control:
- pin 13 (CLK INH) → GND (enabled)
- pin 15 (RESET) → GND initially

Clock:
- pin 14 (CLK) → CLK_CLEAN

Test:
- Put LED on Q0 (pin 3): Q0 → 1k → LED → GND
Move the LED to other Q pins to watch the count.

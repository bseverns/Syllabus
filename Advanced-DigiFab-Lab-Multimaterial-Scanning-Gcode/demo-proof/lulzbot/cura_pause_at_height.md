# LulzBot (Cura LulzBot Edition) — Pause to Color‑Swap (Token Demo)

1. Open Cura LulzBot Edition and load `../assets/ADL-demo-token_40x3.stl`.
2. Choose **PLA Balanced (0.5 mm nozzle)** or your local preset. Set **layer height = 0.25 mm**.
3. Go to **Extensions → Post Processing → Modify G‑code → Add “Pause at height”**.
   - Mode: **Layer No.**
   - Layer: **5** (≈ 1.25 mm)
   - Standby temperature: near print temp (e.g., 200–205 °C).
   - Park X/Y: safe edge; Park Z: +10 mm.
4. Slice and save G‑code. Print, then swap filament at the pause and resume.
5. Use the dual‑fleet filename schema; log in `print-queue-log_dual-fleet.csv`.

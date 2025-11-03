# LulzBot (Cura LE) — Pause/Color Swap

1. Load `../assets/MECH-demo-token_40x3.stl`; select **PLA Balanced (0.5 mm)**.
2. Set **layer height** 0.25 mm.
3. **Extensions → Post Processing → Modify G-code → Pause at height**:
   - Mode: **Layer No.**; Layer: **5**
   - Standby 200–205 °C; Park X/Y safe edge; raise Z +10 mm.
4. Slice, save G-code, print; swap filament at pause and resume.

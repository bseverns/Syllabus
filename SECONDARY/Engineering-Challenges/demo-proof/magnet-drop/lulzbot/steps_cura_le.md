# LulzBot (Cura LE) — Magnet Drop

- Export STL from `assets/magnet_token.scad` with your parameters.
- Defaults give **Z_pause = base_t + magnet_t = 3.2 mm** (1.2 + 2.0).
- With layer 0.25 mm → ~**Layer 13** (use `scripts/pause_calc_magnet.py`).

**Add Pause:** Extensions → Post Processing → Pause at height → Height **3.2 mm**.  
Park X/Y safe edge; Z +10 mm; standby near print temp. Drop magnet flat, verify it’s **below** the last layer; resume.

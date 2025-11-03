# LulzBot (Cura LulzBot Edition) — Magnet Drop Demo

**Model:** `../assets/magnet_token.scad` (export STL after setting params)  
**Defaults:** token Ø40 mm, 10×2 mm magnet, base 1.2 mm, cover 1.0 mm → total ~4.2 mm

## Slice
1. Open the STL exported from `magnet_token.scad` and select your LulzBot Mini 2/3 profile (PLA Balanced 0.5 mm).
2. Set **layer height** (e.g., 0.25 mm). Compute pause layer at:  
   **Z_pause = base_t + magnet_t** → 1.2 + 2.0 = **3.2 mm** → ≈ layer **13** at 0.25 mm (use the pause calc script).

## Add pause
- **Extensions → Post Processing → Modify G-code → Add “Pause at height”**  
  - Mode: **Height**  
  - Height: **3.2 mm** (or the nearest layer-top)  
  - Park: X safe edge, Y front; Z raise +10 mm  
  - Standby temperature: ~200–205 °C (PLA)

## Procedure
- Print until paused. Drop the 10×2 mm magnet into the pocket **flat** (check polarity if making a set).  
- Ensure magnet sits **below** the top of the printed layer (flush or slightly recessed).  
- Resume; the printer will cover it with **cover_t** mm of plastic.

> Safety: Keep fingers/tools clear when resuming. If the magnet rides proud, **abort** to avoid nozzle crash.

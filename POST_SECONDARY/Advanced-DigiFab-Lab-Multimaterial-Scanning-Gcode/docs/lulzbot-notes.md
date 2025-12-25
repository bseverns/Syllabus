# LulzBot Mini 2 / Mini 3 — Tuning Notes (Cura)

These presets are conservative, reliability-first starting points tailored for typical LulzBot Minis with 0.5 mm nozzles and PEI beds.

## General guidance
- **Nozzle:** 0.5 mm (default). If you use 0.4 mm, drop layer heights accordingly.
- **First layer:** 0.32–0.36 mm with slower outer walls for strong adhesion.
- **Retraction (direct drive):** PLA 0.8–1.2 mm @ 25–35 mm/s; PETG 0.6–1.0 mm @ 20–30 mm/s.
- **Cooling:** PLA 100% after layer 2; PETG 30–50%; ASA minimal (enclosed, ventilated per policy).
- **Bed surface:** PEI — use **glue stick as a release agent** for PETG to avoid damaging the sheet.
- **Leveling:** If your firmware supports on-print mesh (**G29**), use the G29 start variant. If you precalibrated and saved a mesh, enable it with **M420 S1**.
- **Wiper pad / nozzle clean:** If your machine has a wiper, include a wipe macro before printing. If not, purge to the edge with a wipe line.

## What’s here
- Cura profiles (`.curaprofile`) for **PLA Draft / Balanced**, **PETG Balanced**, **ASA Enclosed**.
- Two start G-code variants (**G29 each print** vs. **M420 saved mesh**), plus a generic End G-code.
- Checklists for Mini startup and filament changes.

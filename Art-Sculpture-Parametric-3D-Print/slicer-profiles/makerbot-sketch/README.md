# MakerBot Sketch — Digital Factory Presets & Workflow

**Context:** These presets mirror Cura-like parameters inside **UltiMaker Digital Factory** for the Sketch fleet. Treat them as *recipes* to re-create inside the DF UI; export options for native profiles are limited, so we document the knobs here for reproducibility.

## Queue conventions
- **Queue name:** `Parametric-Week##_Team##`
- **Job name:** `L##_study-[technique]-[material]-[quality]` (e.g., `L05_study-vase_PLA_draft`)
- **Notes field:** record `nozzle=0.4 | layer=0.24 | walls=1 | top=0 | bottom=3 | flow=98`

## Presets
- Import the matching preset `.md` and mirror the values in DF.
- If **Spiralize (vase mode)** toggle is missing, emulate by: `walls=1`, `top=0`, `bottom=3`, **seam = aligned**, **z-hop off**, and slower print speeds.

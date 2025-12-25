# Demo‑Proof: Single STL → MakerBot + LulzBot

This folder demonstrates the **dual‑fleet** pipeline with one canonical STL: `assets/ADL-demo-token_40x3.stl` (40 mm × 3 mm).  
Goal: produce a two‑color token by pausing at ~1.2–1.3 mm and swapping filament.

## Steps overview
1) Use the **same STL** for both slicers.  
2) Slice separately: **MakerBot** (job package) and **LulzBot** (G‑code).  
3) Pause at the chosen layer/height, swap filament, resume.  
4) Log both jobs with the same naming key in `templates/print-queue-log_dual-fleet.csv`.

Why this works: color‑swap = time‑based feature; it doesn’t rely on vendor‑specific G‑code.

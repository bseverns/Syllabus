# MakerBot SKETCH — Pause to Color‑Swap (Token Demo)

1. Import `../assets/ADL-demo-token_40x3.stl` and select your preset (Draft or Balanced).
2. Note your **layer height** (e.g., 0.25 mm). Compute the pause layer: 1.25 mm / 0.25 mm ≈ **5**.
3. In the MakerBot UI, schedule a **pause** around layer **5** (or the closest supported height).
4. Start the job. When paused, **swap filament**, purge a small amount away from the part, and resume.
5. Name the job file using the dual‑fleet schema (see `docs/dual-fleet-pipeline.md`).

Tip: Place seam/alignment toward a less‑visible edge to hide the color change transition.

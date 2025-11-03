# Dual‑Fleet Pipeline: MakerBot (SKETCH) + LulzBot (Mini 2/3)

You can run both ecosystems in one class by **separating slicing** but **standardizing assets and metadata**.

## Design assets (shared)
- Keep **source CAD** and **STL/3MF** canonical in `/assets/` (per project).
- Use the **same STL** to produce two outputs: MakerBot job package and LulzBot G‑code.

## Slicing (separate)
- **MakerBot SKETCH**: slice with MakerBot software (or Digital‑Factory‑connected workflow) that produces a **printer‑specific job package**. Do **not** send raw G‑code to MakerBot.
- **LulzBot Mini 2/3**: slice with **Cura LulzBot Edition** to standard **G‑code** using the profiles in `slicer-profiles/lulzbot-mini2/` or `lulzbot-mini3/`.

## Naming
Use a single schema so both outputs stay matched:
```
<course>-<lesson>-<project>-<team>-<material>-<quality>.<ext>
# example:
ADL-L06-startend-demo-T2-PLA-draft.gcode        (LulzBot)
ADL-L06-startend-demo-T2-PLA-draft.makerbot     (MakerBot job package)
```
(Extension shown for illustration; your MakerBot software decides the exact package extension.)

## Logs
- Add **machine** and **slicer** columns to your queue log (see `templates/print-queue-log_dual-fleet.csv`).
- Keep **parity**: aim for similar layer heights, perimeters, and speeds across fleets.

## Inserts / Pauses
- **LulzBot**: use Cura LE “Pause at height” or insert `M0/M600` if supported by firmware.
- **MakerBot**: use the MakerBot UI to schedule pauses; do not edit job packages by hand.

## Start / End
- **LulzBot**: use the provided start/end G‑code variants (G29 vs. M420).
- **MakerBot**: rely on the built‑in machine procedures in job packages.

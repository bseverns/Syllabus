# Engineering Challenges with 3D Printed Mechanisms — Course Repo

**Grade band:** 8–12 • **Duration:** 10–12 weeks (A/B blocks per session) • **Prereqs:** Intro CAD/printing

Students design, print, and test **working mechanisms**: gears, cams, ratchets, linkages, compliant hinges, snap‑fits, and simple transmissions. Each challenge couples **design-for-printability** with **measurable engineering targets** (speed reduction, lift height, repeatable indexing, grasp force, etc.). The repo ships with week‑by‑week lessons, teacher guides, student briefs, printable **rigs** for testing, parametric OpenSCAD templates, rubrics, checklists, and analysis helpers.

## Quick start
- Read the **Course Outline**: [`/syllabus/course-outline.md`](syllabus/course-outline.md).
- Print the core **rigs** from [`/activities/rigs`](activities/rigs).
- Start with **Mechanism Templates** in [`/activities/mechanisms`](activities/mechanisms).
- Pick a **challenge** from [`/challenges`](challenges/) and use the **logs & rubrics** in [`/assessments`](assessments/).

## Repo map
- `syllabus/` – scope & sequence, standards.
- `lessons/` – A/B block daily plans (Teacher + Student).
- `activities/` – parametric mechanism templates + test rigs.
- `challenges/` – project briefs (rubric-aligned).
- `assessments/` – rubrics and checkpoints.
- `slicer-profiles/` – notes + conservative presets (see prior repos for fleet‑specific profiles).
- `checklists/` – safety, rig setup, test-day flow, failure analysis.
- `templates/` – logs, BOMs, design notebook, presentation deck.
- `docs/` – mechanisms primer, tolerances, measurement methods, diagrams.
- `scripts/` – small calculators (gear ratio, torque from mass).
- `policies/` – privacy & ethics.
- `LICENSES/` – CC BY 4.0 (content) + MIT (code).


**Vendor presets:** See `slicer-profiles/lulzbot-mini2/` and `slicer-profiles/lulzbot-mini3/` for Cura LE recipes and start/end G‑code. See `docs/dual-fleet-pipeline.md` for running MakerBot + LulzBot together.


See `demo-proof/` for a paired **dual-fleet color-swap** demo and a **magnet-drop insert** demo.

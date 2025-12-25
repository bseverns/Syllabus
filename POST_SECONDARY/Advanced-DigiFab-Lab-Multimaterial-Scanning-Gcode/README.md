# Advanced Digital Fabrication Lab — Multi‑Material, Scanning & G‑code Hacks

**Grade band:** 11–12 • **Duration:** 14–16 weeks (semester) • **Prereqs:** Intermediate CAD & 3D printing

This capstone treats students as **junior technicians** operating a small print lab. We cover **multi‑material workflows** (MMU/AMS & manual swaps), **3D scanning pipelines** (photogrammetry + handheld), and **G‑code customization** (start/end, conditional pauses, insert workflows). The repo includes a week‑by‑week syllabus with A/B blocks, lesson plans (Teacher/Student), maintenance & QC checklists, calibration artifacts, scanning guides, multi‑material templates, slicer recipes, assessment rubrics, and simple analytics scripts for print logs and G‑code parsing.

## Quick start
- Read the **Course Outline**: [`/syllabus/course-outline.md`](syllabus/course-outline.md).
- Prep the lab with **Opening/Closing** checklists: [`/checklists`](checklists/).
- Print calibration artifacts from [`/activities/calibration`](activities/calibration).
- Choose your **multi‑material path**: `slicer-profiles/prusaslicer` (MMU), `bambu/` (AMS notes), or `makerbot-sketch/` for manual color swaps.
- Explore **G‑code hacks** in [`/activities/gcode-hacks`](activities/gcode-hacks).

## Goals
- Operate a multi‑printer lab safely; triage queues; maintain uptime.
- Execute multi‑material/color workflows and **soluble supports** with minimal waste.
- Capture/clean 3D scans; integrate with parametric CAD for hybrid parts.
- Author and reason about **G‑code edits** (pauses, inserts, conditional logic) and measure their effects.
- Produce a **portfolio**: capstone piece, process logs, and an ops/maintenance vignette.

## Repo map
- `syllabus/` – semester plan, standards alignment.
- `lessons/` – 14 day folders (Teacher/Student A/B blocks).
- `activities/` – calibration, multi‑material demos, scanning workflow, G‑code hacks.
- `assessments/` – rubrics and checkpoints.
- `slicer-profiles/` – PrusaSlicer (MMU), Bambu AMS notes, Cura & MakerBot manual‑swap recipes.
- `checklists/` – opening/closing, nozzle swaps, changeovers, QC.
- `templates/` – queue log, maintenance log, QC checklist, capstone proposal, portfolio index.
- `data/` – CSV examples.
- `docs/` – diagrams, troubleshooting, terminology, reading list.
- `policies/` – privacy & ethics for documentation.
- `scripts/` – simple G‑code parser + KPIs for queue logs.
- `LICENSES/` – CC BY 4.0 (content) + MIT (code).

See **CONTRIBUTING** for how to adapt to your lab.


**Vendor presets:** See `slicer-profiles/lulzbot-mini2/` and `slicer-profiles/lulzbot-mini3/` for Cura recipes and start/end G-code tuned for Mini 2/3.


See `demo-proof/` for a **paired demo** (single STL → MakerBot job + LulzBot G-code with color-swap pause).

See `demo-proof/magnet-drop/` for a **magnet drop** insert demo (OpenSCAD model + LulzBot/MakerBot steps + pause snippets).
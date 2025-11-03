# Design for Printability & Function — Course Repo

**Grade band:** 7–9 • **Duration:** 10 weeks (A/B blocks per session) • **Prereqs:** 3D printing foundations (or equivalent)

This repository contains everything needed to run an intermediate 3D printing course that emphasizes **constraint‑based CAD**, **printability rules**, and **functional design**. It includes lesson plans with A/B blocks, teacher guides, student handouts, OpenSCAD test artifacts (overhang, bridge, tolerance, snap‑fit), assessment rubrics, slicer profiles, data templates for strength tests, and operations checklists.

## Quick start
- See [`/syllabus/course-outline.md`](syllabus/course-outline.md) for the full scope & sequence.
- Start prep with the **Teacher Day‑0 Checklist**: [`/checklists/day0-teacher-setup.md`](checklists/day0-teacher-setup.md).
- Print the **test artifacts** from [`/activities/openscad-tests`](activities/openscad-tests) before Week 3.
- Use the provided **rubrics** in [`/assessments/rubrics`](assessments/rubrics) and **templates** in [`/templates`](templates).
- If you modify slicer profiles, version them in [`/slicer-profiles`](slicer-profiles/).

## Course goals
- Apply **printability constraints** (overhangs, bridging, wall thickness, supports, orientation) during CAD—**not** after the fact.
- Design, prototype, and test **functional assemblies** with **tolerance control** and **snap‑fit** strategies.
- Compare **slicer parameters** vs. **mechanical performance** using structured tests and simple data analysis.
- Produce a capstone **locking container** that assembles cleanly and passes fit / drop / shake tests.

## Repo map
- `syllabus/` – scope & sequence, pacing, standards alignment.
- `lessons/` – day-by-day plans with **A/B block** structure (Teacher + Student versions).
- `activities/` – OpenSCAD test pieces, failure analysis labs, fit gauges.
- `assessments/` – rubrics, checkpoints, reflection prompts.
- `slicer-profiles/` – starter profiles and notes for Cura/PrusaSlicer/MakerBot.
- `checklists/` – safety, machine setup, QA.
- `templates/` – proposal, design review, test logs, reports.
- `data/` – CSV templates and example logs.
- `docs/` – diagrams (Mermaid), reading list, terminology.
- `policies/` – privacy & ethics for classroom documentation.
- `scripts/` – optional analysis tools for class datasets.
- `LICENSES/` – dual license: CC BY 4.0 (content) + MIT (code/SCAD).
- `.gitignore` – standard ignores for CAD/prints.

See **CONTRIBUTING** for suggestions on class forks and local customization.

# Robotics → FPV (15 Weeks × 1.5 h)

A practical arc from ground robots to first‑person‑view flight for high‑performing middle‑schoolers and high‑schoolers.
Students start with **Arduino I/O + voltage control** on a driving base, learn **soldering & harness craft**, then **build, configure, and fly** sub‑250 g FPV whoops. Designed for **10 teams** (2–3 students/team).

## Learning Goals
- Understand I/O, PWM, voltage domains (3.3 V vs 5 V), current limits, motor control, and sensor feedback.
- Explain the flight stack: ESC↔BLDC, IMU, PID, radio links, VTX/OSD, goggle reception.
- Execute safe soldering, LiPo handling, bench tests, and field repairs.
- Fly LOS → stabilized → acro; practice checklists; reflect via DVR logs and pilot journals.
- Operate within ethical & legal boundaries (spotter discipline; TRUST; sub‑250 g best practices).

## Repo Layout
- `syllabus.md` — 15‑week plan and milestones.
- `curriculum/week-XX.md` — step‑by‑step lesson plans (materials, drills, assessment).
- `build/FPV-whoop-BOM.csv` — per‑team parts list (sub‑250 g analog whoop).
- `build/Classroom-kit-BOM.csv` — shared lab tools, safety gear, and spares.
- `safety/FPV-Safety-and-Policy.md` — TRUST / VLOS / LiPo / VTX notes.
- `assessments/Bench-Check-Checklist.md` — continuity → smoke‑stop → arming.
- `assessments/Flight-Checkride-Checklist.md` — hover box → figure‑8 → gates.
- `assessments/Pilot-Logbook.csv` — per‑pilot journal template.
- `sim/Setup.md` & `sim/Drill-Cards.md` — simulator setup + progressive drills.
- `checklists/*` — charging station, crash recovery, classroom ops placards.

## Quickstart (Instructor)
1. **Clone** this repo and print the checklists in `checklists/` and `assessments/`.
2. **Stage** zones: solder lab, charging station, flight cage/gates, bench test table.
3. **Choose a simulator** (VelociDrone or FPV Freerider) and set up radios for USB.
4. **Procure parts** per `build/*.csv` (buy +20% motors/props, +2 AIOs, extra batteries).
5. **Prep bind phrases** (ELRS) and a **VTX channel plan** (25 mW cap indoors).
6. During class: run each `curriculum/week-XX.md`, collect pilot logs, film check‑rides.

> **Disclaimer:** Regulations and school/district policies evolve. Use the safety doc as a **starting point**, then align with current FAA rules and local requirements before flying or transmitting video in your area.

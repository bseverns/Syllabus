# Curriculum Student–Facilitator Support Rollout Plan

**Goal:** Improve only the active primary/secondary offerings where a learner or facilitator must currently invent a documented choice; preserve packages that already work and pilots that need delivery evidence.

**Strategy:** Work one scheduled course at a time. Reuse its existing session plans, cards, checklists, and LMS posts before creating a new document. The smallest acceptable change is an immediate learner action plus a facilitator launch/recovery path, with safety/privacy boundaries at the exact live moment.

## Current baseline

- **Completed:** Lunch Lab student cards + facilitator resources; Lo-Fi Beat Laboratory quickstart/project card; Game Tech facilitator prep and MakeCode link.
- **This pass:** Robotics → FPV learner card, improved simulator drills, and simulator resource links.
- **Keep readiness honest:** no desk-review promotion from `PILOT` to `GO`.

## Queue

### 1. Finish the active Robotics → FPV pass now

- Use `SECONDARY/Robotics-to-FPV-Course/STUDENT_LAB_AND_FLIGHT_CARD.md` as the course-wide student launch point.
- Keep existing `sim/Drill-Cards.md`, bench check, flight checkride, crash recovery, and pilot logbook as the detailed surfaces.
- After one real delivery, record the actual point of confusion. Add a weekly student card only if the course-wide card and existing checklist failed to cover it.

### 2. Complete already-identified delivery prerequisites before adding documents

- **Game Tech Intensive:** build and classroom-test one Scratch starter/remix, then paste its exact URL into `SECONDARY/hs-game-tech-intro/9th-scratch/GOOGLE_CLASSROOM_9TH_SCRATCH.md`. Do not check in an untested generic `.sb3`.
- **Lo-Fi Beat Laboratory:** run the package once; collect which DAW, headphones, safe recording zones, and fallback path actually worked. Update only the point that failed.
- **Primary K–2 pilots:** Tiny Machines, Build a Neighborhood, Sound Hunters, Code With Your Body, Light/Color/Shadow, and Chain-Reaction Playground explicitly need a delivery review. Do not add handout trees before that evidence exists.

### 3. Preserve packages that already meet the support standard

Do not create parallel guides for Digital Manufacturing, StringField Studio, AI in Your Feed, AI at Work, or DIY Local AI. Their existing student/facilitator surfaces are already substantial. Repair a specific defect when a scheduled delivery identifies one.

### 4. Audit the next robotics-family package only when it is scheduled

Audit one of `SECONDARY/HS_Drone_Racing_League`, `SECONDARY/TinyWhoop-Workshop`, `SECONDARY/Robotics_HS_SpikePrime`, or `SECONDARY/robotic-vibes` when a concrete delivery is planned. First read its README, learner prompts, materials/setup, safety, assessment, catalog status, and the closest related package. Do not infer a gap from a filename.

### 5. Treat archive and post-secondary materials as source lineage

Do not normalize `PRIMARY/MPS_comEd`, `PRIMARY/SMM`, or post-secondary packages into the current delivery shape unless a specific offering is being revived. Preserve history; package the requested offering rather than refactoring the archive.

## Repeatable per-course pass

1. Start from `catalog/menu.json` and the course README; confirm audience, readiness, and scheduled use.
2. Trace each learner action to an existing handout/card/session prompt and each facilitator action to setup/materials/safety/assessment.
3. If both paths are usable, stop. If not, repair the existing surface first.
4. Add one direct launch document only when the gap spans the course; otherwise patch the specific live session/card.
5. Put privacy, machine, battery, recording, or field-work boundaries at the live action, not only in a general policy.
6. Verify local Markdown links, added official links, `git diff --check`, and `python3 -m unittest discover -s tests -v`.
7. Record delivery evidence and promote/readjust only after a real run.

## Definition of done for one pass

- A student can begin the next task without waiting for narration.
- A facilitator can preflight tools/materials and recover from the documented failure.
- Every documented option has a real tool/material/fallback or is removed.
- Readiness, catalog claims, and safety boundaries remain truthful.

<!-- ponytail: one-course-at-a-time triage avoids a speculative repository-wide handout rewrite; expand only from delivery evidence. -->

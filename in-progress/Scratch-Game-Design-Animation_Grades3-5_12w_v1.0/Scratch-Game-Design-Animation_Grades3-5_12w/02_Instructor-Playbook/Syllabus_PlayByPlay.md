# Scratch Game Design + Cutscenes Lab (Grades 3–5) — Instructor Play-by-Play (12 Weeks)

This document is the “how to run it” guide: routines, pacing, checkpoints, scripts, and troubleshooting.
For detailed session plans, see: `Sessions/Session_XX_*.md`.

---

## Course success conditions
Students leave with a game that includes:
- **Menu / beginning**
- **Level 1** with clear win condition
- **Cutscene 1** between levels (broadcast-driven; player controls frozen)
- **Level 2** with a new mechanic or a meaningful twist
- **Ending** (win and/or game over)

---

## Classroom operating system (for a very active group)

### The weekly rhythm (same every week)
**0:00–0:05 | Launch Circle**
- “Eyes on me — hands off keys.”
- Today’s mission: one sentence.
- 1-minute demo of the *exact* thing they will build.

**0:05–0:12 | Micro-lesson**
- Teach only today’s blocks.
- Build one tiny example.
- Stop before attention fractures.

**0:12–0:42 | Build Sprints**
- Sprint A: 12 minutes
- Reset: 3 minutes (stand up, stretch, breathe)
- Sprint B: 12 minutes
- Reset: 3 minutes (save + title)
- Sprint C: 12 minutes (extensions or catch-up)

**0:42–0:52 | Playtest Rotation**
- 2 rounds x 5 minutes
- Use a simple form: “Two Stars + One Wish”
- Each tester must identify one bug/confusion.

**0:52–1:00 | Share + Save**
- 2–3 quick shares
- Everyone writes: “Next time I will…”

### Roles (rotate weekly)
- **Debugger:** checks scripts start with events; hunts duplicates
- **Artist:** helps with costumes/backdrops; keeps style consistent
- **Storykeeper:** tracks what happens in cutscenes
- **Playtester:** leads feedback and writes “wishes”
- **Block Finder:** flips through block categories to locate needed blocks

### Attention supports
- Use a visible **noise level** (0–3).
- Use a visible **timer** for sprints.
- Use “show me your hands” pauses before demos.
- Keep demos under 7 minutes; if you must go longer, split into two demos.

---

## Teacher prep (before Week 1)
1. Confirm devices can open Scratch and save projects.
   - If using Piper kits without keyboards: plan a Week 1 setup sprint to build a GPIO keyboard using the Piper app (mouse-only start).
2. Decide account strategy (individual logins vs class studio).
3. Print Handout 00 (Piper Keyboard Build) plus the 6 core handouts in `03_Handouts/`.
4. Create (or rehearse) a minimal **starter template** concept:
   - variables: `level`, `score`, `lives`, `controlsOn`
   - broadcasts: `start game`, `freeze`, `unfreeze`, `level complete`, `reset`, `game over`
   - backdrops: `Menu`, `Level1`, `Cutscene1`, `Level2`, `Win`, `GameOver`

You do *not* need to distribute a full template file yet; the architecture is enough to keep projects stable.

---

## Common patterns (teach these early)

### Pattern A — Controls gate
Player movement runs only when `controlsOn = 1`.

### Pattern B — Scene transitions
Touch “Door” → broadcast `level complete` → switch backdrop → broadcast `unfreeze`.

### Pattern C — Reset
When `reset`:
- player returns to start
- hazards return to start
- collectibles reposition
- controlsOn returns to 1

---

## Assessment (lightweight and fast)
Use weekly “milestone unlocks”:
- Working / Not Yet
- Keep it binary; save your energy for coaching.

See: `Assessment_Rubrics.md`

---

## What to do when the room gets loud
- Pause. Hands off keys. Breathe.
- Give one crisp instruction.
- Restart the timer.
- Praise the behavior you want to replicate (“I see 3 teams already saving.”)

---

## Files in this playbook
- Session plans: `Sessions/`
- Routines + behavior supports: `Classroom_Routines.md`
- Differentiation: `Differentiation_and_Behavior_Supports.md`
- Troubleshooting: `Troubleshooting_Guide.md`
- Assessment + rubrics: `Assessment_Rubrics.md`


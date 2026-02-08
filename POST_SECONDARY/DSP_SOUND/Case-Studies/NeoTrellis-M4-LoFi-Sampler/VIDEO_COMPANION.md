# Video companion — Lo‑Fi Sampler walkthrough (8–10 minutes)

This companion assumes you’re filming from the demo exercises:
`DEMO_EXERCISES.md`

Goal: a walkthrough that is **brief, complete, and reproducible**.

## Minimal shot + overlay plan
- **Camera:** overhead grid (primary), optional macro (secondary), optional face cam (intro/outro only)
- **Audio:** direct capture from the sampler output (primary)
- **Overlay (persistent):**
  - `Shift: velocity / record / stutter`
  - `Alt: probability / undo`
  - `Shift+Alt: FX / reslice`
- Always show **BPM** on screen when demonstrating clocked behavior.

## Suggested chapters
00:00 Cold open (the sampler plays)  
00:15 What it is + where the exercises live  
00:45 (Ex1) Clocked grid  
01:45 (Ex2) Phase drift  
02:35 (Ex3) Offset latches  
03:20 (Ex4–5) Velocity + probability lanes  
04:30 (Ex6) Stutter gesture  
05:05 (Ex7) Record + auto‑slice  
06:10 (Ex8) Undo + reslice  
06:55 (Ex9) FX + “boring ISR” rule  
08:00 (Ex10) Factory restore  
08:45 Wrap

## Narration script (tight, aligned to the exercises)
Use this as a read‑through. Keep transitions short.

### Intro
“This is the NeoTrellis M4 Lo‑Fi Sampler: four rows, one sample per row, and an 8‑step grid locked to a global MIDI clock.  
I’m going to run ten stand‑alone exercises—each one explains what the sampler does *and* why it’s designed this way.”

### Exercise 1 — Clocked Grid
“Clock is the spine. Steps only advance on clock ticks. Stop freezes. Continue resumes on the current step.  
The point is deterministic timing even when UI and storage are busy.”

### Exercise 2 — Phase drift
“Rows A and B share the same gates, but their source lengths differ. Equal slicing on a fixed grid makes the phase relationship drift over bars.  
Complexity from simple inputs.”

### Exercise 3 — Offset latches
“Alt and Shift live one row down so every track keeps a full 8‑step lane.  
The music surface stays the music surface.”

### Exercises 4–5 — Expression lanes
“Velocity lanes are discrete: fast, reliable dynamics.  
Probability lanes add controlled randomness without UI explosion.”

### Exercise 6 — Stutter
“Shift‑tap fires a stutter blast but doesn’t rewrite the pattern.  
Expression without side effects.”

### Exercise 7 — Record + auto‑slice
“Recording writes `source.raw` and immediately cuts eight slices so the grid stays stable.  
Every take becomes a predictable layout.”

### Exercise 8 — Undo + reslice
“Alt restores the previous take if it exists. Shift+Alt+Step6 reslices the current source without touching gates.  
You can experiment without losing the pattern.”

### Exercise 9 — FX + boring ISR
“FX feel immediate, but the audio interrupt stays boring: it reads deterministic tables.  
Slow work happens in the foreground job queue so playback doesn’t glitch.”

### Exercise 10 — Factory restore
“Press `f` in a serial monitor to restore the factory demo from a manifest.  
Teaching boards reset without reflashing firmware.”

### Outro
“That’s the sampler: clocked grid, expressive lanes, live capture, safe recovery—built around a stable audio engine.  
The full steps are in `DEMO_EXERCISES.md`, and `MODULE_CROSSWALK.md` links each exercise to deeper DSP_SOUND modules.”

## Description / pinned comment block (copy/paste)
- Demo steps: `DSP_SOUND/Case-Studies/NeoTrellis-M4-LoFi-Sampler/DEMO_EXERCISES.md`
- Curriculum pointers (per exercise): `DSP_SOUND/Case-Studies/NeoTrellis-M4-LoFi-Sampler/MODULE_CROSSWALK.md`

_Last updated: 2026-02-08_

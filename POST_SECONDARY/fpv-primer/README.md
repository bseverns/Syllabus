# fpv-primer

A lightweight, workshop-friendly on-ramp to FPV as a *systems practice*—power, radio, control loops, telemetry, safety rituals, and the strange beauty of flying instruments.

This repo is meant to sit *next to* project repos like **drone-chorus**:
- **drone-chorus** = the living field manual + art system
- **fpv-primer** = the shared foundation that keeps the ocean learnable

## Who this is for

- Makers who can solder and code but feel new to FPV
- Educators who need a reliable “props-off first” sequence
- Artists who want telemetry as material (without treating safety as optional)

## Core doctrine

1. **Props-off until the system proves itself.** Bench replay is not a shortcut—it’s the ground truth.
2. **Treat telemetry as a contract.** Define semantics, ranges, and failure behavior before you map anything.
3. **Mappings are compositions.** Don’t just route values—shape them (curves, deadbands, smoothing, limits).
4. **Safety nets are features.** “Undo,” “safe mode,” and “known-good reset” are part of the instrument.
5. **Ship artifacts.** Every session ends with something reproducible: a mapping sheet, a log, a preset, a clip.

## Quickstart paths

### Path A: Bench-only (recommended first)
1. Read: `docs/01-safety-and-props-off.md`
2. Read: `docs/04-betaflight-minimum-viable-setup.md`
3. Run: `labs/lab00-bench-sim.md`
4. Run: `labs/lab01-telemetry-to-midi.md`

### Path B: Teaching sequence (2–3 sessions)
- Session 1: Safety + parts map + bench doctrine
- Session 2: Betaflight minimum viable telemetry + logs
- Session 3: Mapping cookbook + musical tests (Drone Chorus style)

### Path C: Field sequence (after bench competence)
- Build checklist → arming discipline → short flights → post-flight review
- Always return to: semantics, logs, mapping, stability

## What you’ll find here

- **docs/**: primers, checklists, semantics, and capture workflows
- **labs/**: repeatable exercises (bench-first)
- **templates/**: mapping sheets and log templates you can copy per project

## Safety + responsibility (read this)
This repo is **not** a substitute for manufacturer manuals, local laws, common sense, or supervised instruction. FPV equipment can cause injury, fire, and property damage. Start with small batteries, remove props for bench work, and treat every power-up as live. When in doubt: stop, ask, and re-check.

## How this connects to Drone Chorus
Drone Chorus needs FPV fluency, but it shouldn’t *teach FPV from scratch* in its own README. This repo holds the shared foundation, then Drone Chorus can stay focused on:
- telemetry → smoothing → MIDI CC
- mapping-as-composition
- patch design + performance practice
- robust capture + repeatable demos

## Roadmap (lightweight)
- [ ] Fill docs stubs with “minimum viable” text + diagrams
- [ ] Add one reference wiring photo per concept (optional)
- [ ] Add a “telemetry semantics table” that matches Drone Chorus mappings
- [ ] Add a troubleshooting decision tree that starts from symptoms

---

## Suggested video companion (optional)
If you’re filming: treat each lab as a short episode.
**Goal → Steps → Observe → Why → Artifact**

Artifacts can be: mapping YAML, log CSV, short A/B clip, or a screenshot of Betaflight settings.

# fpv-primer

A post-secondary, workshop-friendly on-ramp to FPV as a *systems practice*:

- power and energy handling
- radio and control links
- video transport
- control loops and tuning
- telemetry and semantics
- safety rituals, maintenance, and field discipline
- bench replay as a serious debugging method

This repo is meant to sit *next to* project repos like **drone-chorus**:
- **drone-chorus** = the living field manual + art system
- **fpv-primer** = the shared foundation that keeps the ocean learnable

## Who this is for

- Makers who can solder and code but feel new to FPV
- Educators who need a reliable “props-off first” sequence
- Artists who want telemetry as material (without treating safety as optional)
- Advanced students who need a disciplined bridge from bench-safe understanding to repeatable field work

## Default teaching rig

Unless noted otherwise, this primer now assumes a baseline teaching rig similar to a **BETAFPV Air65 with ELRS**:

- 65 mm brushless whoop geometry
- 1S battery system
- integrated or semi-integrated AIO / 5-in-1 style board
- **ELRS 2.4 GHz** control link
- analog FPV video path

That gives the repo a concrete reference stack while keeping the concepts transferable to larger FPV builds.

## Core doctrine

1. **Props-off until the system proves itself.** Bench replay is not a shortcut—it’s the ground truth.
2. **Treat telemetry as a contract.** Define semantics, ranges, and failure behavior before you map anything.
3. **Mappings are compositions.** Don’t just route values—shape them (curves, deadbands, smoothing, limits).
4. **Safety nets are features.** “Undo,” “safe mode,” and “known-good reset” are part of the instrument.
5. **Ship artifacts.** Every session ends with something reproducible: a mapping sheet, a log, a preset, a clip.

## What this repo is trying to solve

A lot of FPV teaching fails in one of two ways:

- it stays at hype level: brands, speed, vibes, but not enough system reasoning
- it goes full tuning rabbit-hole before students can safely prove the stack works

This repo aims for the middle:

- serious enough for post-secondary work
- still compact enough to use in a lab sequence
- explicit about what counts as proof
- explicit about what should *not* be trusted yet

## Expected outputs

By the end of a short primer sequence, students should be able to produce:

- a saved Betaflight config or diff
- a bench-proof checklist with signoff
- one short telemetry capture
- one replayable parsing or mapping test
- one flight or bench log with actual observations
- one troubleshooting narrative that starts from symptoms instead of panic

## Quickstart paths

### Path A: Bench-only (recommended first)
1. Read: `docs/01-safety-and-props-off.md`
2. Read: `docs/02-parts-map.md`
3. Read: `docs/04-betaflight-minimum-viable-setup.md`
4. Read: `docs/06-telemetry-semantics.md`
5. Run: `labs/lab00-bench-sim.md`
6. Run: `labs/lab01-telemetry-to-midi.md`

### Path B: Post-secondary studio / seminar sequence (4-6 sessions)
1. Systems overview + parts map + safety doctrine
2. Betaflight minimum viable setup + failsafe proof
3. Telemetry capture + bench replay
4. Mapping as composition
5. Troubleshooting clinic
6. Capture / presentation / critique

### Path C: Field sequence (after bench competence)
1. Build checklist -> arming discipline -> short flights
2. Post-flight review -> capture -> replay
3. Mapping iteration from the same dataset
4. Controlled comparison of tune or mapping changes

### Path D: Drone Chorus bridge
1. Bench-only ritual
2. Telemetry semantics table
3. One stable telemetry -> MIDI route
4. Three different “feels” from one source signal

### Path E: Regulatory / operations briefing
1. Read: `docs/13-us-operations-and-radio-compliance.md`
2. Read: `docs/14-maintenance-and-post-crash-triage.md`
3. Confirm whether your program is bench-only, indoor-only, or field-capable

## What you’ll find here

- **docs/**: primers, checklists, semantics, and capture workflows
- **labs/**: repeatable exercises (bench-first)
- **templates/**: mapping sheets and log templates you can copy per project
- **course_sequence.md**: a 5-session post-secondary teaching arc
- **instructor_guide.md**: pacing, setup, and proof standards
- **assessment_rubric.md**: artifact-based evaluation criteria

## Teaching package

If you are using this repo as a short course instead of a self-study reference, start here:

1. `course_sequence.md`
2. `instructor_guide.md`
3. `templates/air65-bench-proof-checklist.md`
4. `templates/post-crash-triage-sheet.md`

The intended baseline is still a whoop-class rig similar to a BETAFPV Air65 with ELRS, but the evaluation logic is transferable to other small FPV platforms.

## Safety + responsibility (read this)
This repo is **not** a substitute for manufacturer manuals, local laws, common sense, or supervised instruction. FPV equipment can cause injury, fire, and property damage. Start with small batteries, remove props for bench work, and treat every power-up as live. When in doubt: stop, ask, and re-check.

This repo also assumes:

- you can distinguish control link, video link, and telemetry path
- you are willing to prove failsafe before flight
- you will log what changed instead of relying on memory
- you treat post-crash inspection as part of piloting, not an afterthought

## How this connects to Drone Chorus
Drone Chorus needs FPV fluency, but it shouldn’t *teach FPV from scratch* in its own README. This repo holds the shared foundation, then Drone Chorus can stay focused on:
- telemetry → smoothing → MIDI CC
- mapping-as-composition
- patch design + performance practice
- robust capture + repeatable demos

## Current emphasis

This version now prioritizes:

- systems literacy over brand preference
- bench replay over guess-and-check tuning
- stable semantics over high channel count
- reproducible artifacts over “it felt better, I think”

## Suggested teaching move

If students are new, make them say the stack out loud:

1. power
2. control link
3. flight controller
4. motor output
5. video path
6. telemetry path

If they cannot narrate the chain, they do not understand the failure yet.

---

## Suggested video companion (optional)
If you’re filming: treat each lab as a short episode.
**Goal → Steps → Observe → Why → Artifact**

Artifacts can be: mapping YAML, log CSV, short A/B clip, or a screenshot of Betaflight settings.

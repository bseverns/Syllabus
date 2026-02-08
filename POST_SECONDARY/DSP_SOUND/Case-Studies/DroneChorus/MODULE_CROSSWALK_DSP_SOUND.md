# Module Crosswalk — Drone Chorus ↔ DSP_SOUND

This is optional scaffolding: if you want Drone Chorus to act as a portal into
the larger DSP curriculum stack, these pointers tell you where each concept
already lives in `DSP_SOUND/`.

> Paths below are relative to the DSP_SOUND repo root.

## Exercise 1 — Pipeline Proof (Log → MIDI → Patch)
- `Interfaces-Mapping-and-Protocols/resources/PROTOCOLS.md`  
  Why: Serial/MIDI contracts, “what a protocol guarantees.”
- `Embedded-Systems-and-RealTime/resources/DESIGN_PATTERNS.md`  
  Why: cadence + separation of concerns (bridge vs patch vs broadcast).

## Exercise 2 — Mapping YAML Is the Score
- `Interfaces-Mapping-and-Protocols/resources/MAPPING_PATTERNS.md`  
  Why: curves, scaling, and mapping patterns that behave like composition.
- `Applied-DSP-Optional-Lanes/resources/PARAMETER_FEEL.md`  
  Why: tapers, smoothing, stepping—how parameters become playable.

## Exercise 3 — Smoothing as Musical Trust
- `Applied-DSP-Optional-Lanes/resources/PARAMETER_FEEL.md`  
  Why: slew/smoothing framing; turning jitter into gesture.
- `Foundations-Signals-and-Systems/sessions/week01.md`  
  Why: amplitude/frequency/phase as the “axes” you can map into musical changes.

## Exercise 4 — Attenuverters as Safety Rails
- `Applied-DSP-Optional-Lanes/resources/SAFETY_RAILS.md`  
  Why: guardrails, bounds, and “don’t surprise the listener.”
- `Digital-Tools-and-Platforms/resources/SAFETY.md`  
  Why: practical safety checklists and teaching-room norms.

## Exercise 5 — CC Map Legend (Audience Comprehension)
- `Interfaces-Mapping-and-Protocols/resources/PROTOCOLS.md`  
  Why: why consistent numbering + semantic naming matters.
- `Ethics-Accessibility-LongTerm-Thinking/admin/RISK_SAFETY.md`  
  Why: communication, risk planning, and audience considerations.

## Exercise 6 — Multi‑Drone Channels (Scale)
- `Interfaces-Mapping-and-Protocols/resources/PROTOCOLS.md`  
  Why: channels vs ports as a scaling strategy.
- `Embedded-Systems-and-RealTime/resources/DESIGN_PATTERNS.md`  
  Why: define loss policies + keep failure legible as complexity increases.

## Exercise 7 — Logging + Replay
- `Embedded-Systems-and-RealTime/bench/TEST_PROCEDURES.md`  
  Why: repeatability and measurement habits.
- `Embedded-Systems-and-RealTime/resources/DONT_BRICK.md`  
  Why: safe recovery patterns; treat “reset” as a feature.

## Exercise 8 — Failure Drill
- `Embedded-Systems-and-RealTime/resources/DONT_BRICK.md`  
  Why: fail predictably, recover reliably.
- `Applied-DSP-Optional-Lanes/resources/SAFETY_RAILS.md`  
  Why: audible failure modes (mute/hold/decay) that protect ears + trust.

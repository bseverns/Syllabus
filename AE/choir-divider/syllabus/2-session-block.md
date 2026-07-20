# Choir Divider — Two-Session Lab Block

**Format:** 2 sessions × 90–120 minutes  
**Platform:** Tangible Waves AE Modular BRAEDBOARD (0–5V logic)  
**Core circuit:** 555 clock → (optional 40106) → 4017 decade counter → selected outputs as rhythmic divisions

## Course description
In this lab, students build a compact rhythm engine: a circuit that takes one pulse and produces a family of related pulses. A counter becomes a composer—turning repetition into structure, and structure into groove. Students leave with a patchable AE breadboard module that can act as a clock source, divider, and step-based rhythm generator.

## Learning outcomes
Students will be able to:
1. Build and tune an NE555 astable clock and relate RC values to rate.
2. Explain how a counter advances through states and how those states can be used musically.
3. Derive rhythmic divisions by selecting counter outputs, combining outputs (diode OR), and resetting at chosen steps.
4. Condition/clean a clock using a Schmitt trigger and understand why it matters.
5. Patch divided gates into AE modules to create polyrhythm and rhythmic “masking.”
6. Debug clock/counting circuits using a small set of measurements.

## Materials (per pair)
- ICs: NE555, CD4017, (optional) CD40106
- Resistors: 1k, 47k, 100k
- Capacitors: 10nF, 100nF; electrolytic 10uF
- LEDs + 1k resistors (2 LEDs recommended)
- 50k pot for clock rate (if using internal clock)
- Patch cables; multimeter recommended

---

## Session 1 — “Make time visible”
### Build focus
- Power rails + decoupling habits
- NE555 clock (or external AE clock input)
- 4017 counting with visible step LEDs

### Checkpoints
- Clock LED blinks and sweeps with rate knob (if internal)
- 4017 advances one step per pulse (observe with LED on one output)
- Reset returns counter to Q0 reliably

---

## Session 2 — “Turn steps into groove”
### Build focus
- Divisions: select Q outputs as rhythmic outs
- Reset-early: define loop length (3/4/5-step cycles)
- Optional: diode OR to create patterns
- Optional: 40106 cleanup for crisp pulses

### Checkpoints
- At least 3 distinct rhythmic outputs available
- One output is a stable “downbeat”
- Optional: conditioned clock reduces double-trigger behavior

### Studio assessment
- 30–60s patch demo + patch diagram + short reflection

## ClassHub Delivery Map

Use ClassHub as a private evidence surface. It does not authorize powering, patching, or continued use of a circuit; facilitator inspection and the local bench procedure remain controlling.

| Phase | Required private evidence | ClassHub materials |
| --- | --- | --- |
| Session 1 — clock/count | Power/rail inspection, measured voltage, visible counter sequence, and worksheet notes | Private photo/document upload; bench checklist; short reflection |
| Session 2 — divide/patch | Three outputs, one verified reset length, patch diagram, and recording or observed demonstration | Private artifact upload; completion checklist; optional consent-cleared audio clip |

Keep bench photos private when they expose room, participant, or equipment identifiers. A de-energized diagram/observation route can satisfy the conceptual evidence.

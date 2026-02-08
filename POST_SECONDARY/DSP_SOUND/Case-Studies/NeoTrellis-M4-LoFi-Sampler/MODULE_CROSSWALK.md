# Module crosswalk — demo exercises → DSP_SOUND references

Use this file to connect a Lo‑Fi Sampler walkthrough to the broader DSP_SOUND curriculum.

Structure:
- Each exercise is **one teachable unit**.
- For the video, show: **Goal → Observe → Why** (steps can be minimal on camera).
- In the description / pinned comment, link the DSP_SOUND references.

---

## Exercise 1 — Clocked Grid (Quantization)
**Principle:** cadence + deterministic timebase  
**DSP_SOUND pointers**
- `../../Embedded-Systems-and-RealTime/resources/DESIGN_PATTERNS.md` (cadence, separation of concerns, loss policies)
- `../../Embedded-Systems-and-RealTime/sessions/week01.md` (latency vs jitter; measuring your loop)

**Suggested on‑screen title:** “Clocked Grid (quantized stepping)”

---

## Exercise 2 — “Silence → Phase → Chaos”
**Principle:** phase as a parameter; complexity from constraints  
**DSP_SOUND pointers**
- `../../Foundations-Signals-and-Systems/sessions/week01.md` (amplitude/frequency/phase as touchable parameters)
- `../../Foundations-Signals-and-Systems/sessions/week07.md` (sampling + quantization; aliasing as constraint)

**Suggested on‑screen title:** “Phase drift from unequal source lengths”

---

## Exercise 3 — Modifier Offset Latch
**Principle:** interface design that preserves the music surface  
**DSP_SOUND pointers**
- `../../Interfaces-Mapping-and-Protocols/README.md` (control becomes instrument)
- `../../Interfaces-Mapping-and-Protocols/labs/week07_feedback_design.ipynb` (feedback design patterns)

**Suggested on‑screen title:** “Offset latches (full 8‑step lane stays intact)”

---

## Exercise 4 — Velocity Lanes
**Principle:** discrete expression lanes; parameter feel  
**DSP_SOUND pointers**
- `../../Applied-DSP-Optional-Lanes/resources/PARAMETER_FEEL.md` (tapers, smoothing, stepping, guardrails)
- `../../Interfaces-Mapping-and-Protocols/resources/MAPPING_PATTERNS.md` (shaping + stabilization tools)

**Suggested on‑screen title:** “Velocity lanes (three discrete levels)”

---

## Exercise 5 — Probability Lanes
**Principle:** variation without UI explosion; controlled randomness  
**DSP_SOUND pointers**
- `../../Interfaces-Mapping-and-Protocols/resources/MAPPING_PATTERNS.md` (protect downstream; rate‑limit; meaningful change)
- `../../Interfaces-Mapping-and-Protocols/sessions/week07.md` (build → measure → document loop)

**Suggested on‑screen title:** “Probability lanes (35→60→85→100%)”

---

## Exercise 6 — Stutter Without Reprogramming
**Principle:** performance gestures that do not mutate state  
**DSP_SOUND pointers**
- `../../Interfaces-Mapping-and-Protocols/resources/MAPPING_PATTERNS.md` (events vs continuous streams; protect edges)
- `../../Embedded-Systems-and-RealTime/resources/DESIGN_PATTERNS.md` (separate concerns; define loss policies)

**Suggested on‑screen title:** “Stutter gesture (expression without side effects)”

---

## Exercise 7 — Live Record + Auto‑Slice
**Principle:** sampling as a workflow; predictable surfaces  
**DSP_SOUND pointers**
- `../../Foundations-Signals-and-Systems/sessions/week07.md` + `../../Foundations-Signals-and-Systems/labs/week07_sampling_aliasing.ipynb`
- `../../Foundations-Signals-and-Systems/assignments/hw07_sampling.md` (“why it works” + “local hack”)

**Suggested on‑screen title:** “Record + auto‑slice (stable 8‑step layout)”

---

## Exercise 8 — Undo/Restore + Reslice
**Principle:** recovery as part of the instrument  
**DSP_SOUND pointers**
- `../../Embedded-Systems-and-RealTime/resources/DONT_BRICK.md` (safe mode; factory reset; atomic saves)
- `../../Interfaces-Mapping-and-Protocols/resources/CONFIG_GUIDELINES.md` (safe defaults; validation; export/import)

**Suggested on‑screen title:** “Undo + reslice (keep the pattern)”

---

## Exercise 9 — Performance FX and ISR Discipline
**Principle:** real‑time audio discipline (“boring ISR”)  
**DSP_SOUND pointers**
- `../../Embedded-Systems-and-RealTime/resources/DESIGN_PATTERNS.md` (cadence; separate concerns; loss policies)
- `../../Embedded-Systems-and-RealTime/README.md` (real‑time mindset; bench procedures)

**Suggested on‑screen title:** “FX triggers + boring ISR rule”

---

## Exercise 10 — Factory Demo Restore + Manifest
**Principle:** teaching rigs; integrity; repeatability  
**DSP_SOUND pointers**
- `../../Embedded-Systems-and-RealTime/resources/DONT_BRICK.md` (recovery paths)
- `../../Interfaces-Mapping-and-Protocols/resources/CONFIG_GUIDELINES.md` (factory reset; safe defaults)

**Suggested on‑screen title:** “Factory restore (workshop repeatability)”

---

## Optional: turn the walkthrough into an assignment
Use the HW07 reflection pattern:
- `../../Foundations-Signals-and-Systems/assignments/hw07_sampling.md`

Prompt:
1) Document one demo behavior (include a short audio render).
2) Write 5–10 sentences explaining **why it works** (tie to one pointer above).
3) Propose one “local hack” extension (e.g., new lane values, new FX table, alternate slice rule).

_Last updated: 2026-02-08_

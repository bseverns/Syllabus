# Demo Exercises — Teaching the NeoTrellis M4 Lo‑Fi Sampler

These exercises are short, repeatable demos that explain not just *what* the
sampler does, but *why* the system is designed this way. Each exercise is
stand‑alone; you can run them in order or cherry‑pick for a workshop.

> This file is intended to mirror the sampler project’s own demo exercises.
> If you maintain a canonical copy in the sampler repo (recommended), keep
> this version in sync.

**Preflight**
Make sure the board is loaded with slices in `/A`, `/B`, `/C`, `/D`, and that a
MIDI clock is running.

Use these helpers if needed (from the sampler repo tooling):
- `python examples/gen_demo_row_A.py` to generate demo raws.
- `python examples/midi_clock_sender.py --out "NTM4 Sampler" --bpm 90` for clock.

---

**Exercise 1 — Clocked Grid (Quantization)**
Goal: Show that everything locks to a global USB MIDI clock.

Steps:
1. Start the MIDI clock at 90 BPM.
2. Toggle a few gates on row A (columns 1–6).
3. Stop the clock, wait, then send Continue.

Observe: Steps only advance on the clock, and Continue resumes on the current step.

Why it’s designed this way: The global clock is the backbone that keeps UI,
file I/O, and the DAC ISR synchronized without drift.

---

**Exercise 2 — “Silence → Phase → Chaos”**
Goal: Demonstrate the drift effect when sample lengths differ.

Setup: Ensure rows A and B have different source lengths.

Steps:
1. Turn on the same gates for rows A and B.
2. Let it run for 4–8 bars.

Observe: The two rows gradually drift in and out of phase, creating evolving
rhythms without changing the grid.

Why it’s designed this way: Equal‑slice quantization plus differing source
lengths gives complexity from simple inputs.

---

**Exercise 3 — Modifier Offset Latch**
Goal: Show why Alt/Shift live “one row down.”

Steps:
1. Hold Alt on the row below row A (column 7).
2. While holding, tap gates on row A.
3. Release Alt and tap gates again.

Observe: Modifier latch stays tied to a row while preserving all 8 step pads.

Why it’s designed this way: You keep full 8‑step lanes per row without giving
up modifier access.

---

**Exercise 4 — Velocity Lanes**
Goal: Show per‑step dynamics without a full menu system.

Steps:
1. Enable a few gates on row A.
2. Hold Shift and tap a lit step repeatedly.

Observe: The step’s brightness changes as velocity cycles (80 → 108 → 127).

Why it’s designed this way: Three discrete lanes give musical expression while
keeping UI interactions simple and fast.

---

**Exercise 5 — Probability Lanes**
Goal: Show controlled randomness per step.

Steps:
1. Enable a few gates on row A.
2. Hold Alt and tap a lit step repeatedly.

Observe: The step’s probability cycles (35% → 60% → 85% → 100%).

Why it’s designed this way: Discrete probability lanes add variation without
adding UI complexity or CPU cost.

---

**Exercise 6 — Stutter Without Reprogramming**
Goal: Show “momentary FX” that do not change the gate pattern.

Steps:
1. Enable a gate on row A, step 3.
2. While it plays, hold Shift and tap the lit step.

Observe: A brief stutter blast fires, but the gate pattern stays unchanged.

Why it’s designed this way: Performance gestures are possible without losing
the underlying pattern.

---

**Exercise 7 — Live Record + Auto‑Slice**
Goal: Show the record path and the reason for 8‑slice auto‑cutting.

Steps:
1. Patch a line‑level source into the analog input.
2. Hold Shift and tap a row pad to start recording.
3. Tap the same row pad again to stop and auto‑slice.

Observe: The row mutes during record, then immediately plays 8 new slices.

Why it’s designed this way: Recording creates a `source.raw` plus 8 equal
slices so the playback grid remains stable.

---

**Exercise 8 — Undo/Restore + Reslice**
Goal: Show the safety net and the “try again” workflow.

Steps:
1. Record a new take on row A.
2. Hold Alt and tap row A once.
3. Hold Shift+Alt and tap step 6 on row A.

Observe: Alt swaps in `source_prev.raw` if it exists. Shift+Alt+step 6 reslices
the current `source.raw` without touching gates.

Why it’s designed this way: You can recover the previous take or reslice the
current one without reprogramming the pattern.

---

**Exercise 9 — Performance FX and ISR Discipline**
Goal: Show FX triggers and explain the “boring ISR” rule.

Steps:
1. Hold Shift+Alt and tap step 1 to trigger filter sweep.
2. Hold Shift+Alt and tap step 2 to trigger bitcrush.
3. Hold Shift+Alt and tap step 3 to trigger drive.
4. Hold Shift+Alt and tap step 4 to clear FX.

Observe: The FX feel immediate but playback stays stable.

Why it’s designed this way: The ISR only mixes precomputed tables; slow work
lives in the foreground job queue to avoid audio glitches.

---

**Exercise 10 — Factory Demo Restore + Manifest**
Goal: Show how demo integrity is maintained for teaching rigs.

Steps:
1. Connect Serial Monitor at 115200 baud.
2. Press `f` to trigger factory demo restore.
3. Reboot and watch the `[manifest]` log line.

Observe: The board restores `/factory` files into the live root and reports
manifest status.

Why it’s designed this way: A one‑key reset keeps demo boards consistent
without reflashing firmware.

---

**Trainer Notes**

**Structure**
Use a consistent rhythm so viewers can follow: **Goal → Steps → Observe → Why**.
Keep each exercise to ~45–90 seconds and remind viewers that they can pause and
copy the steps.

**Capture Tips**
- **Audio**: record the board output direct if possible; if filming the speaker,
  keep the music 6–10 dB under your voice.
- **Camera**: one wide shot of the grid, one close‑up on the row you’re using.
- **Overlays**: put the pad combo text on screen (e.g., “Shift + Step 3”).
- **Clock**: always show BPM on screen when changing tempo.

**Narration Cues**
- Say the *reason* in plain language: “We keep the ISR boring so audio doesn’t
  glitch when storage is busy.”
- When showing drift, call out bar numbers: “By bar 4 you’ll hear the phase
  shift.”

**Safety Nets**
- If a take goes wrong, mention the undo: “Alt + Row swaps in the previous take.”
- After any destructive action (erase/reslice), immediately demonstrate the
  restore or factory reset so viewers trust the workflow.

**Pacing**
- Group Exercises 1–3 as a 3‑minute “core system overview.”
- Exercises 4–6 as a 2‑minute “performance controls.”
- Exercises 7–10 as a 3‑minute “recording + recovery + integrity.”

**Suggested On‑Screen Titles**
- “Clocked Grid”
- “Phase Drift”
- “Offset Latches”
- “Velocity Lanes”
- “Probability Lanes”
- “Stutter Gesture”
- “Record + Auto‑Slice”
- “Undo + Reslice”
- “Performance FX”
- “Factory Restore”

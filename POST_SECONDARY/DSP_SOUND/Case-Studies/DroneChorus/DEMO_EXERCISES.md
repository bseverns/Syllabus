# Demo Exercises — Teaching Drone Chorus (Telemetry‑Driven Synth)

These exercises explain not just *what* Drone Chorus does, but *why* the system is
built this way. Each exercise is stand‑alone; run them in order for a complete
walkthrough.

## Preflight (do this every time)
- **Safety first**: read `docs/checklists/SAFETY.md` and treat it as non‑negotiable.
- Confirm you can open the VCV patch: `vcv/DroneChorus_Patch.vcv` (or `DroneChorus_2Drones.vcv`).
- If you’re not using a real drone today, rebuild sample logs:
  - `python scripts/generate_sample_logs.py`
  - pick one file from `data/` (see `data/README.md`)

---

## Exercise 1 — Pipeline Proof (Log → MIDI → Patch)
**Goal:** Prove the end‑to‑end chain without flight.

**Steps**
1. Use the repo’s “bench replay” method to feed MSP bytes from a capture into a virtual serial port. The exact commands vary by OS; see `software/midi-bridge/README.md`.
   - Typical flow: `socat` creates a PTY pair → `miniterm` replays `obs/telemetry/bench_hover.mspbin` into `_in` → the bridge reads from `_out`.
   - Example (one possible Linux/macOS approach):
     ```bash
     # terminal 1: create PTYs
     socat -d -d PTY,raw,echo=0,link=$HOME/.tmp_msp_in PTY,raw,echo=0,link=$HOME/.tmp_msp_out
     
     # terminal 2: replay bytes into _in
     python -m serial.tools.miniterm --raw --exit-char=3 $HOME/.tmp_msp_in 115200 < obs/telemetry/bench_hover.mspbin
     
     # terminal 3: run the bridge against _out
     python software/midi-bridge/msp_to_midi.py --serial $HOME/.tmp_msp_out
     ```
2. Run the bridge against the replay port, then open the VCV patch and ensure a **MIDI‑CC** module is listening to the `DroneChorus` port.
3. Watch CC values move (or add a MIDI monitor window).

**Observe:** The patch reacts even though no aircraft is powered.

**Why it’s designed this way:** Workshops and rehearsals need a “props‑off” mode
that still demonstrates the system.

---

## Exercise 2 — The Mapping YAML Is the Score
**Goal:** Show that `config/mapping.yaml` is the musical contract.

**Steps**
1. Open `config/mapping.yaml` on screen.
2. Call out one mapping line (e.g., roll/pitch) with **min/max, curve, slew**.
3. Make a small change (e.g., increase slew slightly) and reload the bridge.

**Observe:** The same telemetry now *feels* different in the patch.

**Why it’s designed this way:** The config is the teaching surface: it’s easier to
edit a score than to rewire a performance.

---

## Exercise 3 — Smoothing as “Musical Trust”
**Goal:** Demonstrate why raw telemetry is rarely playable.

**Steps**
1. Temporarily set a slew value near zero for one channel (raw-ish).
2. Compare to the default slew (restored).

**Observe:** Raw telemetry jitters; slewed telemetry becomes a gesture.

**Why it’s designed this way:** Smoothing turns sensor noise into phrasing.

---

## Exercise 4 — Attenuverters = Safety Rails (Ears + Mix)
**Goal:** Show how to keep ranges tasteful and hearing-safe.

**Steps**
1. In Rack, set attenuverters so full stick travel ≈ a musical sweep.
2. Engage/verify an OBS limiter if you’re routing audio through OBS (see `obs/README.md`).

**Observe:** Big drone motion doesn’t equal painful audio.

**Why it’s designed this way:** Performance systems must be safe by default, not
safe only when you remember.

---

## Exercise 5 — CC Map Legend (Audience Comprehension)
**Goal:** Make the mapping legible to non‑coders watching.

**Steps**
1. Show the CC plan (CC14–20 + CC64) from `docs/CONTROL_STACK_PLAYBOOK.md`.
2. Flash the audience legend from `docs/UX_MAP.md`.

**Observe:** Viewers can say what they’re hearing: “roll→cutoff,” “yaw→delay,” etc.

**Why it’s designed this way:** If the audience can’t read the mapping, the piece
becomes opaque instead of shareable.

---

## Exercise 6 — Multi‑Drone Channels (Scale Without Chaos)
**Goal:** Add a second drone/stream without changing the CC numbers.

**Steps**
1. Open `config/multi.yaml` and point to channels 1..N on the same port.
2. Load `vcv/DroneChorus_2Drones.vcv` (or duplicate the single voice).
3. Verify channel separation in Rack.

**Observe:** Same CC numbers, different channels, clean separation.

**Why it’s designed this way:** Consistent CC numbers keep the patch teachable;
channels provide scale.

---

## Exercise 7 — Logging + Replay (Debugging as Art)
**Goal:** Show that a performance can be replayed and studied.

**Steps**
1. Record a short run (flight or replay) and save the log.
2. Replay it and compare the sonic result.

**Observe:** The system can reproduce behavior well enough to learn from it.

**Why it’s designed this way:** Repeatability turns “cool moment” into curriculum.

---

## Exercise 8 — Failure Drill (Make Errors Legible)
**Goal:** Demonstrate what happens when a link drops.

**Steps**
1. Disconnect/reconnect the telemetry source (or stop a replay).
2. Show how the bridge and patch behave (hold, decay, mute, etc.).
3. Point to the recovery path in your playbooks.

**Observe:** Failure is visible and survivable.

**Why it’s designed this way:** In performance, failure will happen. Design so it
fails *predictably*.

---

## Trainer Notes
Use a consistent rhythm: **Goal → Steps → Observe → Why**. Keep each exercise to
~60–120 seconds, and remind viewers they can pause and copy steps.

**Suggested on‑screen titles**
- “Pipeline Proof”
- “Mapping YAML”
- “Smoothing”
- “Safety Rails”
- “Audience Legend”
- “Multi‑Drone Channels”
- “Log + Replay”
- “Failure Drill”

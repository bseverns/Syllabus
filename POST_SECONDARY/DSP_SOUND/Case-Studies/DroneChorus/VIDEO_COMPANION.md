# Video Companion — Drone Chorus Walkthrough (10–12 minutes)

This aligns to `DEMO_EXERCISES.md`, but is written for filming: clear chapters,
minimal context switching, maximum legibility.

## Suggested cold open (0:00–0:15)
- Show the VCV patch responding to telemetry (replay log is fine).
- On screen: “Telemetry → MIDI → Synth”.

## Chapter plan
1. What Drone Chorus is (thesis + the diagram in `docs/architecture.svg`)
2. Pipeline proof (Exercise 1) — bench replay is totally valid on camera
3. Mapping YAML (Exercise 2)
4. Smoothing (Exercise 3)
5. Safety rails (Exercise 4)
6. Audience legend (Exercise 5)
7. Multi‑drone scale (Exercise 6)
8. Log + replay (Exercise 7)
9. Failure drill (Exercise 8)
10. Outro: “what to build next”

## Overlays that make this watchable
- A persistent mini-legend: “roll→cutoff • pitch→FM • yaw→delay • rssi→reverb • vbat→tone • throttle→amp • arm→hold”
- A config callout when you show YAML: highlight **min/max, curve, slew**.
- A safety callout: “attenuverters < 50% until tuned • limiter on program audio”.

## Shot recipe (simple)
- Screen capture: terminal + Rack patch + YAML files
- Optional: a small camera shot of the drone **with props removed** during bench mode
- Optional: OBS preview if you want to demonstrate the audience view

## Outro script seed
“Drone Chorus is a mapping instrument: flight dynamics become modulation you can hear.
If you want the deep wiring, start with `docs/CONTROL_STACK_PLAYBOOK.md`. If you want
the teachable demo, use this case study. And if you want the bigger ideas—mapping,
protocols, safety rails—follow the DSP_SOUND crosswalk.”

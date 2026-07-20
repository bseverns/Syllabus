# Step 05 — Divisions + patterns

## Pick steps
Wire Q outputs to jacks as rhythmic outs:
- Q0 (downbeat)
- Q5 (half)
- Q2/Q3 (late accents)
- Q7 (syncopation)

## Reset early (short loops)
To loop 0–3, reset at Q4:
- Q4 → diode → RESET (pin 15)
  (diode anode at Q4, cathode at RESET)
- 100k: RESET → GND (pull-down)

The reset output is not heard as a held step: Q2 produces a 2-step `Q0–Q1` cycle, Q3 produces 3 steps, Q4 produces 4 steps, and Q5 produces 5 steps.

## OR patterns
- Selected Q outputs → diodes → PATTERN node
  (diode anode at Q, cathode at PATTERN)
- 100k: PATTERN → GND

PATTERN goes high on any chosen step.

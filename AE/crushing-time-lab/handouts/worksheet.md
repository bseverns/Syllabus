# Worksheet: Crushing Time Lab (Build + Reflection)

Name(s): ____________________________   Date: ________________   Pair/Group: _______

## Part A — Build checkpoints (measure + verify)

### A1) Rails
- +5V at IC power pins (spot-check at least two ICs):  ______________ V
- GND continuity (GND rail to IC GND pins):  ☐ Yes  ☐ No

### A2) Vref (virtual ground)
- Vref measurement: ______________ V
- Vref is stable (does not drift wildly while you touch the board):  ☐ Yes  ☐ No

Explain in one sentence why we need Vref in a 0-5V audio system:

______________________________________________________________________________

### A3) Clock (NE555)
- Clock present at 555 pin 3 (CLK_RAW):  ☐ Yes  ☐ No
- Clock range feels:  ☐ very slow  ☐ medium  ☐ very fast
- LED indicator (if used):  ☐ blinks  ☐ stays on  ☐ stays off

Describe what happens to the sound when the clock gets slower:

______________________________________________________________________________

### A4) Clock cleanup (CD40106)
- Clean clock present at 40106 output (CLK):  ☐ Yes  ☐ No
- Difference you notice vs CLK_RAW (sound or stability):

______________________________________________________________________________

### A5) Sample/Hold (CD4051)
Hold capacitor used (circle):  10nF   100nF   10uF

- OUT2 (dry) works:  ☐ Yes  ☐ No
- OUT1 (crushed) works:  ☐ Yes  ☐ No

Describe the crushed texture in two adjectives:

_________________________   _________________________

---

## Part B — Patch diagram (draw your patch)

Source module: ____________________   Modulator: ____________________
OUT1 destination: _________________   OUT2 destination: _________________

Patch sketch:

______________________________________________________________________________
______________________________________________________________________________
______________________________________________________________________________

---

## Part C — Controlled experiments (listen, then write)

### C1) Hold capacitor comparison

| Hold cap | What changed in the sound? | Best use (audio or CV)? |
|---------:|-----------------------------|--------------------------|
| 10nF     |                             |                          |
| 100nF    |                             |                          |
| 10uF     |                             |                          |

### C2) CV-controlled crush
CV source patched into CV socket (circle):  LFO   ENV   AUDIO   CLOCK   OTHER: _______

- CV Amount knob position (approx):  ☐ low  ☐ mid  ☐ high
- What did CV change most?

______________________________________________________________________________

---

## Part D — Debug log (the honest part)

1) Symptom: _________________________________________________________________
2) One measurement you took: ________________________________________________
3) Fix you tried: ____________________________________________________________
4) Result:  ☐ fixed  ☐ improved  ☐ no change

---

## Part E — Reflection (short)

In 3-5 sentences: What did this circuit teach you about time, control voltage, and "lo-fi"?

______________________________________________________________________________
______________________________________________________________________________
______________________________________________________________________________

# Build Step 07 — CV-controlled crush (NE555 pin 5)

## Goal
Modulate crush rate with CV like a real module.

## Wire
- CV socket → 47k → CV_IN
- 100nF: CV_IN → GND
- CV amount pot (50k):
  - lug1 → CV_IN
  - lug3 → GND
  - wiper → CV_ATTEN
- 100k: CV_ATTEN → 555 pin 5 (CTRL)
- 10nF: 555 pin 5 → GND
- Clamp diodes at pin 5:
  - 1N4148 anode pin5, cathode +5V
  - 1N4148 anode GND, cathode pin5

## Check
Patch an LFO to CV: the crush rate should sweep.

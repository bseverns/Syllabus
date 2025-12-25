# Pin-accurate netlist (core + CV-controlled crush)

## Node names
+5V, GND, Vref, AUDIO_IN, IN_AC, AUDIO_BIASED, CLK_RAW, CLK, SAMP_NODE, SAMP_SHAPED, OUT_CRUSH, OUT_DRY, AE_OUT

---

## 0) Power and decoupling
### MCP602 (U4) DIP-8
- U4-8 → +5V
- U4-4 → GND
- 100nF: +5V ↔ GND close to U4

### NE555 (U1) DIP-8
- U1-8 → +5V
- U1-1 → GND
- U1-4 → +5V
- 100nF: U1-8 ↔ GND close to U1
- 10nF: U1-5 → GND (CTRL decouple)

### CD40106 (U2) DIP-14
- U2-14 → +5V
- U2-7  → GND
- 100nF: U2-14 ↔ U2-7 close to U2

### CD4051 (U3) DIP-16
- U3-16 → +5V
- U3-8  → GND
- 100nF: U3-16 ↔ U3-8 close to U3

---

## 1) Vref (2.5V)
- 100k: +5V → Vref
- 100k: Vref → GND
- 100nF: Vref → GND

---

## 2) Input bias + buffer (U4A)
- 100nF: AUDIO_IN → IN_AC
- 100k: IN_AC → Vref
- U4-3 (+IN A) → IN_AC
- U4-1 (OUT A) → AUDIO_BIASED
- U4-2 (−IN A) → AUDIO_BIASED  (follower)
- OUT_DRY = AUDIO_BIASED

---

## 3) NE555 clock (U1 astable)
- tie U1-2 to U1-6  (THR_TRIG)
- 47k: +5V → U1-7 (DISCH)
- 50k pot as variable resistor: U1-7 ↔ THR_TRIG
- 10uF: THR_TRIG → GND (electrolytic + to THR_TRIG)
- U1-3 (OUT) → CLK_RAW

---

## 4) Clock cleanup (U2 CD40106)
Use inverter gate 1:
- U2-1 (IN1)  → CLK_RAW
- U2-2 (OUT1) → CLK
(Optional invert using gate 2)
- U2-3 (IN2)  → CLK
- U2-4 (OUT2) → CLK_INV

---

## 5) Sample/Hold (U3 CD4051)
- U3-15 (A) → GND
- U3-14 (B) → GND
- U3-13 (C) → GND
- U3-1 (X0) → AUDIO_BIASED
- U3-3 (Z)  → SAMP_NODE
- 100nF: SAMP_NODE → Vref  (hold cap, placed close to U3)
- U3-12 (INH) → CLK  (or CLK_INV if preferred)

---

## 6) Optional shaping (“bit-feel”)
- 10k: SAMP_NODE → SAMP_SHAPED
- 47k: SAMP_SHAPED → Vref
- 1N4148 clamp pair:
  - Dhi: anode SAMP_SHAPED, cathode +5V
  - Dlo: anode GND, cathode SAMP_SHAPED

(If skipping shaping, tie SAMP_SHAPED = SAMP_NODE.)

---

## 7) Output buffer (U4B)
- U4-5 (+IN B) → SAMP_SHAPED
- U4-7 (OUT B) → OUT_CRUSH
- U4-6 (−IN B) → OUT_CRUSH  (follower)

Route OUT_CRUSH to AE OUT jack (BRAEDBOARD OUT1).
Route OUT_DRY to AE OUT jack (BRAEDBOARD OUT2).

---

## 8) CV-controlled crush (robust)
Goal: modulate NE555 pin 5 (CTRL) safely.

### CV input conditioning
- 47k: CV_SOCKET → CV_IN
- 100nF: CV_IN → GND

### CV amount pot (50k)
- pot lug1 → CV_IN
- pot lug3 → GND
- pot wiper → CV_ATTEN

### Injection into pin 5
- 100k: CV_ATTEN → U1-5 (CTRL)
- Keep 10nF: U1-5 → GND (already in power section)
- Clamp diodes at U1-5:
  - 1N4148: anode U1-5, cathode +5V
  - 1N4148: anode GND, cathode U1-5

> If you want the “base+CV summing” variant, see `extensions/base-plus-cv.md`.

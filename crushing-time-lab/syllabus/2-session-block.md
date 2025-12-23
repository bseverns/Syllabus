# Two-session syllabus block: Crushing Time (AE Modular Breadboard Lab)

**Format:** 2 sessions × 90–120 minutes  
**Audience:** advanced high school / undergrad / community lab (no calculus; basic breadboard literacy)  
**Core build:** 5V sample-rate reducer (NE555 clock → CD40106 cleanup → CD4051 sample/hold) with MCP602 buffering and CV control.

## Course description (catalog-style)
In this two-session lab, students build a patchable circuit that “crushes” sound by sampling it too slowly. We’ll treat time as a material: clocks become instruments, control voltage becomes performance gesture, and the breadboard becomes a site for both engineering and aesthetics. Students leave with a working AE Modular breadboard module and a set of patch recipes that transform noise, oscillators, and drum voices into stepped, aliased textures.

## Learning outcomes
Students will be able to:
1. Build and verify a 5V power + reference system (Vref) for single-supply audio.
2. Explain (in plain language) how sample-rate reduction differs from amplitude “bit depth.”
3. Construct and tune an NE555 astable oscillator and relate RC values to rate.
4. Use a Schmitt trigger to stabilize a clock signal and reduce chatter.
5. Implement sample/hold with an analog switch and choose hold capacitor values for different textures.
6. Patch CV to modulate a parameter (crush rate) safely and musically (attenuation + filtering).
7. Debug a non-working breadboard circuit using measured checkpoints.

## Materials (per pair)
- Tangible Waves BRAEDBOARD module (or equivalent dual mini breadboards + patch jacks)
- 5V supply via AE system
- ICs: NE555, CD40106, CD4051, MCP602
- R: 1k, 4.7k, 10k, 47k, 100k (assortment)
- C: 1nF, 10nF, 100nF; electrolytic 10uF
- LEDs + 1k resistors (clock indicator)
- 2× 50k pots (rate + CV amount)
- Patch cables; optional scope or audio interface for visualization
- Multimeter (recommended)

## Session 1 — “Build the ground you stand on” (90–120 min)
### Agenda
- 0:00–0:10 Listening + intent: what does “crushing time” sound like?
- 0:10–0:35 Power rails, Vref, decoupling (build + measure)
- 0:35–1:00 Audio bias + MCP602 input buffer (build + test tone)
- 1:00–1:25 NE555 clock with rate pot + LED indicator (build + tune)
- 1:25–1:40 CD40106 cleanup (square the clock) + discussion of “why Schmitt”
- 1:40–2:00 Checkpoint tests + tidy wiring for Session 2

### Checkpoints (students must demonstrate)
- Vref ≈ 2.5V (±0.2V)
- Clock LED blinks and sweeps from slow to fast with the pot
- Audio buffer output sits near Vref with no input; passes audio when patched

### Student artifact
- Photo of build + 3 bullet notes: what worked, what failed, what surprised you

## Session 2 — “Turn it into an instrument” (90–120 min)
### Agenda
- 0:00–0:10 Recap: show Vref + clock on meter/scope
- 0:10–0:45 CD4051 sample/hold + hold capacitor experiments (10nF vs 100nF vs 10uF)
- 0:45–1:10 Output buffer + dry/crushed outputs
- 1:10–1:35 CV-controlled crush (CV in → filter → attenuate → 555 pin 5)
- 1:35–2:00 Patch lab: 4 patch recipes + mini performance share-out

### Checkpoints
- “Freeze”: slow clock yields stepped waveform / held samples
- “Rasp”: fast clock yields aliasing texture
- CV modulation changes crush rate without breaking the clock (attenuator matters)
- OUT1 (crushed) and OUT2 (dry) both function

### Student artifact
- 30–60s recording (phone is fine) + patch diagram + reflection paragraph

## Assessment (lightweight, studio-appropriate)
- Function (40%): circuit meets checkpoints
- Understanding (30%): students can explain Vref, clock, S/H in plain language
- Craft (15%): wiring hygiene, decoupling placed close to ICs, safe patching
- Expression (15%): patch choice + short performance or sound study

## Extensions (optional)
- Replace internal clock with AE CLK bus for rhythmic sync
- Use 4017 for stepped depth patterns (“bit mask sequencer”)
- Add LDR/LED for light-reactive crush rate

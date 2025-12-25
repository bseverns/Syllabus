# Patch recipes (AE Modular)

## 1) Classic crusher
- Source (VCO, sampler, drum) → CV socket (audio in)
- OUT1 → VCA → Mixer
- OUT2 → Mixer (dry blend)

## 2) Breathing crush
- LFO → CV socket (crush modulation)
- Audio source → CV socket *won’t work simultaneously* unless you dedicate another input.
  (Instructor note: offer a second input in an extension lab.)

## 3) Sync to system clock
- Use AE CLK socket as the clock source:
  - Disconnect internal clock feed to 40106
  - Patch AE CLK → 40106 input
- Now crusher locks to the rack tempo.

## 4) CV mode (slow clock)
- Set clock very slow (or patch slow clock)
- OUT1 becomes stepped CV you can patch to filter cutoff, VCA, etc.

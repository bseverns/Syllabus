# Student handout: Crushing Time Lab (AE Modular Breadboard)

## What we’re making
A small patchable circuit that **breaks audio on purpose** by sampling it too slowly.  
This is called **sample-rate reduction**. It makes crunchy, stepped, “early sampler” textures.

You’ll build it in layers:
1) **Vref** (a mid-point voltage so audio can live inside 0–5V)
2) **Clock** (a controllable pulse stream)
3) **Sample/Hold** (grabs audio snapshots at the clock rate)
4) **CV control** (modulate crush rate like an instrument)

## The golden rule (5V audio needs a center)
Because our system is **0–5V**, audio can’t swing negative.  
So we create **Vref ≈ 2.5V** and “float” the audio around it.

If Vref is wrong, *everything* gets weird.

## How to think about the sound
- **Slow clock** = big steps = “staircase” / robotic / frozen
- **Fast clock** = tiny steps = gritty / aliasing / “digital dust”
- **Hold capacitor** changes texture:
  - 10nF: sharper, brighter crackle
  - 100nF: classic mushy sampler smear
  - 10uF: long hold / slow glide (more CV-like)

## Safety + robustness (how not to lose an hour)
- Put decoupling caps **close** to each IC.
- Keep the clock wire short and away from the hold node.
- If it doesn’t work: stop, measure Vref, measure +5, then measure the clock.

## What you’ll turn in
- Photo of your build
- A short recording + patch diagram
- 3–5 sentences about what changed when you changed the clock and hold cap

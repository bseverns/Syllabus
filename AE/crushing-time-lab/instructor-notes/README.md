# Instructor notes

## Pacing
- The biggest time sink is usually: rails not shared / rail breaks / IC rotated.
- Insist on Vref measurement early. It prevents cascading confusion.

## Grouping
Pairs work well:
- One person wires, the other checks each row against the netlist + meter.

## Teaching moves that help
- Have students *name* the nodes: +5, GND, Vref, CLK, SAMP_NODE.
- Ask: “Where would noise matter most?” (answer: SAMP_NODE, Vref)
- Use intentional failure: remove a decoupling cap and listen for ticking.

## Minimal demo kit
- A simple oscillator voice
- One slow LFO
- Headphones or small speaker amp

## Accessibility
- Offer an “audio-only” path first (dry vs crush) before the deeper explanation.
- For non-math learners: describe the clock as a camera shutter.

## If you need to simplify further
Skip optional shaping. Focus on:
Vref → clock → S/H → buffers → CV modulation.

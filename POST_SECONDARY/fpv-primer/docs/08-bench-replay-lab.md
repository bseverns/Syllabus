# Bench replay lab (why it matters)

Bench replay is the bridge between flight data and disciplined iteration.

It lets you:

- test parsing
- tune smoothing
- compare mappings
- inspect failure behavior
- capture A/B output

...without flying again just to answer a software question.

## Standard bench replay ritual

1. Capture telemetry from a short, known scenario.
2. Freeze that dataset.
3. Replay it through the pipeline.
4. Measure, watch, and listen.
5. Change one thing.
6. Replay the exact same capture again.
7. Compare outputs, not memories.

## Good replay scenarios

- one clean launch and hover
- one simple turn
- one gate entry and exit
- one dropout or failsafe scenario
- one disarm / rearm cycle

## Why this matters pedagogically

Students often try to debug:

- flying
- configuration
- parsing
- mapping
- output rendering

all at once.

Bench replay separates those layers.

## Minimum output

After a replay lab, students should be able to say:

- what capture was used
- what changed between version A and B
- what stayed constant
- what claim the replay does and does not support

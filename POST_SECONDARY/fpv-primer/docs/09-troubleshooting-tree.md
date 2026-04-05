# Troubleshooting decision tree

Start from symptoms, not theories.

## Symptom: motors spin unexpectedly

Check in this order:

1. props off
2. arming state and mode configuration
3. receiver behavior
4. motor test state
5. FC reboot or runaway configuration error

Likely layers:

- modes
- receiver mapping
- bench ritual failure

## Symptom: no receiver movement in Betaflight

Check:

1. correct receiver protocol
2. wiring or integrated RX configuration
3. bind / model match state
4. radio model output
5. channel map assumptions

On an Air65-style ELRS baseline, do not start by blaming the FC if the receiver protocol or bind state is wrong.

## Symptom: telemetry exists but values are noisy or jumping

Check:

1. semantics definition
2. deadband
3. smoothing
4. whether the value is actually supposed to jitter
5. whether you are reading command, sensor, or derived state

Likely layers:

- semantics
- mapping math
- measurement assumptions

## Symptom: MIDI or downstream control is stuck

Check:

1. source value still updating
2. normalization range
3. clamp or quantization logic
4. dropout behavior
5. transport output path

Likely layers:

- parser
- mapping
- output transport

## Symptom: timing jitter or latency feels wrong

Check:

1. capture path and rate
2. smoothing settings
3. replay versus live comparison
4. serial bottlenecks
5. output-render load

Likely layers:

- capture
- replay
- output scheduling

## Symptom: craft flies, but the data story is nonsense

Check:

1. are you reading the intended variable?
2. are units documented?
3. is the signal valid in the current state?
4. does “zero” mean idle, disarmed, or missing?

This is usually a semantics problem before it is a coding problem.

## Instructor move

Require students to state:

- the symptom
- the first layer they are checking
- why that layer is first

That alone improves troubleshooting quality dramatically.

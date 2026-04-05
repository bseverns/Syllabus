# Mapping cookbook (telemetry -> control)

Mappings are compositions.

The same telemetry source can feel like:

- a smooth controller
- a twitchy trigger
- a stepped sequencer
- a limiter pump
- a dead, unplayable lie

The difference is not only the source signal. It is the conditioning and shape you impose.

## 1. Deadband

Use when:

- center jitter should not produce output
- ELRS or stick noise exists around rest

Pseudocode:

```text
if abs(x) < deadband:
  y = 0
else:
  y = x
```

## 2. Smoothing (EMA)

Use when:

- the source is too jagged for the target
- you want gesture memory

Pseudocode:

```text
y = alpha * x + (1 - alpha) * y_prev
```

Tradeoff:

- more smoothness
- more lag

## 3. Slew limiting

Use when:

- you want output to move like a physical object
- sudden jumps should be impossible

Pseudocode:

```text
delta = clamp(x - y_prev, -max_step, max_step)
y = y_prev + delta
```

## 4. Hysteresis

Use when:

- threshold chatter is a problem
- values hover near boundaries

Use different enter / exit thresholds so state does not flap.

## 5. Curves

Use curves when the destination should respond differently at the center than at the extremes.

Common options:

- linear
- exponential
- logarithmic
- S-curve
- piecewise custom

## 6. Quantization

Use when:

- you want steps, bins, or rhythm
- continuous movement should become discrete behavior

Pseudocode:

```text
step_index = floor(x * num_steps)
y = step_index / (num_steps - 1)
```

## 7. Safety rails

Always consider:

- min / max clamp
- dropout behavior
- out-of-range rejection
- “do nothing” state on invalid input

## Three example feels

### Feather
- deadband
- moderate EMA
- soft S-curve

Result:
- gentle
- forgiving
- expressive near center

### Blade
- minimal smoothing
- tight deadband
- piecewise aggressive curve

Result:
- sharp
- immediate
- unforgiving

### Ritual
- heavy smoothing
- quantization
- hysteresis

Result:
- stepped
- deliberate
- rhythmically stable

## Required artifact

Do not present a mapping without:

- a semantic definition of the source
- pseudocode or patch logic
- a claimed musical / control intent
- one replayable demonstration

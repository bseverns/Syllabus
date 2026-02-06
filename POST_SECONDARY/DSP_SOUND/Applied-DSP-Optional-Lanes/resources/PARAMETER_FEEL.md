# Parameter feel

A parameter is a promise.

Tools:
- tapers (linear/expo/log)
- smoothing (EMA, slew limiter)
- stepping (musical quantization)
- guardrails (clamps, sanity checks, NaN protection)

Checklist:
- no zipper noise on sweeps
- bounded behavior at extremes
- preset recall doesn’t “jump” (smooth to target)

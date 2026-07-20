# HW 04 — Non-blocking timing and jitter

1. Run the metronome for at least 100 ticks and capture `t_ms,tick,interval_ms`.
2. Plot interval error relative to the target. Report median, minimum, maximum, and one outlier.
3. Add a second independently scheduled behavior without `delay()`. Prove both continue.
4. Compare `previous += interval` with `previous = now` conceptually or experimentally; state which drift behavior you want.

Submit firmware, CSV/plot, one timing diagram, and `reflections/week04.md` explaining jitter, drift, and a design choice.

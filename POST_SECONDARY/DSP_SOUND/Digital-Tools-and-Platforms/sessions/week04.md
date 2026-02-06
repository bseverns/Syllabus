# Week 04 — Timing without delay (metronome + jitter)

## Goals
- Replace delay() patterns with millis()-based timing.
- Build a metronome tick loop.
- Reason about jitter and drift.

## Session arc (timed)
1. Warm-up (10 min): what goes wrong when you put delay() everywhere?
2. Mini-lecture (20–30 min): non-blocking loops, scheduling, drift vs jitter
3. Build + flash (40–60 min): flash Week04 metronome; log ticks
4. Observe + log (20 min): plot tick intervals; estimate jitter
5. Share-out (15 min): what caused jitter in your setup?
6. Close (10 min): preview sensor thresholds + hysteresis

## Prep (instructor)
- Prepare a brief diagram of loop timing.
- Optional: show why Serial print affects timing.

## Links
- `firmware/week04_metronome/`
- `labs/week04_timing_jitter.ipynb`
- `assignments/hw04_timing.md`

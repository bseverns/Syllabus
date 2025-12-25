# LABS: Lookahead Limiter

## Lab A — See the Envelope
- Run the demo and print `env` in dB for each block.
- Vary release_ms: 20, 50, 200. Describe what changes.

## Lab B — Threshold Games
- Change ceiling: −6 dB, −1 dB, −0.3 dB. Watch `GR` (gain reduction).
- Why does limiting at −0.3 dB still matter when interop devices sum signals?

## Lab C — Latency Tradeoffs
- Try lookahead 1 ms vs 5 ms vs 10 ms.
- Feed a click; which values avoid overshoot? How does it feel?

## Lab D — Hold Stage
- Implement `hold_ms`. Keep `env` at `g_req` for `hold_ms` before releasing.
- Compare pumping on a bass line.

## Lab E — Stereo Detectors
- Replace max(|L|,|R|) with mid/side detection (max of |M|,|S|).
- Does it change gain behavior on wide content?

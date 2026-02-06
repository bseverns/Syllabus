# Week 01 — Real-time thinking: measuring your loop

## Goals
- Define latency vs jitter in your own words and in a plot.
- Capture loop timing under zero load and under added load.
- Name one thing you will stop doing in firmware because you saw its cost.

## Session arc
1. Warm-up: a ‘bad sketch’ demo: delay + spam prints → feel the lag
2. Mini-lecture: what ‘real-time’ means for instruments (bounded response, not infinite speed)
3. Build: flash loop timing sketch; then add fake work
4. Measure: log loop dt; compute jitter stats in notebook
5. Critique: each group shows one plot and one hypothesis
6. Close: preview scheduling as composing time

## Links
- `firmware/week01_loop_timing/`
- `host/serial_loop_logger.py`
- `labs/week01_latency_jitter.ipynb`
- `bench/TEST_PROCEDURES.md`

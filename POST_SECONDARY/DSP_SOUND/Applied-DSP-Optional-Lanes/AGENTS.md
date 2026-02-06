# AGENTS.md

## Safe work
- Add tests + measurement scripts
- Improve docs clarity + examples
- Refactor to reduce allocations and clarify contracts
- Add parameter smoothing/taper utilities

## Don’t
- Change DSP behavior “by vibe” without before/after evidence
- Add heavy dependencies
- Bake lane-specific assumptions into `dsp/`

Evidence = plots, golden comparisons, or CPU measurements.

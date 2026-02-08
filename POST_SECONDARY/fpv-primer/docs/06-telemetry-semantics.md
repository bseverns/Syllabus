# Telemetry semantics (make the invisible consistent)

Define semantics *before* mapping:
- What does each value mean?
- What’s the expected range?
- What does “0” mean (idle? disarmed? missing?) 
- What happens when a value disappears?

Include:
- a small semantic table
- normalization rules (raw → 0..1)
- failure handling (hold last, decay, zero, safe default)

This file becomes the backbone for stable mappings.

# Build Step 06 — Output buffer (MCP602B) + dry/crush outs

## Goal
Provide stable outputs to the AE system.

## Wire
- MCP602B follower:
  - +IN ← SAMP_SHAPED (or SAMP_NODE if skipping shaping)
  - OUT → OUT_CRUSH
  - −IN tied to OUT
- OUT1 jack ← OUT_CRUSH
- OUT2 jack ← OUT_DRY (AUDIO_BIASED)

## Check
- OUT2 is clean/dry
- OUT1 is crushed

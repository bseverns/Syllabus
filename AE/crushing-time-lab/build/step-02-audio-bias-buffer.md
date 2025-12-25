# Build Step 02 — Audio bias + buffer (MCP602A)

## Goal
Take AE audio (0–5V) and buffer it safely inside our circuit.

## Wire
1. 100nF series cap: AUDIO_IN → IN_AC
2. 100k: IN_AC → Vref
3. MCP602A follower:
   - +IN → IN_AC
   - OUT → AUDIO_BIASED
   - −IN tied to OUT

## Check
- With no input, AUDIO_BIASED sits near Vref.
- With an audio source patched, AUDIO_BIASED carries that sound.

## Tip
If you can, listen to AUDIO_BIASED on OUT2 early (dry path).

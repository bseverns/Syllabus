# Build Step 04 — Clock cleanup (CD40106)

## Goal
Make the clock edges crisp and reduce chatter.

## Wire
- CLK_RAW → 40106 IN
- 40106 OUT → CLK

## Check
- If you have a scope: clean 0–5V square wave.
- If not: the crusher will sound more stable once you use CLK.

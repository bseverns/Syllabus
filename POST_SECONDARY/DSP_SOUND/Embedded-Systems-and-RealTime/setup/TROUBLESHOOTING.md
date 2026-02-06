# Troubleshooting

## Latency/jitter feels bad
Common culprits:
- blocking `delay()` calls
- `Serial.print()` inside tight loops at high rate
- polling too many inputs too frequently
- doing expensive math in the critical path

## ADC is noisy
- use a stable reference and good grounding
- add a small capacitor on wiper (hardware) + EMA smoothing (software)
- sample at a stable cadence; avoid reading immediately after large current changes (LEDs)

## USB weirdness
- some boards reset on serial open; add a boot grace period
- always print a startup banner so the host can sync

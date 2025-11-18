# Handout: Building a Lookahead Limiter (TMS Teaching Edition)

**Goals**
- Prevent clipping past a ceiling (e.g., −1 dBFS)
- Keep transients clean by acting *before* they occur (lookahead)
- Recover smoothly (release)

**Signal Flow**
```
input → detector (|L|,|R| max) → required_gain → envelope (release) ┐
                                                                   ├→ apply → output
input ──────────────────────────────────────────────────────────────┘ (delayed by lookahead)
```

**Core Equations**
- `ceiling_lin = 10^(ceiling_dB/20)`
- `g_req = clamp( ceiling_lin / max(|L|,|R|), 0..1 )`
- `env[n] = min( g_req,  env[n−1] + alpha * (1 − env[n−1]) )`
- `alpha = 1 − exp( −1 / (tau * fs) )`, `tau = release_ms / 1000`

**Parameters**
- *Ceiling (dBFS)*: typical −1 dB to −0.3 dB (headroom for interop chains)
- *Lookahead (ms)*: 1–5 ms (bigger = safer peaks, more latency)
- *Release (ms)*: 20–200 ms (short = chatter; long = pumping)

**Safety**
- Fixed-size buffers, no allocation on audio thread
- Clamp all divisions with epsilons

**Exercises**
1. Replace the peak detector with RMS (windowed). Compare sound.
2. Add a hold stage: keep `env` at `g_req` for X ms before releasing.
3. Oversample the detector by 2× and see if it catches sharper spikes.
4. Plot `env` over time for a snare transient (recorded sample).

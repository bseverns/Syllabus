#pragma once
/*
LookaheadLimiter — teaching implementation (mono/stereo)
=======================================================

Concept
-------
We delay the *audio* by a small lookahead window (e.g., 1–5 ms) so that a
detector can "see" peaks just before they emerge. We compute a gain envelope
that prevents the delayed audio from exceeding a ceiling, then smoothly
release the gain back toward unity.

This file is intentionally verbose and heavily commented for classroom use.

Key ideas students should notice:
- separation of *detection* and *application*
- envelope behaves like an instantaneous limiter with a smooth release tail
- lookahead introduces latency equal to N lookahead samples
- per-sample vs per-block APIs

Parameters
----------
- ceilingDb  : maximum allowed peak level in dBFS (e.g., -1 dB)
- lookaheadMs: delay applied to audio path so detector can react early
- releaseMs  : how quickly gain recovers back to 1.0 after a peak

Detector
--------
We use the absolute value of the stereo max (max(|L|, |R|)) as the peak
signal proxy. That's a common and easy-to-teach choice.

Math
----
Required gain g_req = ceiling / detector_level
We clamp g_req <= 1.0 and avoid division by 0.
Envelope g_env[n] = min( g_req,  g_env[n-1] + alpha * (1 - g_env[n-1]) )
Where alpha = 1 - exp( -1 / (tau * fs) ), tau = releaseMs/1000

Implementation notes
--------------------
- Fixed-size ring buffers (no allocation) for real-time safety.
- Detector is per-sample; you can extend to oversampling for better HF behavior.
- This is a simple limiter, not a multiband or lookahead compressor.
*/

#include <stdint.h>
#include <string.h>
#include <math.h>

namespace tms {

struct LookaheadLimiter {
  // --------- Tunables (safe bounds for class) ---------
  static constexpr int   kMaxLookaheadSamples = 4096;    // supports ~93 ms @ 44.1k
  static constexpr float kMinCeilingDb       = -12.0f;
  static constexpr float kMaxCeilingDb       = -0.1f;

  // --------- Runtime state ---------
  int   sampleRate   = 44100;
  int   lookaheadSmp = 256;         // ~5.8 ms @ 44.1k
  float ceilingLin   = dbToLin(-1.0f);
  float releaseAlpha = 0.005f;      // per-sample approach rate to unity
  float env          = 1.0f;        // current gain envelope

  // Audio delay lines
  float bufL[kMaxLookaheadSamples];
  float bufR[kMaxLookaheadSamples];
  int   w = 0;   // write index

  // --- Utilities ---
  static inline float dbToLin(float db) { return powf(10.0f, db * 0.05f); }
  static inline float linToDb(float x)  { return 20.0f * log10f(fmaxf(x, 1e-12f)); }
  static inline float clampf(float x, float lo, float hi){ return x<lo?lo:(x>hi?hi:x); }

  void setup(int sr){
    sampleRate = sr;
    memset(bufL, 0, sizeof(bufL));
    memset(bufR, 0, sizeof(bufR));
    w = 0; env = 1.0f;
    setLookaheadMs(5.8f);
    setCeilingDb(-1.0f);
    setReleaseMs(50.0f);
  }

  void setCeilingDb(float db){
    db = clampf(db, kMinCeilingDb, kMaxCeilingDb);
    ceilingLin = dbToLin(db);
  }

  void setLookaheadMs(float ms){
    int samples = (int)(0.001f * ms * sampleRate + 0.5f);
    samples = samples < 1 ? 1 : (samples > kMaxLookaheadSamples ? kMaxLookaheadSamples : samples);
    lookaheadSmp = samples;
  }

  void setReleaseMs(float ms){
    float tau = ms * 0.001f;
    // One-pole toward 1.0: y += alpha*(1 - y)
    releaseAlpha = 1.0f - expf(-1.0f / (tau * sampleRate));
  }

  // --- Mono tick (for teaching) ---
  float tickMono(float x){
    // Write incoming sample into ring
    bufL[w] = x;
    // Determine read index = w - lookahead (wrapped)
    int r = w - lookaheadSmp;
    if (r < 0) r += kMaxLookaheadSamples;

    // Peak detector uses current (non-delayed) sample
    float level = fabsf(x);
    float g_req = (level <= 1e-12f) ? 1.0f : clampf(ceilingLin / level, 0.0f, 1.0f);

    // Envelope: choose the smaller (instant limit) then release toward 1.0
    float g_env = fminf(g_req, env + releaseAlpha * (1.0f - env));
    env = g_env;

    // Apply to delayed sample
    float y = bufL[r] * env;

    // advance
    w = (w + 1) % kMaxLookaheadSamples;
    return y;
  }

  // --- Stereo tick ---
  void tickStereo(float xL, float xR, float& yL, float& yR){
    bufL[w] = xL;
    bufR[w] = xR;
    int r = w - lookaheadSmp;
    if (r < 0) r += kMaxLookaheadSamples;

    float level = fmaxf(fabsf(xL), fabsf(xR));
    float g_req = (level <= 1e-12f) ? 1.0f : clampf(ceilingLin / level, 0.0f, 1.0f);
    float g_env = fminf(g_req, env + releaseAlpha * (1.0f - env));
    env = g_env;

    yL = bufL[r] * env;
    yR = bufR[r] * env;

    w = (w + 1) % kMaxLookaheadSamples;
  }

  // --- Block process (arrays) ---
  void process(float* inL, float* inR, float* outL, float* outR, int n){
    for (int i = 0; i < n; ++i){
      tickStereo(inL ? inL[i] : 0.0f, inR ? inR[i] : 0.0f, outL[i], outR[i]);
    }
  }
};

} // namespace tms

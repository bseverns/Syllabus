/*
Limiter Lookahead Demo (Teensy-friendly, serial-print)
======================================================
This sketch exercise the teaching limiter in `LookaheadLimiter.h`.

What you'll see in Serial:

- dry peak vs. limited peak
- envelope gain in dB (how hard we clamp)
- effect of ceiling, lookahead, and release

Wire-up note: This prints only; to audition, route audio through the process()
call inside your Teensy audio update loop.
*/

#include <Arduino.h>
#include "LookaheadLimiter.h"

tms::LookaheadLimiter lim;

const int kSR = 44100;
float t = 0.0f;

// synth a nasty burst that tries to clip:
float synthSample(){
  // two sines, abrupt gain spike every ~0.2 s
  float s = 0.4f * (sinf(2*PI*220*t) + 0.6f*sinf(2*PI*880*t));
  if (fmodf(t, 0.2f) < 0.01f) s *= 10.0f; // sudden transient
  t += 1.0f / kSR;
  return s;
}

void setup(){
  Serial.begin(115200);
  while(!Serial && millis()<3000){}
  lim.setup(kSR);
  lim.setCeilingDb(-1.0f);
  lim.setLookaheadMs(5.0f);
  lim.setReleaseMs(50.0f);
  Serial.println("Lookahead limiter demo ready.");
}

void loop(){
  const int N = 128;
  float inL[N], inR[N], outL[N], outR[N];
  float peakDry = 0.0f, peakWet = 0.0f;

  for (int i=0;i<N;++i){
    float s = synthSample();
    inL[i]=inR[i]=s;
  }
  lim.process(inL,inR,outL,outR,N);

  for (int i=0;i<N;++i){
    peakDry = max(peakDry, fabs(inL[i]));
    peakWet = max(peakWet, fabs(outL[i]));
  }

  float gr_db = 20.0f * log10f( (peakWet>1e-12f)? (peakWet/peakDry) : 1.0f );
  Serial.printf("dry=%.3f wet=%.3f GR=%.1f dB env=%.1f dB\n",
                peakDry, peakWet, gr_db, 20.0f*log10f(lim.env));
  delay(30);
}

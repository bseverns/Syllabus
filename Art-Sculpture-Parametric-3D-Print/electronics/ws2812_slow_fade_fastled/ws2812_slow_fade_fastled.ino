/*
  WS2812 Slow Fades — Gallery-Safe (FastLED version)
  - Power-capped to ~30 mA at 5V via FastLED power management.
  - Very slow warm palette drift; no harsh steps; dithering off to reduce flicker.
  - Recommended boards: Arduino Nano, Pro Micro, QT Py (ATmega32u4), etc.
*/
#include <FastLED.h>

#define DATA_PIN   5
#define NUM_LEDS   16   // adjust to your strip length
#define LED_TYPE   WS2812B
#define COLOR_ORDER GRB

CRGB leds[NUM_LEDS];

// Soft palette between candle → amber → warm white
CRGBPalette16 warm1 = CRGBPalette16(
  CRGB::Black, CRGB(180, 70, 10), CRGB(255, 120, 20), CRGB(255, 160, 60),
  CRGB::Black, CRGB(220, 100, 20), CRGB(255, 180, 80), CRGB(255, 210, 120),
  CRGB::Black, CRGB(200, 90, 20), CRGB(255, 150, 50), CRGB(255, 190, 90),
  CRGB::Black, CRGB(230, 110, 25), CRGB(255, 200, 110), CRGB(255, 230, 140)
);

CRGBPalette16 target = warm1;
CRGBPalette16 current = warm1;

void setup(){
  FastLED.addLeds<LED_TYPE, DATA_PIN, COLOR_ORDER>(leds, NUM_LEDS);
  FastLED.setMaxPowerInVoltsAndMilliamps(5, 30);  // ≈ 30 mA cap
  FastLED.setBrightness(28);                      // extra safety cap
  FastLED.setDither(false);                       // avoid shimmer/flicker
  fill_solid(leds, NUM_LEDS, CRGB::Black);
  FastLED.show();
}

void loop(){
  // Slowly morph palette (optional future variants could swap target)
  nblendPaletteTowardPalette(current, target, 1);

  // Compute a very slow time base (minutes scale)
  uint16_t t = millis() / 64; // slower index progression

  for(int i=0; i<NUM_LEDS; i++){
    // Soft spatial offset for gentle gradient along the strip
    uint8_t idx = sin8((t/8) + i*6);
    CRGB c = ColorFromPalette(current, idx, 255, LINEARBLEND);

    // Very gentle breathing multiplier (0.75 … 1.0 approx.)
    uint8_t breath = 192 + sin8(t/4) / 8;
    c.nscale8_video(breath);

    leds[i] = c;
  }

  blur1d(leds, NUM_LEDS, 32);   // spatial smoothing

  FastLED.show();
  EVERY_N_MILLISECONDS(40) { /* idle */ }
}

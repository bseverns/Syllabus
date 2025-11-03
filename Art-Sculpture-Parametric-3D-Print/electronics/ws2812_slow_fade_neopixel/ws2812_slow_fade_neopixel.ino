/*
  WS2812 Slow Fades — Gallery-Safe (Adafruit NeoPixel version)
  - Uses conservative brightness to approximate <= 25–30 mA total current.
  - Extremely slow warm fade; gamma-corrected output.
*/
#include <Adafruit_NeoPixel.h>

#define DATA_PIN   5
#define NUM_LEDS   16
Adafruit_NeoPixel strip(NUM_LEDS, DATA_PIN, NEO_GRB + NEO_KHZ800);

// Rough power model: max white ≈ 60 mA/LED; set global cap
const uint16_t CAP_MA = 25; // overall current budget
uint8_t safeBrightness(){
  // brightness ≈ CAP / (60mA * NUM_LEDS) * 255; add gentle fudge factor
  float b = (float)CAP_MA / (60.0f * NUM_LEDS) * 255.0f * 1.2f;
  if (b < 4) b = 4;    // ensure visible
  if (b > 40) b = 40;  // upper bound for small strips
  return (uint8_t)b;
}

uint32_t warmFromPhase(float p){
  // p in [0..1]: morph candle→amber→warm white
  float r = 150 + 80 * p;
  float g = 40  + 120 * p * 0.7;
  float b = 10  + 60  * p * 0.3;
  return strip.Color((uint8_t)r,(uint8_t)g,(uint8_t)b);
}

void setup(){
  strip.begin();
  strip.setBrightness(safeBrightness());
  strip.show();
}

void loop(){
  // very slow timebase
  float t = millis() / 60000.0f; // minutes
  float phase = fmod(t * 0.25f, 1.0f); // full cycle ~4 minutes
  for (int i=0; i<NUM_LEDS; i++){
    float offset = (float)i / (float)NUM_LEDS;
    float local = fmod(phase + offset * 0.15f, 1.0f);
    // breathing envelope 0.85..1.0
    float env = 0.925f + 0.075f * (0.5f + 0.5f * sinf(millis()/4000.0f + i*0.2f));
    uint32_t c = warmFromPhase(local);
    // gamma correction via library
    uint32_t g = strip.gamma32(c);
    // apply envelope by scaling brightness per pixel (approx.)
    uint8_t r = (uint8_t)(((g >> 16) & 0xFF) * env);
    uint8_t gr= (uint8_t)(((g >>  8) & 0xFF) * env);
    uint8_t b = (uint8_t)(( g        & 0xFF) * env);
    strip.setPixelColor(i, r, gr, b);
  }
  strip.show();
  delay(40);
}

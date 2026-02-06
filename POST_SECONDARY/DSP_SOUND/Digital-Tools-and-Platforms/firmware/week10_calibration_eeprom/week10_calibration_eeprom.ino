// Week 10 — Calibration + persistence (EEPROM)
// Note: EEPROM library availability differs by board.
// For Arduino AVR: <EEPROM.h> works.
// For Teensy: EEPROM is supported but differs slightly.

#include <EEPROM.h>

const int POT = A0;
int minV = 1023;
int maxV = 0;

// EEPROM addresses
const int ADDR_MIN = 0;
const int ADDR_MAX = 2;

void setup() {
  Serial.begin(115200);
  delay(500);

  EEPROM.get(ADDR_MIN, minV);
  EEPROM.get(ADDR_MAX, maxV);

  // sanity
  if (minV < 0 || minV > 1023) minV = 1023;
  if (maxV < 0 || maxV > 1023) maxV = 0;

  Serial.print("Loaded min/max: "); Serial.print(minV); Serial.print(" / "); Serial.println(maxV);
  Serial.println("Rotate pot fully. Send 'S' over Serial to save.");
}

void loop() {
  int raw = analogRead(POT);
  if (raw < minV) minV = raw;
  if (raw > maxV) maxV = raw;

  // Listen for save
  if (Serial.available()) {
    char c = (char)Serial.read();
    if (c == 'S') {
      EEPROM.put(ADDR_MIN, minV);
      EEPROM.put(ADDR_MAX, maxV);
      Serial.print("Saved min/max: "); Serial.print(minV); Serial.print(" / "); Serial.println(maxV);
    }
  }

  static unsigned long lastLog = 0;
  unsigned long now = millis();
  if (now - lastLog > 50) {
    lastLog = now;
    Serial.print(now); Serial.print(",");
    Serial.print(raw); Serial.print(",");
    Serial.print(minV); Serial.print(",");
    Serial.println(maxV);
  }
}

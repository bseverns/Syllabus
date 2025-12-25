#pragma once
#include <Arduino.h>
class MIDISender {
public:
  static inline void cc(uint8_t ch, uint8_t cc, uint8_t v){
    Serial.write(0xB0 | (ch & 0x0F));
    Serial.write(cc & 0x7F);
    Serial.write(v & 0x7F);
  }
};

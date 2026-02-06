// Week 09 — Diagnostics + safe mode on boot
// Hold BTN on boot → SAFE mode (defaults, ignores stored config).
//
// Prints:
//  MODE,SAFE or MODE,NORMAL
//  INFO:...

#include <EEPROM.h>

const int BTN = 2;

struct Config { uint8_t version; uint8_t ch; uint8_t sum; };
const int ADDR=0;
Config cfg;

uint8_t sum(const Config& c){ return (uint8_t)(c.version + c.ch + 0x33); }

bool load() {
  EEPROM.get(ADDR, cfg);
  return (cfg.version==1 && cfg.ch>=1 && cfg.ch<=16 && cfg.sum==sum(cfg));
}

void defaults(){ cfg.version=1; cfg.ch=1; cfg.sum=sum(cfg); }

bool safeMode = false;

void setup() {
  pinMode(BTN, INPUT_PULLUP);
  Serial.begin(115200);
  delay(50);
  safeMode = (digitalRead(BTN) == LOW);
  delay(450);

  if (safeMode) {
    defaults();
    Serial.println("MODE,SAFE");
  } else {
    if (!load()) { defaults(); EEPROM.put(ADDR, cfg); }
    Serial.println("MODE,NORMAL");
  }

  Serial.print("INFO:FW=1.0;CH="); Serial.println(cfg.ch);
}

void loop() { /* no-op */ }

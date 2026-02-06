// Week 08 — Persistence (config struct + version + CRC-ish)
// Stores a small config with a simple checksum.
// Commands: INFO | SETCH <1-16> | RESET

#include <EEPROM.h>

struct Config {
  uint8_t version;
  uint8_t midiCh;
  uint8_t checksum; // simple additive checksum
};

const int ADDR = 0;
Config cfg;

uint8_t calcChecksum(const Config& c) {
  return (uint8_t)(c.version + c.midiCh + 0x5A);
}

void setDefaults() {
  cfg.version = 1;
  cfg.midiCh = 1;
  cfg.checksum = calcChecksum(cfg);
}

bool load() {
  EEPROM.get(ADDR, cfg);
  if (cfg.version != 1) return false;
  if (cfg.midiCh < 1 || cfg.midiCh > 16) return false;
  if (cfg.checksum != calcChecksum(cfg)) return false;
  return true;
}

void save() {
  cfg.checksum = calcChecksum(cfg);
  EEPROM.put(ADDR, cfg);
}

void setup() {
  Serial.begin(115200);
  delay(500);
  if (!load()) { setDefaults(); save(); Serial.println("CFG:DEFAULTED"); }
  Serial.println("READY");
}

String line;

void info() {
  Serial.print("INFO:FW=1.0;CH="); Serial.println(cfg.midiCh);
}

void handle(const String& s) {
  if (s == "INFO") { info(); return; }
  if (s.startsWith("SETCH ")) {
    int ch = s.substring(6).toInt();
    if (ch >= 1 && ch <= 16) { cfg.midiCh = (uint8_t)ch; save(); Serial.println("OK"); }
    else Serial.println("ERR");
    return;
  }
  if (s == "RESET") {
    setDefaults(); save(); Serial.println("OK");
    return;
  }
  Serial.println("ERR");
}

void loop() {
  while (Serial.available()) {
    char c = (char)Serial.read();
    if (c == '\n' || c == '\r') {
      if (line.length()) { handle(line); line = ""; }
    } else line += c;
  }
}

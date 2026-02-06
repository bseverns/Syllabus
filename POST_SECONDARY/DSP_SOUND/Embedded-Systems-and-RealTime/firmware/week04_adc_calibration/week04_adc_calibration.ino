// Week 04 — ADC calibration + smoothing (one knob)
// Goal: store min/max so full travel maps cleanly.
//
// Commands:
//  CAL_START  (move knob fully across range for 5 seconds)
//  CAL_SAVE
//  SHOW
//
// Output: CAL,<min>,<max>,VAL,<mapped_0_127>

#include <EEPROM.h>

struct Cal {
  uint8_t version;
  int minv;
  int maxv;
};

const int ADDR = 0;
const int POT = A0;
Cal cal;

bool calibrating = false;
unsigned long calEnd = 0;

float ema = 0.0f;
const float ALPHA = 0.15f;

String line;

void defaults() {
  cal.version = 1;
  cal.minv = 0;
  cal.maxv = 1023;
}

void setup() {
  Serial.begin(115200);
  delay(500);

  EEPROM.get(ADDR, cal);
  if (cal.version != 1 || cal.minv < 0 || cal.maxv > 1023 || cal.minv >= cal.maxv) {
    defaults();
    EEPROM.put(ADDR, cal);
    Serial.println("CAL:DEFAULTED");
  }
  ema = analogRead(POT);
  Serial.println("READY");
}

void handle(const String& s) {
  if (s == "CAL_START") {
    calibrating = true;
    calEnd = millis() + 5000;
    cal.minv = 1023;
    cal.maxv = 0;
    Serial.println("OK");
  } else if (s == "CAL_SAVE") {
    calibrating = false;
    if (cal.minv < cal.maxv) {
      EEPROM.put(ADDR, cal);
      Serial.println("OK");
    } else Serial.println("ERR");
  } else if (s == "SHOW") {
    Serial.print("CAL,"); Serial.print(cal.minv); Serial.print(","); Serial.println(cal.maxv);
  } else {
    Serial.println("ERR");
  }
}

int mapCal(int raw) {
  raw = constrain(raw, cal.minv, cal.maxv);
  long v = (long)(raw - cal.minv) * 127L / (long)(cal.maxv - cal.minv);
  return (int)constrain(v, 0, 127);
}

void loop() {
  // serial command parsing
  while (Serial.available()) {
    char c = (char)Serial.read();
    if (c == '\n' || c == '\r') {
      if (line.length()) { handle(line); line = ""; }
    } else line += c;
  }

  // sample knob
  int raw = analogRead(POT);
  ema = ALPHA * raw + (1.0f - ALPHA) * ema;

  if (calibrating) {
    if (raw < cal.minv) cal.minv = raw;
    if (raw > cal.maxv) cal.maxv = raw;
    if ((long)(millis() - calEnd) >= 0) {
      calibrating = false;
      Serial.println("CAL_DONE");
    }
  }

  static unsigned long last = 0;
  unsigned long now = millis();
  if (now - last >= 10) { // 100 Hz report
    last = now;
    int val = mapCal((int)ema);
    Serial.print("CAL,"); Serial.print(cal.minv); Serial.print(","); Serial.print(cal.maxv);
    Serial.print(",VAL,"); Serial.println(val);
  }
}

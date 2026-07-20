#include <EEPROM.h>

// Week 10: hold D2 to GND during reset for a 5-second A0 calibration.
const uint8_t CALIBRATE_PIN = 2;
const uint8_t SENSOR_PIN = A0;
const uint16_t MAGIC = 0xCA1B;
const unsigned long CALIBRATION_MS = 5000;
const unsigned long REPORT_MS = 50;

struct Calibration {
  uint16_t magic;
  int minimum;
  int maximum;
};

Calibration calibration = {MAGIC, 0, 1023};
unsigned long lastReport = 0;

void runCalibration() {
  calibration.minimum = 1023;
  calibration.maximum = 0;
  const unsigned long started = millis();
  while (millis() - started < CALIBRATION_MS) {
    const int value = analogRead(SENSOR_PIN);
    if (value < calibration.minimum) calibration.minimum = value;
    if (value > calibration.maximum) calibration.maximum = value;
    delay(2);  // Deliberate, bounded setup-only sampling.
  }
  if (calibration.maximum - calibration.minimum < 10) {
    calibration.minimum = 0;
    calibration.maximum = 1023;
    Serial.println("ERR,CALIBRATION_RANGE");
  } else {
    EEPROM.put(0, calibration);
    Serial.println("ACK,CALIBRATION_SAVED");
  }
}

void setup() {
  pinMode(CALIBRATE_PIN, INPUT_PULLUP);
  Serial.begin(115200);
  EEPROM.get(0, calibration);
  if (calibration.magic != MAGIC || calibration.maximum <= calibration.minimum) {
    calibration = {MAGIC, 0, 1023};
  }
  if (digitalRead(CALIBRATE_PIN) == LOW) runCalibration();
}

void loop() {
  const int raw = analogRead(SENSOR_PIN);
  const long mapped = map(constrain(raw, calibration.minimum, calibration.maximum),
                          calibration.minimum, calibration.maximum, 0, 127);
  const unsigned long now = millis();
  if (now - lastReport >= REPORT_MS) {
    lastReport = now;
    Serial.print(now);
    Serial.print(',');
    Serial.print(raw);
    Serial.print(',');
    Serial.print(mapped);
    Serial.print(',');
    Serial.print(calibration.minimum);
    Serial.print(',');
    Serial.println(calibration.maximum);
  }
}

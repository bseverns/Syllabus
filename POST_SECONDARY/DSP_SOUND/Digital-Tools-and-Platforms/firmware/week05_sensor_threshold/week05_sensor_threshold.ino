// Week 05 — Sensor thresholds + hysteresis
// Example: photoresistor on A0. Output an LED toggle when crossing thresholds.
// Serial: t_ms,raw,state

const int SENSOR_PIN = A0;
const int LED_PIN = LED_BUILTIN;

// Tune for your sensor + lighting
const int THRESH_UP = 650;
const int THRESH_DOWN = 600;

bool state = false;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
  delay(500);
}

void loop() {
  unsigned long now = millis();
  int raw = analogRead(SENSOR_PIN);

  // Hysteresis: separate thresholds for up/down transitions
  if (!state && raw > THRESH_UP) state = true;
  if (state && raw < THRESH_DOWN) state = false;

  digitalWrite(LED_PIN, state ? HIGH : LOW);

  static unsigned long lastLog = 0;
  if (now - lastLog >= 20) {
    lastLog = now;
    Serial.print(now);
    Serial.print(",");
    Serial.print(raw);
    Serial.print(",");
    Serial.println(state ? 1 : 0);
  }
}

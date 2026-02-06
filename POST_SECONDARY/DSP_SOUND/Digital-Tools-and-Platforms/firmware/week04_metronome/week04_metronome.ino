// Week 04 — Timing without delay (metronome)
// Goal: build a non-blocking timer loop using millis().

const int LED_PIN = LED_BUILTIN;
int bpm = 120;

unsigned long intervalMs() {
  return (unsigned long)(60000.0 / (float)bpm);
}

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
  delay(500);
  Serial.println("t_ms,tick");
}

void loop() {
  static unsigned long lastTick = 0;
  unsigned long now = millis();
  if (now - lastTick >= intervalMs()) {
    lastTick += intervalMs();
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));

    Serial.print(now);
    Serial.println(",1");
  }
}

// Week 02 — Button + Debounce + Logging
// Wiring: button between pin 2 and GND (INPUT_PULLUP).
// Serial output: t_ms,raw,debounced

const int BTN_PIN = 2;
const unsigned long DEBOUNCE_MS = 20;

int rawState = HIGH;
int debouncedState = HIGH;
int lastRaw = HIGH;
unsigned long lastChange = 0;

void setup() {
  pinMode(BTN_PIN, INPUT_PULLUP);
  Serial.begin(115200);
  delay(500);
}

void loop() {
  unsigned long now = millis();
  rawState = digitalRead(BTN_PIN);

  if (rawState != lastRaw) {
    lastRaw = rawState;
    lastChange = now;
  }

  // Debounce: accept change only after stable window
  if ((now - lastChange) > DEBOUNCE_MS && debouncedState != rawState) {
    debouncedState = rawState;
  }

  // Log at ~100 Hz
  static unsigned long lastLog = 0;
  if (now - lastLog >= 10) {
    lastLog = now;
    Serial.print(now);
    Serial.print(",");
    Serial.print(rawState == LOW ? 1 : 0);
    Serial.print(",");
    Serial.println(debouncedState == LOW ? 1 : 0);
  }
}

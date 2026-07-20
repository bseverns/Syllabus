// Week 02: active-low button on D2; reports t_ms,rawPressed,debouncedPressed.
const uint8_t BUTTON_PIN = 2;
const unsigned long DEBOUNCE_MS = 25;
const unsigned long REPORT_MS = 5;

bool lastRaw = false;
bool debounced = false;
unsigned long rawChangedAt = 0;
unsigned long lastReport = 0;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Serial.begin(115200);
}

void loop() {
  const unsigned long now = millis();
  const bool rawPressed = digitalRead(BUTTON_PIN) == LOW;
  if (rawPressed != lastRaw) {
    lastRaw = rawPressed;
    rawChangedAt = now;
  }
  if (now - rawChangedAt >= DEBOUNCE_MS) {
    debounced = rawPressed;
  }
  if (now - lastReport >= REPORT_MS) {
    lastReport = now;
    Serial.print(now);
    Serial.print(',');
    Serial.print(rawPressed ? 1 : 0);
    Serial.print(',');
    Serial.println(debounced ? 1 : 0);
  }
}

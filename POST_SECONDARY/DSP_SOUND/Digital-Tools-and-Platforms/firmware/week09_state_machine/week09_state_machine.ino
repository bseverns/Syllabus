// Week 09: button advances IDLE -> PLAY -> CONFIG; pot is state-dependent.
enum Mode { IDLE, PLAY, CONFIG };
const uint8_t BUTTON_PIN = 2;
const uint8_t LED_PINS[3] = {9, 10, 11};
const uint8_t CONTROL_PIN = A0;
const unsigned long DEBOUNCE_MS = 25;
const unsigned long REPORT_MS = 100;

Mode mode = IDLE;
bool lastRaw = false;
bool stablePressed = false;
unsigned long changedAt = 0;
unsigned long lastReport = 0;

void showMode() {
  for (uint8_t i = 0; i < 3; i++) digitalWrite(LED_PINS[i], i == (uint8_t)mode ? HIGH : LOW);
}

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  for (uint8_t i = 0; i < 3; i++) pinMode(LED_PINS[i], OUTPUT);
  Serial.begin(115200);
  showMode();
}

void loop() {
  const unsigned long now = millis();
  const bool rawPressed = digitalRead(BUTTON_PIN) == LOW;
  if (rawPressed != lastRaw) {
    lastRaw = rawPressed;
    changedAt = now;
  }
  if (now - changedAt >= DEBOUNCE_MS && rawPressed != stablePressed) {
    stablePressed = rawPressed;
    if (stablePressed) {
      mode = (Mode)(((uint8_t)mode + 1) % 3);
      showMode();
      Serial.print("EVENT,MODE,");
      Serial.println((uint8_t)mode);
    }
  }
  if (now - lastReport >= REPORT_MS) {
    lastReport = now;
    Serial.print("DATA,");
    Serial.print(now);
    Serial.print(',');
    Serial.print((uint8_t)mode);
    Serial.print(',');
    Serial.println(analogRead(CONTROL_PIN));
  }
}

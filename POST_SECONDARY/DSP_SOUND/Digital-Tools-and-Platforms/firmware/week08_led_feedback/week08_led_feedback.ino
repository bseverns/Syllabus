// Week 08 minimum route: three discrete LEDs communicate state without a library.
// Wire D9/D10/D11 through appropriate current-limiting resistors to LEDs.
const uint8_t LED_PINS[3] = {9, 10, 11};
const uint8_t CONTROL_PIN = A0;
const unsigned long REPORT_MS = 50;
int currentState = -1;
unsigned long lastReport = 0;

void showState(int state) {
  for (uint8_t i = 0; i < 3; i++) digitalWrite(LED_PINS[i], i == state ? HIGH : LOW);
}

void setup() {
  for (uint8_t i = 0; i < 3; i++) pinMode(LED_PINS[i], OUTPUT);
  Serial.begin(115200);
}

void loop() {
  const int raw = analogRead(CONTROL_PIN);
  const int state = raw < 341 ? 0 : (raw < 682 ? 1 : 2);
  if (state != currentState) {
    currentState = state;
    showState(state);
  }
  const unsigned long now = millis();
  if (now - lastReport >= REPORT_MS) {
    lastReport = now;
    Serial.print(now);
    Serial.print(',');
    Serial.print(currentState);
    Serial.print(',');
    Serial.println(raw);
  }
}

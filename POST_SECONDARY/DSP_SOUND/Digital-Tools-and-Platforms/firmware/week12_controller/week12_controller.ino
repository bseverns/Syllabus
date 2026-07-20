// Week 12 Uno-compatible baseline: 4 pots, 4 active-low buttons, 3 state LEDs.
const uint8_t KNOB_PINS[4] = {A0, A1, A2, A3};
const uint8_t BUTTON_PINS[4] = {2, 3, 4, 5};
const uint8_t LED_PINS[3] = {9, 10, 11};
const unsigned long DEBOUNCE_MS = 25;
const unsigned long REPORT_MS = 20;

bool lastRaw[4] = {false, false, false, false};
bool stablePressed[4] = {false, false, false, false};
unsigned long changedAt[4] = {0, 0, 0, 0};
int lastKnob[4] = {-999, -999, -999, -999};
uint8_t mode = 0;
unsigned long lastReport = 0;

void showMode() {
  for (uint8_t i = 0; i < 3; i++) digitalWrite(LED_PINS[i], i == mode ? HIGH : LOW);
}

void setup() {
  for (uint8_t i = 0; i < 4; i++) pinMode(BUTTON_PINS[i], INPUT_PULLUP);
  for (uint8_t i = 0; i < 3; i++) pinMode(LED_PINS[i], OUTPUT);
  Serial.begin(115200);
  showMode();
}

void loop() {
  const unsigned long now = millis();
  for (uint8_t i = 0; i < 4; i++) {
    const bool rawPressed = digitalRead(BUTTON_PINS[i]) == LOW;
    if (rawPressed != lastRaw[i]) {
      lastRaw[i] = rawPressed;
      changedAt[i] = now;
    }
    if (now - changedAt[i] >= DEBOUNCE_MS && rawPressed != stablePressed[i]) {
      stablePressed[i] = rawPressed;
      if (stablePressed[i]) {
        if (i == 0) {
          mode = (mode + 1) % 3;
          showMode();
        }
        Serial.print("BUTTON,");
        Serial.print(now);
        Serial.print(',');
        Serial.print(i);
        Serial.print(',');
        Serial.print(1);
        Serial.print(',');
        Serial.println(mode);
      }
    }
  }

  if (now - lastReport >= REPORT_MS) {
    lastReport = now;
    for (uint8_t i = 0; i < 4; i++) {
      const int value = map(analogRead(KNOB_PINS[i]), 0, 1023, 0, 127);
      if (abs(value - lastKnob[i]) >= 2) {
        lastKnob[i] = value;
        Serial.print("KNOB,");
        Serial.print(now);
        Serial.print(',');
        Serial.print(i);
        Serial.print(',');
        Serial.print(value);
        Serial.print(',');
        Serial.println(mode);
      }
    }
  }
}

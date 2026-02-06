// Week 03 — Debounce + edge detection → events
// Output:
//   EVT,BTN,<id>,DOWN
//   EVT,BTN,<id>,UP
//
// Wiring: button to D2, INPUT_PULLUP.

const int BTN_PIN = 2;
const unsigned long DEBOUNCE_MS = 25;

int stable = HIGH;
int lastRaw = HIGH;
unsigned long lastChange = 0;

void setup() {
  pinMode(BTN_PIN, INPUT_PULLUP);
  Serial.begin(115200);
  delay(500);
}

void emit(const char* s) {
  Serial.print("EVT,BTN,0,");
  Serial.println(s);
}

void loop() {
  unsigned long now = millis();
  int raw = digitalRead(BTN_PIN);

  if (raw != lastRaw) {
    lastRaw = raw;
    lastChange = now;
  }

  if ((now - lastChange) > DEBOUNCE_MS && raw != stable) {
    stable = raw;
    if (stable == LOW) emit("DOWN");
    else emit("UP");
  }
}

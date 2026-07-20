// Week 01: non-blocking blink plus a numeric Serial stream.
const uint8_t LED_PIN = LED_BUILTIN;
const unsigned long BLINK_MS = 500;
const unsigned long REPORT_MS = 100;

unsigned long lastBlink = 0;
unsigned long lastReport = 0;
bool ledState = false;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  const unsigned long now = millis();
  if (now - lastBlink >= BLINK_MS) {
    lastBlink = now;
    ledState = !ledState;
    digitalWrite(LED_PIN, ledState);
  }
  if (now - lastReport >= REPORT_MS) {
    lastReport = now;
    Serial.print(now);
    Serial.print(',');
    Serial.println(ledState ? 1 : 0);
  }
}

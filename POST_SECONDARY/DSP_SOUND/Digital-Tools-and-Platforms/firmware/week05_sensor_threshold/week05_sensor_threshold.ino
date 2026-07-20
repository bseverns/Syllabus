// Week 05: analog sensor on A0 with hysteresis; LED on D9 through a resistor.
const uint8_t SENSOR_PIN = A0;
const uint8_t LED_PIN = 9;
const int ON_THRESHOLD = 650;
const int OFF_THRESHOLD = 550;
const unsigned long REPORT_MS = 20;

bool active = false;
unsigned long lastReport = 0;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  const int raw = analogRead(SENSOR_PIN);
  if (!active && raw >= ON_THRESHOLD) active = true;
  if (active && raw <= OFF_THRESHOLD) active = false;
  digitalWrite(LED_PIN, active ? HIGH : LOW);

  const unsigned long now = millis();
  if (now - lastReport >= REPORT_MS) {
    lastReport = now;
    Serial.print(now);
    Serial.print(',');
    Serial.print(raw);
    Serial.print(',');
    Serial.println(active ? 1 : 0);
  }
}

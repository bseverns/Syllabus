// Week 04: millis()-scheduled metronome; reports t_ms,tick,interval_ms.
const uint8_t LED_PIN = LED_BUILTIN;
const unsigned long TICK_MS = 250;

unsigned long previousTick = 0;
unsigned long tickCount = 0;
bool ledState = false;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
  previousTick = millis();
}

void loop() {
  const unsigned long now = millis();
  if (now - previousTick >= TICK_MS) {
    const unsigned long actualInterval = now - previousTick;
    previousTick += TICK_MS;  // Holds the schedule instead of resetting to now.
    tickCount++;
    ledState = !ledState;
    digitalWrite(LED_PIN, ledState);
    Serial.print(now);
    Serial.print(',');
    Serial.print(tickCount);
    Serial.print(',');
    Serial.println(actualInterval);
  }
}

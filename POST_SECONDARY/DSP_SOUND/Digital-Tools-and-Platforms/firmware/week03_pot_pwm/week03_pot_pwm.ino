// Week 03: potentiometer on A0, PWM LED on D9 through a resistor.
// ADC_MAX is 1023 for a default 10-bit Arduino Uno/Nano ADC; adapt locally.
const uint8_t POT_PIN = A0;
const uint8_t LED_PIN = 9;
const int ADC_MAX = 1023;
const float SMOOTHING = 0.15f;
const int DEADBAND = 4;
const unsigned long REPORT_MS = 20;

float smoothed = 0.0f;
int stableValue = 0;
unsigned long lastReport = 0;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
  smoothed = analogRead(POT_PIN);
  stableValue = (int)smoothed;
}

void loop() {
  const int raw = analogRead(POT_PIN);
  smoothed += SMOOTHING * (raw - smoothed);
  if (abs((int)smoothed - stableValue) >= DEADBAND) {
    stableValue = (int)smoothed;
  }
  const int pwm = map(stableValue, 0, ADC_MAX, 0, 255);
  analogWrite(LED_PIN, constrain(pwm, 0, 255));

  const unsigned long now = millis();
  if (now - lastReport >= REPORT_MS) {
    lastReport = now;
    Serial.print(now);
    Serial.print(',');
    Serial.print(raw);
    Serial.print(',');
    Serial.print(smoothed, 2);
    Serial.print(',');
    Serial.println(pwm);
  }
}

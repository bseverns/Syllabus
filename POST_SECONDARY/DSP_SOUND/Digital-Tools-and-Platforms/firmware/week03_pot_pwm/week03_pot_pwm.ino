// Week 03 — Potentiometer → PWM LED + smoothing + deadband
// Wiring: pot wiper to A0, ends to 5V/3.3V and GND.
// LED on PWM pin 9 (change if needed).
// Serial output: t_ms,raw,smoothed,mappedPWM

const int POT_PIN = A0;
const int LED_PIN = 9;

// Exponential moving average
float ema = 0.0f;
const float ALPHA = 0.1f;

// Deadband in raw ADC units (0..1023 on Arduino, 0..4095 on some boards)
const int DEADBAND = 4;
int lastRaw = 0;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
  delay(500);
  lastRaw = analogRead(POT_PIN);
  ema = (float)lastRaw;
}

void loop() {
  unsigned long now = millis();
  int raw = analogRead(POT_PIN);

  // Deadband: ignore tiny changes
  if (abs(raw - lastRaw) < DEADBAND) raw = lastRaw;
  lastRaw = raw;

  // EMA smoothing
  ema = (1.0f - ALPHA) * ema + ALPHA * (float)raw;

  // Map to PWM
  int pwm = map((int)ema, 0, 1023, 0, 255);
  pwm = constrain(pwm, 0, 255);
  analogWrite(LED_PIN, pwm);

  // Log at ~100 Hz
  static unsigned long lastLog = 0;
  if (now - lastLog >= 10) {
    lastLog = now;
    Serial.print(now);
    Serial.print(",");
    Serial.print(raw);
    Serial.print(",");
    Serial.print((int)ema);
    Serial.print(",");
    Serial.println(pwm);
  }
}

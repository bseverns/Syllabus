// Week 01 — Measure your loop timing (microseconds)
// Prints: LOOP,<dt_us>
// Warning: Serial printing affects timing; that is part of the lesson.

unsigned long last = 0;

void setup() {
  Serial.begin(115200);
  delay(500);
  last = micros();
}

void loop() {
  unsigned long now = micros();
  unsigned long dt = now - last;
  last = now;

  Serial.print("LOOP,");
  Serial.println(dt);

  // Do nothing else; then gradually add work and watch jitter grow.
}

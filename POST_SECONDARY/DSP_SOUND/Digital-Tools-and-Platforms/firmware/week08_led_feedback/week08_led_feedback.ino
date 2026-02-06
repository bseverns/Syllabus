// Week 08 — LED feedback (scaffold)
// If you have addressable LEDs, you can use FastLED or Adafruit NeoPixel.
// This scaffold stays library-free and uses 3 discrete LEDs (pins 5,6,9).

const int LED1 = 5;
const int LED2 = 6;
const int LED3 = 9;

void setup() {
  pinMode(LED1, OUTPUT); pinMode(LED2, OUTPUT); pinMode(LED3, OUTPUT);
  Serial.begin(115200);
  delay(500);
}

void loop() {
  unsigned long now = millis();
  int phase = (now / 500) % 6;

  digitalWrite(LED1, phase < 2 ? HIGH : LOW);
  digitalWrite(LED2, (phase >= 2 && phase < 4) ? HIGH : LOW);
  digitalWrite(LED3, phase >= 4 ? HIGH : LOW);

  // Log state for analysis
  Serial.print(now); Serial.print(",");
  Serial.print(digitalRead(LED1)); Serial.print(",");
  Serial.print(digitalRead(LED2)); Serial.print(",");
  Serial.println(digitalRead(LED3));
}

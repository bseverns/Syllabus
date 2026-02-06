// Week 01 — Blink + Serial Hello
// Goal: prove you can flash firmware and see Serial output.
// Board: Arduino/Teensy (adjust LED_BUILTIN pin if needed)

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
  delay(500);
  Serial.println("HELLO_FROM_BOARD");
}

void loop() {
  static unsigned long last = 0;
  static bool on = false;
  unsigned long now = millis();
  if (now - last >= 500) {
    last = now;
    on = !on;
    digitalWrite(LED_BUILTIN, on ? HIGH : LOW);
    Serial.println(on ? "LED=1" : "LED=0");
  }
}

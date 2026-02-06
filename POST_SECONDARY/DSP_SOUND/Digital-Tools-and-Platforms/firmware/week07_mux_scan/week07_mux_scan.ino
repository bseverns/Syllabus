// Week 07 — Multiplexer scanning (conceptual scaffold)
// This sketch assumes a 3-bit select mux (like CD4051) feeding A0.
// You MUST adapt pin numbers to your wiring/chip.

// Select pins
const int S0 = 2;
const int S1 = 3;
const int S2 = 4;

const int SIG = A0;

void setChannel(int ch) {
  digitalWrite(S0, (ch & 1) ? HIGH : LOW);
  digitalWrite(S1, (ch & 2) ? HIGH : LOW);
  digitalWrite(S2, (ch & 4) ? HIGH : LOW);
}

void setup() {
  pinMode(S0, OUTPUT); pinMode(S1, OUTPUT); pinMode(S2, OUTPUT);
  Serial.begin(115200);
  delay(500);
}

void loop() {
  unsigned long now = millis();
  for (int ch = 0; ch < 8; ch++) {
    setChannel(ch);
    delayMicroseconds(10); // settling time (tune!)
    int raw = analogRead(SIG);
    Serial.print(now);
    Serial.print(",");
    Serial.print(ch);
    Serial.print(",");
    Serial.println(raw);
  }
  delay(10);
}

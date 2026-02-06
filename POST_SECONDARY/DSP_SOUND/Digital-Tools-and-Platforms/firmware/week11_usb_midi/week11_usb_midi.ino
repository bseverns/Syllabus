// Week 11 — USB MIDI (Teensy recommended)
// If you're on Arduino Uno, skip or treat as pseudo-code.
// Teensy: include usbMIDI and send CC.

const int POT = A0;
int lastCC = -1;

void setup() {
  Serial.begin(115200);
  delay(500);
}

void loop() {
  int raw = analogRead(POT);
  int cc = map(raw, 0, 1023, 0, 127);
  cc = constrain(cc, 0, 127);

  if (abs(cc - lastCC) >= 1) {
    lastCC = cc;

    // For Teensy:
    // usbMIDI.sendControlChange(1, cc, 1); // CC#1 on channel 1

    Serial.print("CC1="); Serial.println(cc);
  }

  // For Teensy: handle incoming
  // while (usbMIDI.read()) {}

  delay(5);
}

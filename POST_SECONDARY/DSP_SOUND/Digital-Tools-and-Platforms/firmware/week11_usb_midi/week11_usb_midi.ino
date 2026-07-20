// Week 11: pot on A0 sends CC 1 when its 0..127 value changes.
// Teensy: select a USB Type that includes MIDI before compiling.
// Other boards: the required fallback prints the intended MIDI message to Serial.
const uint8_t CONTROL_PIN = A0;
const uint8_t CC_NUMBER = 1;
const uint8_t MIDI_CHANNEL = 1;
int lastValue = -1;

void setup() {
  Serial.begin(115200);
}

void loop() {
  const int value = map(analogRead(CONTROL_PIN), 0, 1023, 0, 127);
  if (abs(value - lastValue) >= 2) {
    lastValue = value;
#if defined(TEENSYDUINO)
    usbMIDI.sendControlChange(CC_NUMBER, value, MIDI_CHANNEL);
#endif
    Serial.print("MIDI,CC,");
    Serial.print(CC_NUMBER);
    Serial.print(',');
    Serial.print(value);
    Serial.print(',');
    Serial.println(MIDI_CHANNEL);
  }
#if defined(TEENSYDUINO)
  while (usbMIDI.read()) { }
#endif
  delay(5);
}

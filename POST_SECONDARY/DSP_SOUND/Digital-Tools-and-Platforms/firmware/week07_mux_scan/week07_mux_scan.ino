// Week 07: CD4051-style mux scan. Confirm the exact chip pinout and voltage first.
const uint8_t SELECT_PINS[3] = {2, 3, 4};
const uint8_t SIGNAL_PIN = A0;
const uint8_t CHANNELS = 8;
const unsigned int SETTLE_US = 200;
const unsigned long FRAME_MS = 20;
unsigned long lastFrame = 0;

void selectChannel(uint8_t channel) {
  for (uint8_t bit = 0; bit < 3; bit++) {
    digitalWrite(SELECT_PINS[bit], (channel >> bit) & 0x01);
  }
}

void setup() {
  for (uint8_t i = 0; i < 3; i++) pinMode(SELECT_PINS[i], OUTPUT);
  Serial.begin(115200);
}

void loop() {
  const unsigned long now = millis();
  if (now - lastFrame < FRAME_MS) return;
  lastFrame = now;
  for (uint8_t channel = 0; channel < CHANNELS; channel++) {
    selectChannel(channel);
    delayMicroseconds(SETTLE_US);
    const int value = analogRead(SIGNAL_PIN);
    Serial.print(now);
    Serial.print(',');
    Serial.print(channel);
    Serial.print(',');
    Serial.println(value);
  }
}

// Week 09 — State machines + modes
// One button cycles modes; LEDs indicate current mode.
// Wiring: button to D2 and GND with INPUT_PULLUP.

const int BTN = 2;
const int LED1 = 5;
const int LED2 = 6;
const int LED3 = 9;

enum Mode { MODE_A=0, MODE_B=1, MODE_C=2 };
Mode mode = MODE_A;

unsigned long lastChange = 0;
const unsigned long DEBOUNCE_MS = 30;

void setup() {
  pinMode(BTN, INPUT_PULLUP);
  pinMode(LED1, OUTPUT); pinMode(LED2, OUTPUT); pinMode(LED3, OUTPUT);
  Serial.begin(115200);
  delay(500);
}

void showMode() {
  digitalWrite(LED1, mode == MODE_A);
  digitalWrite(LED2, mode == MODE_B);
  digitalWrite(LED3, mode == MODE_C);
}

void loop() {
  unsigned long now = millis();
  static int last = HIGH;
  int raw = digitalRead(BTN);

  if (raw != last) { last = raw; lastChange = now; }

  // Detect press (stable LOW)
  if (raw == LOW && (now - lastChange) > DEBOUNCE_MS) {
    // Wait for release to avoid repeat
    while (digitalRead(BTN) == LOW) { delay(1); }
    mode = (Mode)(((int)mode + 1) % 3);
    showMode();
    Serial.print(now); Serial.print(",MODE=");
    Serial.println((int)mode);
  }
}

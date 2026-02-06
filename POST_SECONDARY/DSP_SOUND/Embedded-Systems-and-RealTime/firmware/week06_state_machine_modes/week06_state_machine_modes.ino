// Week 06 — State machine with explicit transitions
// Button cycles modes; knob meaning changes per mode.
//
// Output:
// MODE,<n>
// CC,<cc>,<val>,<ch>

const int BTN = 2;
const int POT = A0;

enum Mode { MODE_A=0, MODE_B=1, MODE_C=2 };
Mode mode = MODE_A;

const int CH = 1;

unsigned long lastChange = 0;
const unsigned long DEBOUNCE_MS = 30;

int lastVal = -1;

int ccForMode(Mode m) {
  if (m == MODE_A) return 1;
  if (m == MODE_B) return 11;
  return 21;
}

void setup() {
  pinMode(BTN, INPUT_PULLUP);
  Serial.begin(115200);
  delay(500);
  Serial.print("MODE,"); Serial.println((int)mode);
}

void loop() {
  unsigned long now = millis();

  // mode button (basic debounce)
  static int last = HIGH;
  int r = digitalRead(BTN);
  if (r != last) { last = r; lastChange = now; }
  if (r == LOW && (now - lastChange) > DEBOUNCE_MS) {
    while (digitalRead(BTN) == LOW) delay(1);
    mode = (Mode)(((int)mode + 1) % 3);
    Serial.print("MODE,"); Serial.println((int)mode);
  }

  // knob + mapping
  int val = constrain(map(analogRead(POT), 0, 1023, 0, 127), 0, 127);
  if (lastVal < 0 || abs(val - lastVal) >= 2) {
    lastVal = val;
    int cc = ccForMode(mode);
    Serial.print("CC,"); Serial.print(cc); Serial.print(","); Serial.print(val); Serial.print(","); Serial.println(CH);
  }

  delay(2);
}

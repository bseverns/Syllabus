// Week 05 — Event queue + priority drop policy
// Demonstrates a ring buffer event queue with "drop knob updates first".
//
// Events:
// 0 = button edge (high priority)
// 1 = knob update (low priority)

struct Event {
  uint8_t type;
  uint8_t id;
  int16_t value;
};

const int QN = 32;
Event q[QN];
volatile int head = 0, tail = 0;

bool qFull()  { return ((head + 1) % QN) == tail; }
bool qEmpty() { return head == tail; }

bool push(Event e) {
  if (!qFull()) {
    q[head] = e;
    head = (head + 1) % QN;
    return true;
  }

  // If full and event is high priority: try to drop a low priority item.
  if (e.type == 0) {
    // naive policy: drop the oldest item if it's low priority; otherwise fail.
    if (q[tail].type == 1) {
      tail = (tail + 1) % QN;
      q[head] = e;
      head = (head + 1) % QN;
      return true;
    }
  }
  return false;
}

bool pop(Event &e) {
  if (qEmpty()) return false;
  e = q[tail];
  tail = (tail + 1) % QN;
  return true;
}

void setup() {
  Serial.begin(115200);
  delay(500);
  Serial.println("READY");
}

void loop() {
  // simulate events
  static unsigned long lastGen = 0;
  static int knob = 0;
  unsigned long now = millis();

  if (now - lastGen >= 1) { // 1000 Hz knob spam
    lastGen = now;
    knob = (knob + 1) % 128;
    push({1, 0, (int16_t)knob});
  }
  if (now % 250 == 0) { // button edge occasionally
    push({0, 0, 1});
  }

  // process a few events
  for (int i = 0; i < 4; i++) {
    Event e;
    if (!pop(e)) break;
    Serial.print("EVT,"); Serial.print(e.type); Serial.print(","); Serial.print(e.id); Serial.print(","); Serial.println(e.value);
  }
}

// Week 02 — Cooperative scheduler (no delay)
// A tiny task scheduler with fixed cadences.
//
// Tasks:
// - sample buttons @ 1000 Hz
// - sample knobs   @ 200 Hz
// - send protocol  @ 100 Hz
// - render LEDs    @ 60 Hz
//
// Replace task bodies with your real IO.

struct Task {
  unsigned long interval_us;
  unsigned long next_us;
  void (*fn)();
};

void taskButtons() { /* TODO: debounce, edge detect, push events */ }
void taskKnobs()   { /* TODO: analog reads, filtering, push events */ }
void taskProtocol(){ /* TODO: pop events, send MIDI/Serial */ }
void taskLEDs()    { /* TODO: render state */ }

Task tasks[] = {
  {1000, 0, taskButtons},
  {5000, 0, taskKnobs},
  {10000,0, taskProtocol},
  {16666,0, taskLEDs},
};

void setup() {
  Serial.begin(115200);
  delay(500);
  unsigned long now = micros();
  for (auto &t : tasks) t.next_us = now + t.interval_us;
}

void loop() {
  unsigned long now = micros();
  for (auto &t : tasks) {
    // Signed compare to handle wraparound
    if ((long)(now - t.next_us) >= 0) {
      t.next_us += t.interval_us;
      t.fn();
    }
  }
}

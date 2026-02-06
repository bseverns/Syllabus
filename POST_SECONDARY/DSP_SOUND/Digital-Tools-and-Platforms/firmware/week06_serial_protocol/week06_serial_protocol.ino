// Week 06 — Serial protocol as a contract
// Commands (newline terminated):
//   SET_BPM 120
//   LED 1
//   LED 0
// Outputs:
//   OK <cmd>
//   t_ms,tick

const int LED_PIN = LED_BUILTIN;
int bpm = 120;

unsigned long intervalMs() { return (unsigned long)(60000.0 / (float)bpm); }

String line;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
  delay(500);
  Serial.println("READY");
}

void handleLine(const String& s) {
  if (s.startsWith("SET_BPM ")) {
    bpm = s.substring(8).toInt();
    Serial.println("OK SET_BPM");
  } else if (s == "LED 1") {
    digitalWrite(LED_PIN, HIGH);
    Serial.println("OK LED");
  } else if (s == "LED 0") {
    digitalWrite(LED_PIN, LOW);
    Serial.println("OK LED");
  } else {
    Serial.println("ERR UNKNOWN");
  }
}

void loop() {
  // Read commands
  while (Serial.available()) {
    char c = (char)Serial.read();
    if (c == '\n' || c == '\r') {
      if (line.length() > 0) {
        handleLine(line);
        line = "";
      }
    } else {
      line += c;
    }
  }

  // Metronome tick
  static unsigned long lastTick = 0;
  unsigned long now = millis();
  if (now - lastTick >= intervalMs()) {
    lastTick += intervalMs();
    Serial.print(now);
    Serial.println(",1");
  }
}

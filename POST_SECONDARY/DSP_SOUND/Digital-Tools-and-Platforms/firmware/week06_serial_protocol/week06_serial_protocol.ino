// Week 06: newline-framed ASCII protocol.
// Commands: PING | GET | LED 0 | LED 1 | RATE <20..2000>
const uint8_t LED_PIN = LED_BUILTIN;
const uint8_t SENSOR_PIN = A0;
char lineBuffer[32];
uint8_t lineLength = 0;
bool ledState = false;
unsigned long reportRateMs = 250;
unsigned long lastReport = 0;

void sendData() {
  Serial.print("DATA,");
  Serial.print(millis());
  Serial.print(',');
  Serial.print(analogRead(SENSOR_PIN));
  Serial.print(',');
  Serial.println(ledState ? 1 : 0);
}

void handleCommand(char *line) {
  if (strcmp(line, "PING") == 0) {
    Serial.println("ACK,PONG");
  } else if (strcmp(line, "GET") == 0) {
    sendData();
  } else if (strncmp(line, "LED ", 4) == 0 && (line[4] == '0' || line[4] == '1') && line[5] == '\0') {
    ledState = line[4] == '1';
    digitalWrite(LED_PIN, ledState);
    Serial.println(ledState ? "ACK,LED,1" : "ACK,LED,0");
  } else if (strncmp(line, "RATE ", 5) == 0) {
    const long requested = atol(line + 5);
    if (requested >= 20 && requested <= 2000) {
      reportRateMs = (unsigned long)requested;
      Serial.print("ACK,RATE,");
      Serial.println(reportRateMs);
    } else {
      Serial.println("ERR,RATE_RANGE");
    }
  } else {
    Serial.println("ERR,UNKNOWN_COMMAND");
  }
}

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
  Serial.println("ACK,READY,1");
}

void loop() {
  while (Serial.available() > 0) {
    const char incoming = (char)Serial.read();
    if (incoming == '\n' || incoming == '\r') {
      if (lineLength > 0) {
        lineBuffer[lineLength] = '\0';
        handleCommand(lineBuffer);
        lineLength = 0;
      }
    } else if (lineLength < sizeof(lineBuffer) - 1) {
      lineBuffer[lineLength++] = incoming;
    } else {
      lineLength = 0;
      Serial.println("ERR,LINE_TOO_LONG");
    }
  }

  const unsigned long now = millis();
  if (now - lastReport >= reportRateMs) {
    lastReport = now;
    sendData();
  }
}

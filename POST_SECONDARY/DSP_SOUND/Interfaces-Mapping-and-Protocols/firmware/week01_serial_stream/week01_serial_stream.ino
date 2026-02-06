// Week 01 — Serial stream (CSV-ish): t_ms,rawPot,btn
const int POT=A0, BTN=2;
void setup(){ pinMode(BTN, INPUT_PULLUP); Serial.begin(115200); delay(500); }
void loop(){
  static unsigned long last=0; unsigned long now=millis();
  if(now-last<10) return; last=now; // 100 Hz
  int raw=analogRead(POT);
  int btn=(digitalRead(BTN)==LOW)?1:0;
  Serial.print(now); Serial.print(","); Serial.print(raw); Serial.print(","); Serial.println(btn);
}

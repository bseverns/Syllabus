// Week 05 — Rate limiting + change threshold
const int POT=A0, CH=1, CC_NUM=1;
const unsigned long MIN_MS=10; const int MIN_CHANGE=2;
unsigned long lastSend=0; int lastVal=-1;
void setup(){ Serial.begin(115200); delay(500); }
void loop(){
  unsigned long now=millis();
  int val=constrain(map(analogRead(POT),0,1023,0,127),0,127);
  if(now-lastSend<MIN_MS) return;
  if(lastVal>=0 && abs(val-lastVal)<MIN_CHANGE) return;
  lastSend=now; lastVal=val;
  Serial.print("CC,"); Serial.print(CC_NUM); Serial.print(","); Serial.print(val); Serial.print(","); Serial.println(CH);
}

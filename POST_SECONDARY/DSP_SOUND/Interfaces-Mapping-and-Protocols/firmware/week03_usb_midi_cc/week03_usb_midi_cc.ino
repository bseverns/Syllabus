// Week 03 — USB MIDI CC (Teensy) or Serial fallback: CC,cc,val,ch
const int POT=A0; const int CH=1, CC_NUM=1; int lastVal=-1;
void setup(){ Serial.begin(115200); delay(500); }
void loop(){
  int val=constrain(map(analogRead(POT),0,1023,0,127),0,127);
  if(lastVal>=0 && abs(val-lastVal)<1) { delay(5); return; }
  lastVal=val;
  // usbMIDI.sendControlChange(CC_NUM, val, CH);
  Serial.print("CC,"); Serial.print(CC_NUM); Serial.print(","); Serial.print(val); Serial.print(","); Serial.println(CH);
  delay(5);
}

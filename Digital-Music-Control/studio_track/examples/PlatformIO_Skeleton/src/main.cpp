#include <Arduino.h>
#include "MIDISender.h"
const int POT=A0; uint8_t ch=0, cc=1;
void setup(){ Serial.begin(115200); pinMode(POT,INPUT); }
void loop(){
  int raw = analogRead(POT);
  uint8_t v = map(raw, 0, 1023, 0, 127);
  MIDISender::cc(ch, cc, v);
  delay(8);
}

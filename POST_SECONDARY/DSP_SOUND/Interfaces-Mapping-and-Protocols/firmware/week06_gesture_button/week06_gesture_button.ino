// Week 06 — Button gestures: SINGLE/DOUBLE/LONG
const int BTN=2;
const unsigned long DEBOUNCE=25, DOUBLE_MS=350, LONG_MS=700;
int raw=HIGH, stable=HIGH, lastRaw=HIGH;
unsigned long lastChange=0, pressTime=0, lastRelease=0;
bool waitingSecond=false;

void setup(){ pinMode(BTN, INPUT_PULLUP); Serial.begin(115200); delay(500); }

void loop(){
  unsigned long now=millis();
  raw=digitalRead(BTN);
  if(raw!=lastRaw){ lastRaw=raw; lastChange=now; }
  if((now-lastChange)>DEBOUNCE && stable!=raw){
    stable=raw;
    if(stable==LOW){ pressTime=now; Serial.println("EVT:PRESS"); }
    else{
      unsigned long held=now-pressTime;
      Serial.println("EVT:RELEASE");
      if(held>=LONG_MS){ Serial.println("EVT:LONG"); waitingSecond=false; }
      else{
        if(waitingSecond && (now-lastRelease)<=DOUBLE_MS){ Serial.println("EVT:DOUBLE"); waitingSecond=false; }
        else{ waitingSecond=true; lastRelease=now; }
      }
    }
  }
  if(waitingSecond && (now-lastRelease)>DOUBLE_MS){ Serial.println("EVT:SINGLE"); waitingSecond=false; }
}

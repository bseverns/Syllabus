const int LEDS[8]={2,3,4,5,6,7,8,9};
void setup(){ for(int i=0;i<8;i++) pinMode(LEDS[i],OUTPUT); }
void loop(){ for(int i=0;i<8;i++){ digitalWrite(LEDS[i],HIGH); delay(80); digitalWrite(LEDS[i],LOW);} }
// Week 07 — LED feedback language: mode A/B/C
const int BTN=2, LED1=5, LED2=6, LED3=9;
enum Mode{A=0,B=1,C=2}; Mode mode=A;
unsigned long lastChange=0; const unsigned long DEBOUNCE=30;

void showMode(){ digitalWrite(LED1, mode==A); digitalWrite(LED2, mode==B); digitalWrite(LED3, mode==C); }

void setup(){
  pinMode(BTN, INPUT_PULLUP);
  pinMode(LED1, OUTPUT); pinMode(LED2, OUTPUT); pinMode(LED3, OUTPUT);
  Serial.begin(115200); delay(500); showMode();
}

void loop(){
  unsigned long now=millis();
  static int last=HIGH;
  int r=digitalRead(BTN);
  if(r!=last){ last=r; lastChange=now; }
  if(r==LOW && (now-lastChange)>DEBOUNCE){
    while(digitalRead(BTN)==LOW) delay(1);
    mode=(Mode)(((int)mode+1)%3); showMode();
    Serial.print("MODE="); Serial.println((int)mode);
  }
}

// Encoder_Input — simple quadrature read
const int PIN_A=2, PIN_B=3; volatile long enc=0; int last=0;
void setup(){ pinMode(PIN_A,INPUT_PULLUP); pinMode(PIN_B,INPUT_PULLUP); Serial.begin(115200); last=(digitalRead(PIN_A)<<1)|digitalRead(PIN_B); }
void loop(){ int cur=(digitalRead(PIN_A)<<1)|digitalRead(PIN_B); if(cur!=last){ if((last==0&&cur==1)||(last==1&&cur==3)||(last==3&&cur==2)||(last==2&&cur==0)) enc++; else enc--; last=cur; Serial.println(enc);} }
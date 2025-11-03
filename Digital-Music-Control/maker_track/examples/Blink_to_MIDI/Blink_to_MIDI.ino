/* Blink_to_MIDI — Arduino Uno (Serial-as-MIDI via host bridge) */
const int LED=13; byte cc=1, ch=0; int v=0, dv=3;
void setup(){ pinMode(LED,OUTPUT); Serial.begin(115200); }
void sendCC(byte cc, byte val, byte ch){ Serial.write(0xB0 | (ch & 0x0F)); Serial.write(cc & 0x7F); Serial.write(val & 0x7F); }
void loop(){ digitalWrite(LED, HIGH); delay(50); digitalWrite(LED, LOW); delay(50); sendCC(cc, v, ch); v+=dv; if(v>=127||v<=0) dv=-dv; }
byte ch=0, cc=74; int v=0, dv=2;
void setup(){ Serial.begin(115200); }
void loop(){ Serial.write(0xB0 | (ch & 0x0F)); Serial.write(cc & 0x7F); Serial.write(v & 0x7F);
  v+=dv; if(v>=127||v<=0) dv=-dv; delay(10); }
// Week 10 — Minimal config protocol: INFO and CFG:<json>
int midiChannel=1; String line;

void setup(){ Serial.begin(115200); delay(500); Serial.println("READY"); }

void sendInfo(){
  Serial.print("INFO:FW=1.0;CH="); Serial.print(midiChannel);
  Serial.println(";CAPS=KNOBS:8,BTNS:4,LEDS:8");
}

int parseMidiChannel(const String& json){
  int idx=json.indexOf("\"midi_channel\""); if(idx<0) return -1;
  int colon=json.indexOf(":", idx); if(colon<0) return -1;
  int i=colon+1; while(i<(int)json.length() && json[i]==' ') i++;
  String num=""; while(i<(int)json.length() && isDigit(json[i])){ num+=json[i]; i++; }
  return num.length()?num.toInt():-1;
}

void handleLine(const String& s){
  if(s=="INFO"){ sendInfo(); return; }
  if(s.startsWith("CFG:")){
    int ch=parseMidiChannel(s.substring(4));
    if(ch>=1 && ch<=16){ midiChannel=ch; Serial.println("OK"); }
    else Serial.println("ERR");
    return;
  }
  Serial.println("ERR");
}

void loop(){
  while(Serial.available()){
    char c=(char)Serial.read();
    if(c=='\n'||c=='\r'){ if(line.length()){ handleLine(line); line=""; } }
    else line+=c;
  }
}

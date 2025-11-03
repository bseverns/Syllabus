import processing.serial.*;
Serial port; String line="";
void setup(){ size(800,400); println(Serial.list()); port=new Serial(this, Serial.list()[0],115200); port.bufferUntil('\n'); textFont(createFont("Monospaced",14)); }
void draw(){ background(0); fill(255); text("Serial MIDI bytes (hex):", 10,20); text(line, 10, 50); }
void serialEvent(Serial s){ String raw=s.readStringUntil('\n'); if(raw!=null){ raw=trim(raw); line=raw; } }
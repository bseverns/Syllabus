import processing.serial.*; import org.json.*; Serial port; float v=0;
void setup(){ size(600,400); println(Serial.list()); port=new Serial(this, Serial.list()[0],115200); port.bufferUntil('\n'); }
void draw(){ background(0); fill(255); text("val: "+v, 20, 20); circle(width/2, height/2, 50+v); }
void serialEvent(Serial s){ String line=trim(s.readStringUntil('\n')); if(line!=null&&line.startsWith("{")){ try{ JSONObject j=new JSONObject(line); v=(float)j.getDouble("v"); }catch(Exception e){} } }
#include <EEPROM.h>
struct Settings{ byte cc1; byte cc2; byte scene; } s;
void save(){ EEPROM.put(0, s); }
void load(){ EEPROM.get(0, s); if(s.cc1>127){ s.cc1=1; s.cc2=74; s.scene=0; } }
void setup(){ Serial.begin(115200); load(); }
void loop(){ /* modify s then save() on change */ }
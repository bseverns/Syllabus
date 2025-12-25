enum Scene { Idle, Breathe, Pulse, Spin };
Scene sc=Idle; unsigned long t0=0;
void setup(){ t0=millis(); }
void loop(){ unsigned long now=millis(); switch(sc){ case Idle: break; case Breathe: break; case Pulse: break; case Spin: break; } }
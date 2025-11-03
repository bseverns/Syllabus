/*
  Vase-mode form: continuous single-wall using rotate_extrude.
*/
h = 120;
w = 70;
wav = 6;
wav_amp = 6;

module profile(){
    polygon([
        for(i=[0:1:100]) let(t=i/100) [
          w/2 + wav_amp*sin(360*wav*t),
          h*t
        ]
    ]);
}

rotate_extrude(angle=360, $fn=180) translate([w/2,0,0]) profile();

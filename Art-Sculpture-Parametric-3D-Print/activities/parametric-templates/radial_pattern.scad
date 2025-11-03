/*
  Radial pattern: parametric petals with variable curvature & count.
*/
petals = 18;
inner_r = 8;
outer_r = 35;
thickness = 2;
wave_amp = 3;
wave_freq = 4;

module petal(angle){
    rotate([0,0,angle])
    linear_extrude(height=thickness)
    polygon([
        for (i=[0:1:60]) let(
            t = i/60,
            r = inner_r + (outer_r-inner_r)*t + wave_amp*sin(360*wave_freq*t)
        ) [ r*cos(360*t), r*sin(360*t) ]
    ]);
}

for (i=[0:petals-1]) petal(360/petals*i);

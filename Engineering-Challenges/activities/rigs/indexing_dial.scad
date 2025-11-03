r = 40; th = 3; $fn=180;
difference(){ cylinder(h=th, r=r); translate([0,0,-1]) cylinder(h=th+2, r=3, $fn=60); }
for(i=[0:11]) rotate([0,0,i*30]) translate([r-2, -1, th]) cube([2, 2, 2]);

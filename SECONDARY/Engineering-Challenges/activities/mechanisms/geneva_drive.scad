/*
  Geneva mechanism (4-slot wheel + drive pin; teaching scale).
*/
slots = 4;
wheel_r = 30;
pin_r = 2.5;
th = 5;
$fn=180;

module geneva_wheel(){
  difference(){
    cylinder(h=th, r=wheel_r);
    for(i=[0:slots-1]) rotate([0,0,i*(360/slots)]) cube([wheel_r*1.2, pin_r*2.2, th+1], center=true);
    translate([0,0,-1]) cylinder(h=th+2, r=3, $fn=60);
  }
}

module drive_disk(){
  difference(){
    cylinder(h=th, r=wheel_r/2);
    translate([0,0,-1]) cylinder(h=th+2, r=3, $fn=60);
  }
  translate([wheel_r/2 - pin_r*1.2,0,0]) cylinder(h=th, r=pin_r, $fn=60);
}

geneva_wheel();
translate([75,0,0]) drive_disk();

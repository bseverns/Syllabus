/*
  Rack & pinion teaching model (rack is a flat rail; pinion is a gear blank).
*/
module_mm = 2.0;
teeth_pinion = 16;
thickness = 6;
bore = 5;
rack_teeth = 40;
$fn=120;

module pinion(){
  difference(){
    cylinder(h=thickness, r=(module_mm*teeth_pinion/2)+module_mm, $fn=180);
    translate([0,0,-1]) cylinder(h=thickness+2, r=bore/2, $fn=80);
  }
}

module rack(){
  linear_extrude(height=thickness)
    square([module_mm*rack_teeth*1.25, 12], center=false);
}

translate([0,0,0]) pinion();
translate([-(module_mm*rack_teeth*1.25)/2, 20, 0]) rack();

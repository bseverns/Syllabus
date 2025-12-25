/* Simple temperature tower with labels (manually assign temps per segment) */
module segment(h, label){
  cube([20,20,h], center=false);
  translate([2,2,h-1]) linear_extrude(1) text(label, size=4);
}
translate([0,0,0]) segment(10,"210");
translate([0,0,10]) segment(10,"205");
translate([0,0,20]) segment(10,"200");
translate([0,0,30]) segment(10,"195");
translate([0,0,40]) segment(10,"190");

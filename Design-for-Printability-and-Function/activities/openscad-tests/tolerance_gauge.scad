/*
  Tolerance gauge: board with pegs & matching holes at varying clearance (mm).
  Positive values = clearance; negative = interference.
*/
clearances = [-0.20, -0.10, 0.00, 0.10, 0.20, 0.30];
peg_d = 6;
th   = 3;
hole_d_base = peg_d;

module peg(d){
    cylinder(h=10, r=d/2, $fn=48);
}

module hole(d){
    translate([0,0,0]) cylinder(h=10, r=d/2, $fn=48);
}

spacing = 16;
board_w = spacing*(len(clearances)-1) + 20;
board_d = 30;

difference(){
    cube([board_w, board_d, th]);
    // holes row
    for (i=[0:len(clearances)-1]){
        d = hole_d_base + clearances[i];
        translate([10 + i*spacing, 10, 0]) hole(d);
    }
}

for (i=[0:len(clearances)-1]){
    d = peg_d;
    translate([10 + i*spacing, 22, th]) peg(d);
}

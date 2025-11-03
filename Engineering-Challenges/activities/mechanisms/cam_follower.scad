/*
  Cam & follower: heart/snail cams (approximate) + simple follower lever.
*/
profile = "heart"; // ["snail","heart"]
thickness = 6;
r_base = 20;
ecc = 6; // eccentricity
$fn=180;

module cam(){
  if (profile == "snail"){
    linear_extrude(height=thickness)
      polygon([ for(a=[0:360]) [ (r_base + a*ecc/360)*cos(a), (r_base + a*ecc/360)*sin(a) ] ]);
  } else {
    linear_extrude(height=thickness)
      polygon([ for(a=[0:360]) let(rad=radians(a)) [ (r_base*(1 - sin(rad)))*cos(rad), (r_base*(1 - sin(rad)))*sin(rad) ] ]);
  }
}

module follower(){ linear_extrude(height=thickness) square([50,6]); }

cam();
translate([60,0,0]) follower();

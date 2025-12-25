/*
  p5.js SVG tiling generator — export SVG motifs to extrude in OpenSCAD.
  Use p5.js with p5.svg.js library in the browser.
*/
function setup(){
  createCanvas(800,800, SVG);
  noFill(); strokeWeight(2);
  let cols = 10, rows = 10, g = width/cols;
  for(let y=0;y<rows;y++){
    for(let x=0;x<cols;x++){
      push();
      translate(x*g+g/2, y*g+g/2);
      let r = 0.3*g + 0.2*g * noise(x*0.1, y*0.1);
      polygon(0,0,r,6 + int(noise(x,y)*6));
      pop();
    }
  }
  save("pattern.svg");
  noLoop();
}

function polygon(x, y, r, n){
  beginShape();
  for(let a=0;a<TWO_PI;a+=TWO_PI/n){
    vertex(x + cos(a)*r, y + sin(a)*r);
  }
  endShape(CLOSE);
}

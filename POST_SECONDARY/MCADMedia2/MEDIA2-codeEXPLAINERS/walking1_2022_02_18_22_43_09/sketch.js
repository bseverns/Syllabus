let img1;
let img2;
let p1;

function preload() {
  img1 = loadImage("terrycrews.gif");
  img2 = loadImage("stapleSCREEN.png");
  p1 = createP("This is some text, longer text may be a bit clunky");
}

function setup() {
  createCanvas(800, 800);
  //setting up my text to read about the images
  p1.style('font-size', '20px');
  p1.position(350, 350);
}

function draw() {
  background(220);
  image(img1, 0, 0);
  image(img2, 400, 400);
}
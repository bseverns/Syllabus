function setup() {
	createCanvas(400,400);
}

function draw() {
	background(255);

	animateDM(mouseX, mouseY); //us an entirely different function to build the thing that we are going to "draw", carry two variables into doing that function

}









function animateDM(x, y) { //naming those variables we are taking into this function

	push(); //explanation below
	translate(x, y); //setting what our new (0,0) is which was set in our draw function as our mouseX &&mouseY see the Reference

	if ((frameCount / 15) % 2 < 1) { //a programatic way to check to see if the frame count out of 60 is divisible by 2
		drawDM1(); //do a function
	} else {
		drawDM2(); //do another function
	}
	pop(); //reset - explanation below
}

function drawDM1() { //sub-function #1
	noStroke();
	fill(250, 200, 0);
	rect(3, 0, 44, 45, 8);

	fill(255);
	ellipse(15, 15, 12, 12);
	ellipse(35, 15, 12, 12);
	fill(0, 120, 250);
	ellipse(15, 15, 8, 8);
	ellipse(35, 15, 6, 6);
	fill(28);
	ellipse(15, 15, 4, 4);
	ellipse(35, 15, 3, 3);

	fill(64);
	rect(7, 40 - 1, 13, 10, 5);
	rect(30, 40 + 1, 13, 10, 5);
	rect(3, 45 - 1, 17, 5, 5);
	rect(30, 45 + 1, 17, 5, 5);

	fill(64);
	ellipse(8, 32 - 1, 15, 10);
	ellipse(42, 32 + 1, 15, 10);

	stroke(200, 20, 20);
	strokeWeight(2);
	fill(100, 0, 15);
	quad(18, 25, 32, 28, 30, 35, 20, 30);


	fill(60, 100);
	strokeWeight(2);
	stroke(100, 60, 0);
	line(3, 10, 47, 10);
	rect(27, 10, 15, 10);
	rect(8, 10, 15, 10);
}

function drawDM2() { //sub-function #2
	noStroke();
	fill(250, 200, 0);
	rect(3, 0, 44, 45, 8);

	fill(255);
	ellipse(15, 15, 12, 12);
	ellipse(35, 15, 12, 12);
	fill(0, 120, 250);
	ellipse(15, 15, 8, 8);
	ellipse(35, 15, 6, 6);
	fill(28);
	ellipse(15, 15, 4, 4);
	ellipse(35, 15, 3, 3);

	fill(64);
	rect(7, 40 + 1, 13, 10, 5);
	rect(30, 40 - 1, 13, 10, 5);
	rect(3, 45 + 1, 17, 5, 5);
	rect(30, 45 - 1, 17, 5, 5);

	fill(64);
	ellipse(8, 32 + 1, 15, 10);
	ellipse(42, 32 - 1, 15, 10);

	stroke(200, 20, 20);
	strokeWeight(2);
	fill(100, 0, 15);
	quad(18, 25, 32, 28, 30, 35, 20, 30);


	fill(60, 100);
	strokeWeight(2);
	stroke(100, 60, 0);
	line(3, 10, 47, 10);
	rect(27, 10, 15, 10);
	rect(8, 10, 15, 10);
}

let snakeX = [];
let snakeY = [];

function setup() {
	createCanvas(400, 400);
}

function draw() {
	background(128);

/*The push(##) method adds the value ## to the end of an array.  In the example to the right, the arrays for snakeX and snakeY initially have no values in them.*/
	snakeX.push(mouseX);
	snakeY.push(mouseY);

/*
To remove a value from an array, use the splice(loc, num) method.  This goes to the index value specified by loc and removes num values from the array, shortening it.

The following if() statements checks to see if the snakeX.length is longer than 50 values and removes the oldest one (the first one) if it is.
*/

	if(snakeX.length>50){
		snakeX.splice(0,1);
		snakeY.splice(0,1);
	}

	for(let i = 0; i<snakeX.length; i= i+1){
		noStroke();
		fill(100, 0, 2*i, 2*i);
		ellipse(snakeX[i], snakeY[i], i, i); //try changing the graphic primitive-type to get other shapes to appear
	}

}

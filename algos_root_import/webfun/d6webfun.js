// Math Library - floor method rounds down
// Ceiling would round up. Not like math class rounding


// can we predict what random might return??
/*
var floor = Math.floor(1.8);
var ceiling = Math.ceil( Math.PI ); //PI is literally 3.141592654
var random = Math.random(); // always between 0-1, up to 0.99 repeating, doesn't include 1

console.log(floor);
console.log(ceiling);
console.log(random);
*/

// RETURN A VALUE BETWEEN 1-6

function d6() {
     var roll = Math.random(); // this gives us 0-0.99
     roll = roll*6
     roll = Math.ceil(roll)
return roll;
}

var playerRoll = d6();
console.log("The player rolled: " + playerRoll);

// WRITE A FUNCTION THAT WILL RANDOMLY RETURN AN ANSWER FROM THE ARRAY BELOW TO ANSWER ALL OF OUR QUESTIONS RANDOMLY

var lifesAnswers = [
     "It is certain.",
     "It is decidedly so.",
     "Without a doubt.",
     "Yes – definitely.",
     "You may rely on it.",
     "As I see it, yes.",
     "Most likely.",
     "Outlook good.",
     "Yes.",
     "Signs point to yes.",
     "Reply hazy, try again.",
     "Ask again later.",
     "Better not tell you now.",
     "Cannot predict now.",
     "Concentrate and ask again.",
     "Don't count on it.",
     "My reply is no.",
     "My sources say no.",
     "Outlook not so good.",
     "Very doubtful."
];

// console.log(lifesAnswers.length) - array length is 20
var random = (Math.random()) * (lifesAnswers.length);

// console.log(random)
var value = Math.floor(random);

// arrays index at 0, so the 20th value = 19th index
// console.log(lifesAnswers[20]) // showing that there's no 20th value, so we should do Math.floor instead of Math.ceil
// arrays are always n-1 where n is length, so randomizing within an array should almost always be floor in that sense!!!

// console.log(value)
var answer = lifesAnswers[value];
console.log(answer);

//prompt() function - try it out!
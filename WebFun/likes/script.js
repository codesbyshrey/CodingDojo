
console.log("I hope this has loaded");

// Rather than trying to change and keep track of multiple variable names and different numbers every time, makes a lot more sense to have a preset array of values that spits out numbers necessary to read

var numLikes = [9, 12, 10];
console.log(numLikes);

var spanText = [
     document.querySelector("#neil"),
     document.querySelector("#nichole"),
     document.querySelector("#jim")
];
console.log(spanText);

function increase(id){
     //alert("you clicked a like button");

     numLikes[id]++; 
     console.log(numLikes);
     spanText[id].innerHTML = numLikes[id] + " like(s)";

     // We use innerHTML over innerText in this case because I'm willing to let the function print out the string regarding the likes, rather than keeping it outside of the span and having to micromanage all of the element names. On the first pass around I tried to do it like DojoWeather where it selects just the numbers and does the conversion, but adequately being able to find those areas and specifically just change number is more difficult compared to keeping it in one streamlined section of code here
}

// increase likes by 1 for each respective person and I have to find the parent element of the like button which is div.mininav and then I need to go back in to edit the text within span.neilnum, span.nicholenum, and span.jimnum

// attempt number one - my console log is appropraitely increasing the array values and reading it out. My text inside is not changing though
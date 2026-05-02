

var countPositives = 0;
var numbers = [3, 4, -2, 7, 16, -8, 0];

// your code here! 
for(var i=0; i<numbers.length; i++) {
     // console.log(numbers[i]) - created to double check that I could read and print the array
     if (numbers[i] >=0) {
          countPositives++
          // console.log(countPositives) making sure it would increase the value correctly
     }
}

console.log("there are " + countPositives + " positive values");

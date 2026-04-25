/* var fruit1= "apples";
var fruit2= "oranges";

// var temp = fruit1;
// fruit1 = fruit2; 
// fruit2 = temp; 
fruit2 = fruit1
console.log( fruit2 = "an" + fruit1)

var start = 0;
var end = 12;

while (start < end ) {
     console.log("start: " + start + ", end:" + end)
     start += 2;
     start -=2;
}
*/

// now to practice reversing and array
// warite a function reverse (arr) to reverse an array

function reverse(array) {
     console.log(array);
     for (var i=0; i<array.length/2; i++) {
          var temp = array[i]; // assigns value of array[1] to temporary
          var last= array[array.length-1-i]; // assigns last to i-1 array value\
          array[i] = last;  // assign value of last to array[i]
          array[array.length-1-i] = temp; // assign value at last place as value of temp
     }
     return array;
}

var result = reverse(["a", "b", "c", "d", "e", "f"]);
console.log(result)

// for i = 0, temp is a, last is e --> we swap them
// the for loop repeats till i < array.length/1

/*
var temp = array[0]
for i = 0; i<=array.legnth/2 -1; i++ {
     array[i] = array[array.length-1-i];
     array[array.legnth-1-i] = temp
     temp = array[i+1];
}
*/
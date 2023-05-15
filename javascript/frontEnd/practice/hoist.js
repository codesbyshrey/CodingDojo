// Practice reading JavaScript the same way as the interpreter reads it

// GIVEN
console.log(example);
var example = "I'm the example!";
// AFTER HOISTING BY THE INTERPRETER
    // var example;
    // console.log(example); // logs undefined
    // example = "I'm the example!";

    // console.log(example2);
    // let example2 = "I'm the example!";
    // ReferenceError: Cannot access example2 before initialization

/* 
1. Rewrite the given code as it is seen by the intrepreter
2. Predict the outputs
3. Run the original code and compare the outputs to your predictions
*/

console.log("====================") //DONE
// PROBLEM 1 -----------------------------------------------------

console.log(hello);
var hello = 'world';
    // AFTER HOISTING BY THE INTERPRETER
    // var hello;
    // console.log(hello) // logs undefined
    // hello = "world";


console.log("====================")
// PROBLEM 2 -----------------------------------------------------

var needle = 'haystack';
test();
function test() {
    var needle = 'magnet';
    console.log(needle);
}
// AFTER HOISTING BY THE INTERPRETER
    // var needle = `haystack`;
    // function test() {
    //     var needle = 'magnet';
    //     console.log(needle) // will console log magnet as it is the local scope being called within the function
    // }
    // test(); // will console log magnet now that the function is called. It recognizes the function's purpose once encountering the function, even on a preceding line

console.log("====================")
// PROBLEM 3 -----------------------------------------------------

var brendan = 'super cool';
function print() {
    brendan = 'only okay';
    console.log(brendan);
}
console.log(brendan);
// AFTER HOISTING BY THE INTERPRETER
    // Will only console.log "super cool" since print function was never called

console.log("====================")
// PROBLEM 4 -----------------------------------------------------

var food = 'chicken';
console.log(food);
eat();
function eat() {
    food = 'half-chicken';
    console.log(food);
    var food = 'gone';
}
// AFTER HOISTING BY THE INTERPRETER
    // food has been defined as chicken
    // console log will print "chicken"
    // function will be interpreted prior to function call, even though it's on a preceding line
    // the function declares food, a global variable, as half-chicken in the scope of the function. 
    // console log will then print "half chicken"
    // the function then changes food to be defined as "gone", but there is no console.log that will result in it being printed

console.log("====================")
// PROBLEM 5 -----------------------------------------------------

mean();
console.log(food);
var mean = function () {
    food = "chicken";
    console.log(food);
    var food = "fish";
    console.log(food);
}
console.log(food);
    // AFTER HOISTING BY THE INTERPRETER
    // mean is not a function that it will recognize through the var method, as that means the variable might be hoisted to exist, but the function itself won't be. so this code will immediately throw an error.
    // the console log of food outside of the function ^on line 91 above the comments area will not trigger either since food is not declared outside of the scope of the function / variable declaration of function

console.log("====================")
// PROBLEM 6 -----------------------------------------------------

console.log(genre);
var genre = "disco";
rewind();
function rewind() {
    genre = "rock";
    console.log(genre);
    var genre = "r&b";
    console.log(genre);
}
console.log(genre);
// AFTER HOISTING BY THE INTERPRETER
    // var genre;
    // undefined first console.log
    // rewind function will print rock, r&b
    // console.log outside of function will print disco, since that is still the value assigned to the global variable and the function's changes are for a locally scoped variable


console.log("====================")
// PROBLEM 7 -----------------------------------------------------

dojo = "san jose";
console.log(dojo);
learn();
function learn() {
    dojo = "seattle";
    console.log(dojo);
    var dojo = "burbank";
    console.log(dojo);
}
console.log(dojo);

// AFTER HOISTING BY THE INTERPRETER
    // console log san jose, seattle, burbank, and san jose

console.log("====================")
// PROBLEM 8 -----------------------------------------------------

console.log(makeDojo("Chicago", 65));
console.log(makeDojo("Berkeley", 0));
function makeDojo(name, students) {
    const dojo = {};
    dojo.name = name;
    dojo.students = students;
    if (dojo.students > 50) {
        dojo.hiring = true;
    }
    else if (dojo.students <= 0) {
        dojo = "closed for now";
    }
    return dojo;
}
// AFTER HOISTING BY THE INTERPRETER
    // the function will be able to create Chicago Dojo
    // the function will fail entirely to run  because dojo is a constant and a dictionary (tuple)
    // We would need a dictionary that can be changed, which is ideal with a let
    // if we replaced const with a let, the function would reveal Chicago and would reveal that Dojo's only value is "closed for now"
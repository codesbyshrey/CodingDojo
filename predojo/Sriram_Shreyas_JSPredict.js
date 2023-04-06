function myBirthYearFunc(){
         console.log("I was born in " + 1980);
}

// Predict 1 : what will console log state when this function is called?
// console.log should print "I was born in 1980"
// 1980 is a predefined number and not a variable, but separte from the string


function myBirthYearFunc(birthYearInput){
         console.log("I was born in " + birthYearInput);
     }     

// Predict 2: if var birthYearInput = 1980 then console.log should print the same as predict 1
// "I was born in 1980"


function add(num1, num2){
     console.log("Summing Numbers!");
     console.log("num1 is: " + num1);
     console.log("num2 is: " + num2);
     var sum = num1 + num2;
     console.log(sum);
}

// Predict 3: if var num1 = 10 and var num2 = 20, what would console.log state?
/*

Summing Numbers!
num1 is: 10
num2 is: 20
30

 */
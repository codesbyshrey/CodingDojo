// Preduct Desctructuring - For the following five blocks of code, predict the output. If a line of code will throw an error, state the error.

console.log("========== PROBLEM 1 ==========")

const cars = ['Tesla', 'Mercedes', 'Honda']
const [ randomCar ] = cars // tesla
const [ ,otherRandomCar ] = cars // mercedes
//Predict the output
console.log(randomCar)
console.log(otherRandomCar)

// should have no error, just print out Tesla, then Mercedes
// Tesla
// Mercedes


console.log("========== PROBLEM 2 ==========")

const employee = {
    name: 'Elon',
    age: 47,
    company: 'Tesla'
}
const { name: otherName } = employee;
//Predict the output
console.log(name); // will throw an error since you have to declare employee.name for the object call
console.log(otherName); // will print out Elon since that is the destructured value from tuple employee to be assigned to otherName

// error with console.log(name);


console.log("========== PROBLEM 3 ==========")

const person = {
    name: 'Phil Smith',
    age: 47,
    height: '6 feet'
}
const password = '12345';
const { password: hashedPassword } = person;  
//Predict the output
console.log(password); //12345
console.log(hashedPassword); //undefined since password is not part of the person 

// no errors
// 12345
// undefined

console.log("========== PROBLEM 4 ==========")

const numbers = [8, 2, 3, 5, 6, 1, 67, 12, 2];
const [,first] = numbers; // 2
const [,,,second] = numbers; //5
const [,,,,,,,,third] = numbers; //2
//Predict the output
console.log(first == second); //false, 2 is not equal to 5
console.log(first == third); // true, 2 is equal to 2

// no errors
// false
// true

console.log("========== PROBLEM 5 ==========")

const lastTest = {
    key: 'value',
    secondKey: [1, 5, 1, 8, 3, 3]
}
const { key } = lastTest; // value
const { secondKey } = lastTest; // array of numbers
const [ ,willThisWork] = secondKey; //pulls 5 from second array? slightly new

//Predict the output
console.log(key);
console.log(secondKey);
console.log(secondKey[0]); //1
console.log(willThisWork);

// no error
// value
// [1, 5, 1, 8, 3, 3]
// 1
// 5 (comma means skip one value, so we destructured lastTest's key named secondKey and assigned the second value of that array (first index) to the variable name willThisWork)
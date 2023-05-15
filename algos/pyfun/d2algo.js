// with Tyler Thibault 2/7

/** String: reverse
 * given a string, return a new string that is reversed
 */

const str1="creature";
const expected1="erutaerc";

const str2="dog";
const expected2="god";

const str3="hello";
const expected3="olleh";

const str4="";
const expected4="";

/** Reverses the given string
 * Time: O(?)
 * Space: O(?)
 * 
 * @param {string} str String to be reversed
 * @returns {string} The given string reverwse
 * 
 * Create a function that takes in a string
 * Create a var to hold the new string
 * Start a loop from the end of the given string
 * .... add the current index to the new string
 * Return new string
 */

function reverseString(str) {
     var newString="";
     for (var i=str.length-1; i>=0; i--) {
          newString += str[i];
     }
     return newString;
}

console.log(reverseString(str1));

/************************************************************************ */

/** Acronyms
 * Create a function that, given a string, returns the string's acronym (first letter of each word capitalized)
 * Do it with .split first if you need to, then try it without
 */

const two_str1 = "object oriented programming";   
const two_expected1 = "OOP";

// The 4 pillars of OOP
const two_str2 = "abstraction polymorphism inheritance encapsulation";
const two_expected2 = "APIE";

const two_str3 = "software development life cycle";
const two_expected3 = "SDLC";

// Bonus: ignore extra spaces
const two_str4 = "  global   information tracker    ";
const two_expected4 = "GIT";``

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
function acronymize(str) {
     var newString = str.split(" ");
     var acronym ="";
     // look for space
     newString[0]=newString[0].toUpperCase();
     return newString;
}

console.log(acronymize(two_str1));
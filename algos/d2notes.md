# Day 2
Whats next

```js
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
```
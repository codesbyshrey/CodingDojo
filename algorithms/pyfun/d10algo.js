
/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

const str2 = "   hello  darkness my   old    friend     ";
const expected2 = "hello  darkness my   old    friend";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
function trim(str) {
     var finTrim = false;
     var  newStr = "";
     for (var i = 0; i < str.length; i++) {
          if (str[i] !== ' ') {
               finTrim = true;
          }
          if (finTrim) {
               newStr += str[i];
          }
     return newStr
     }
}

var result = trim(str1);
console.log(result);
var result2 = trim(str2);
console.log(result2);
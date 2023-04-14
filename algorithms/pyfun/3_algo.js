/* 
  Recursively reverse a string
  helpful methods:
  str.slice(beginIndex[, endIndex])
  returns a new string from beginIndex to endIndex exclusive
*/

const str1 = "abc";
const expected1 = "cba";

const str2 = "";
const expected2 = "";

const str3 = "Python"

/**
 * Recursively reverses a string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given str reversed.
 * 
 * - edge case
 * - base case
 * - recursive call
 */
function reverseStr(str) {
     if (str.length <= 1) {
          return str;
     }
     else {
          // console.log("repeat", str.charAt(str.length-1));
          return str.charAt(str.length-1) + reverseStr(str.substring(0, str.length-1));
     }
}

console.log(reverseStr(str1));
console.log(reverseStr(str3));

     // str.charAt(str.length-1) is a more efficient process than substring ^^
     // str.substring(str.length-1) --> last value in string
     // str.substring (start, end) --> gives back a string
     // return last value in string + return reverseStr(remainder of string without last value)

/*****************************************************************************/

/*
  Recursive Binary Search
  Input: SORTED array of ints, int value
  Output: bool representing if value is found
  Recursively search to find if the value exists, do not loop over every element.
  Approach:
  Take the middle item and compare it to the given value.
  Based on that comparison, narrow your search to a particular section of the array
*/

const two_nums1 = [1, 3, 5, 6];
const two_searchNum1 = 4;
const two_expected1 = false;

const two_nums2 = [4, 5, 6, 8, 12];
const two_searchNum2 = 5;
const two_expected2 = true;

const two_nums3 = [3, 4, 6, 8, 12];
const two_searchNum3 = 3;
const two_expected3 = true;

/**
 * Add params if needed for recursion
 * Recursively performs a binary search (divide and conquer) to determine if
 * the given sorted nums array contains the given number to search for.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the searchNum was found in the sortedNums array.
 */
// function binarySearch(sortedNums, searchNum) {
//      // if statement --> false by default, exit once search is complete OR exit with True if searchNum is found
//      const middle = Math.floor(sortedNums.length - 0);

//      if (searchNum) {
//           console.log(f"Found:"{searchNum})
//           return searchNum;
//           // if we found searchNum, exit with True.
//           // if not, exit with False.
//      }
//      else {

//      }
//      // return
// }

// console.log(binarySearch(two_nums1, two_searchNum1));
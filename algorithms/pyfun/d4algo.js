
/* 
String: Is Palindrome
Create a function that returns a boolean whether the string is a strict palindrome. 
- palindrome = string that is same forwards and backwards

Do not ignore spaces, punctuation and capitalization
*/

const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given str is a palindrome or not.
 */
function isPalindrome(str) {
  var expected = true;
    for (var left = 0; left < str.length/2; left++) {
      var right = str.length-1-left;
      if (str[left] != str[right]) {
        expected = false;
        return expected;
      }
    }
    return expected;
}

function isPal2(str){
  var reverseStr = "";
  for (var i = str.length - 1; i >=0; i--) {
    reverseStr += str[i]
  }
  return str === reverseStr ? true : false
}

console.log(isPalindrome(str1));
console.log(isPalindrome(str2));
console.log(isPalindrome(str3));
console.log(isPalindrome(str4));

console.log(isPal2(str1));
console.log(isPal2(str2));
console.log(isPal2(str3));
console.log(isPal2(str4));

/*****************************************************************************/

/* 
  Longest Palindrome
  For this challenge, we will look not only at the entire string provided,
  but also at the substrings within it.
  Return the longest palindromic substring. 
  Strings longer or shorter than complete words are OK.
  All the substrings of "abc" are:
  a, ab, abc, b, bc, c
*/

const two_str1 = "what up, daddy-o?";
const two_expected1 = "dad";

const two_str2 = "uh, not much";
const two_expected2 = "u";

const two_str3 = "Yikes! my favorite racecar erupted!";
const two_expected3 = "e racecar e";

const two_str4 = "a1001x20002y5677765z";
const two_expected4 = "5677765";

const two_str5 = "a1001x20002y567765z";
const two_expected5 = "567765";

/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The longest palindromic substring from the given string.
 */
function longestPalindromicSubstring(str) {

}/**
 * - Time: O(n^3). Cubed. The nested for loops make it n^2, but then there
 *    is a 3rd loop that is nested from the slice which in the worst case
 *    slices the whole string. We focus on the worst case even though all
 *    but one iteration is not slicing the whole string.
 * - Space: O(n) linear.
 */
function longestPalindromicSubstring(str = "") {
  let longestPalindrome = str[0];

  // generate every sub string 1 at a time and check
  // if it is a palindrome and how long it is.
  for (let i = 0; i < str.length; i++) {
    for (let j = i + 1; j < str.length + 1; j++) {
      let subStr = str.slice(i, j);

      // No need to check if it is a palindrome if it can't be longer.
      if (subStr.length > longestPalindrome.length && isPalindrome(subStr)) {
        longestPalindrome = subStr;
      }
    }
  }
  return longestPalindrome;
}

console.log(longestPalindromicSubstring(two_str1));
console.log(longestPalindromicSubstring(two_str2));
console.log(longestPalindromicSubstring(two_str3));
console.log(longestPalindromicSubstring(two_str4));
console.log(longestPalindromicSubstring(two_str5));

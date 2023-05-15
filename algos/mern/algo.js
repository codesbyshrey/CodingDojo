function canMakePalindrom(s) {
    let countChars = new Map();

    // Count the occurrences of each character
    for (let i = 0; i < s.length; i++) {
        let c = s.charAt(i);
        let count = countChars.get(c);
        if (count == null) {
            count = 1;
        } else {
            count = count + 1;
        }
        countChars.set(c, count);
    }

    let hasOdd = false;
    for (let count of countChars.values()) {
        if (count % 2 === 1) {
            if (hasOdd) {
                // Found two chars with odd counts - return false;
                return false;
            } else {
                // Found the first char with odd count
                hasOdd = true;
            }
        }
    }

    // Haven't found more than one char with an odd count
    return true;
}

const str1 = "";
const expected1 = false;

const str2 = "a";
const expected2 = true;

const str3 = "ddaa";
const expected3 = true;
// Explanation: "daad" or "adda"

const str4 = "dda";
const expected4 = true;
// Explanation: "dad"

const str5 = "adaad";
const expected5 = true;
// Explanation: "daaad" / "adada"

const  str6 = "abc";
const expected6 = false;

console.log(canMakePalindrom(str1))
console.log(canMakePalindrom(str2))
console.log(canMakePalindrom(str3))
console.log(canMakePalindrom(str4))
console.log(canMakePalindrom(str5))
console.log(canMakePalindrom(str6))
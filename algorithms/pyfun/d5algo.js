/* 
  Zip Arrays into Map
  
  
  Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
  Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
  abc: 42,
  3: "wassup",
  yo: true,
};

const keys2 = [];
const vals2 = [];
const expected2 = {};

// ****************** Potential Edge Cases *************************
// Can you have a bool as a key??
const keys3 = ["abc", 3, "yo", true];
const vals3 = [42, "wassup", true, 5];
const expected3 = '?'

const keys4 = ["abc", 3, "yo", 'something'];
const vals4 = [42, "wassup", true];
const expected4 = {
  abc: 42,
  3: "wassup",
  yo: true,
  something: undefined
};

const keys5 = ["abc", 3, "yo"];
const vals5 = [42, "wassup", true, 'something'];
const expected5 = false


/**
 * Converts the given arrays of keys and values into an object.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} keys
 * @param {Array<any>} values
 * @returns {Object} The object with the given keys and values.
 */
function zipArraysIntoMap(keys, values) {

     //var expect = keys.map(function(e, i) {
          //return [e, values[i]];
     //});
     //console.log(expect);

     var result = {};
     for (let i = 0; i < keys.length; i++){
          // let key = keys[i]
          // let value = values[i]
          if (values.length > keys.length) {
               return false;
          }
          result[keys[i]] = values[i];
     }
     return result;
}



console.log(zipArraysIntoMap(keys1, vals1));
console.log(zipArraysIntoMap(keys2, vals2));
console.log(zipArraysIntoMap(keys3, vals3));
console.log(zipArraysIntoMap(keys4, vals4));
console.log(zipArraysIntoMap(keys5, vals5));

/* 
  Invert Hash
  A hash table / hash map is an obj / dictionary
  Given an object / dict,
  return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const two_obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const two_expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

// ****************** Potential Edge Cases *************************

const two_obj2 = { name: "Zaphod", charm: "high", morals: "dicey", something:"dicey" };
const two_expected2 = { Zaphod: "name", high: "charm", dicey: ["morals", "something"] };
const two_expected3 = { Zaphod: "name", high: "charm", dicey: "morals", dicey2: "something" };

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, any>} obj
 * @return The given object with key value pairs inverted.
 */
function invertObj(obj) {
     newObj = {};
     for (var [key, value] of Object.entries(obj)) {
          newObj[value] = key;
     }
     return newObj;
}

console.log(invertObj(two_obj1));
console.log(invertObj(two_obj2));
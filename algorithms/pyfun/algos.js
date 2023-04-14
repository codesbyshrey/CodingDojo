// 2.22.23 - Wednesday

/* 
  Given a SORTED array of integers, dedupe the array 
  Because array elements are already in order, all duplicate values will be grouped together.
  Ok to use a new array
  Bonus: do it in O(n) time (no nested loops, new array ok)
  Bonus: Do it in-place (no new array)
  Bonus: Do it in-place in O(n) time and no new array
  Bonus: Keep it O(n) time even if it is not sorted
*/

const nums1 = [1, 1, 1, 1];
const expected1 = [1];

const nums2 = [1, 1, 2, 2, 3, 3];
const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
const expected3 = [1, 2, 3, 4];

const nums4 = [1, 1];
const expected4 = [1];

/**
 * De-dupes the given sorted array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {Array<number>} The given array deduped.
 */

// nums.splice(i,1)
// empty - tried .hasOwnProperty
// tried (!(nums[i] in newnums)) w/out else statement

function dedupeSorted(nums) {
     newnums=[];
     for (let i = 0; i < nums.length; i++) {
          if (nums[i] !== newnums[newnums.length-1]) {
               newnums.push(nums[i]);
               // Pushing in each new unique value
               // Don't push in if the value is already present in newnums
          }
     }
     return newnums;
}

console.log(dedupeSorted(nums1))
console.log(dedupeSorted(nums2))
console.log(dedupeSorted(nums3))
console.log(dedupeSorted(nums4))

/* 
  Given an array of integers
  return the first integer from the array that is not repeated anywhere else
  If there are multiple non-repeated integers in the array,
  the "first" one will be the one with the lowest index.
*/

const anums1 = [3, 5, 4, 3, 4, 6, 5];
const aexpected1 = 6;

const anums2 = [3, 5, 5];
const aexpected2 = 3;

const anums3 = [3, 3, 5];
const aexpected3 = 5;

const anums4 = [5];
const aexpected4 = 5;

const anums5 = [];
const aexpected5 = null;

/**
 * Finds the first int from the given array that has no duplicates. I.e., the
 *    item at the lowest index that doesn't appear again in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number|null} The first int value from the given array that has no
 *    dupes or null if there is none.
 */
function firstNonRepeated(nums) {
     // frequency table it up
     numcount = {};
     nr = []; //first non repeated values
     for (i = 0; i < nums.length; i++) {
          if (numcount[nums[i]]) {
               numcount[nums[i]] += 1;
          }
          else {
               numcount[nums[i]] = 1; //which line
          }
     }

     for (i = 0; i < numcount.length; i++) {
          if (numcount[i] === 1 ) {
               nr.push[numcount[i]];
               console.log(nr); // I don't even think it's getting to this since it doesnt give us undefined even
          }
     }
     console.log(numcount);
     return nr;
}


//console.log(firstNonRepeated(anums1));
//console.log(firstNonRepeated(anums2));
//console.log(firstNonRepeated(anums3));
//console.log(firstNonRepeated(anums4));
//console.log(firstNonRepeated(anums5));
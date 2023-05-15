
class ListNode {
     constructor(data) {
          this.data = data;
          this.next = null;
     }
}

/**
 * This class keeps track of the start (head) of the list and to store all the
 * functionality (methods) that each list should have.
 */
class SinglyLinkedList {
     constructor() {
          this.head = null;
     }

     isEmpty() {
          return this.head === null ? true : false
     }


     insertAtBack(data) {
          const newElement = new ListNode(data);

          if (this.head == null) {
               this.head = newElement;
               return this;
          }

          let runner = this.head;
          while (runner.next != null) {
               runner = runner.next;
          }
          runner.next = newElement;
          return this;
     }


     /**
    * Removes the last node of this list.
    * - Time: O(?).
    * - Space: O(?).
    * @returns {any} The data from the node that was removed.
    */
     removeBack() { }

     /**
      * Determines whether or not the given search value exists in this list.
      * - Time: O(?).
      * - Space: O(?).
      * @param {any} val The data to search for in the nodes of this list.
      * @returns {boolean}
      */
     contains(val) { }

     /**
      * Determines whether or not the given search value exists in this list.
      * - Time: O(?).
      * - Space: O(?).
      * @param {any} val The data to search for in the nodes of this list.
      * @param {?ListNode} current The current node during the traversal of this list
      *    or null when the end of the list has been reached.
      * @returns {boolean}
      */
     containsRecursive(val, current = this.head) { }




     insertAtBackMany(vals) {
          for (const item of vals) {
               this.insertAtBack(item);
          }
          return this;
     }


     toArr() {
          const arr = [];
          let runner = this.head;

          while (runner) {
               arr.push(runner.data);
               runner = runner.next;
          }
          return arr;
     }
}

/******************************************************************* 
Multiple test lists already constructed to test your methods on.
Below commented code depends on insertAtBack method to be completed,
after completing it, uncomment the code.
*/
const emptyList = new SinglyLinkedList();

const singleNodeList = new SinglyLinkedList().insertAtBackMany([1]);
const biNodeList = new SinglyLinkedList().insertAtBackMany([1, 2]);
const firstThreeList = new SinglyLinkedList().insertAtBackMany([1, 2, 3]);
const secondThreeList = new SinglyLinkedList().insertAtBackMany([4, 5, 6]);
const unorderedList = new SinglyLinkedList().insertAtBackMany([
     -5, -10, 4, -3, 6, 1, -7, -2,
]);


// Print your list like so:
console.log(firstThreeList.toArr());

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

     insertAtFront(data) {
          const newHead = new ListNode(data);
          newHead.next = this.head;
          this.head = newHead;
          return this;
     }

     removeHead() {
          if (this.isEmpty()) {
               return null;
          }

          const oldHead = this.head;
          this.head = oldHead.next;
          return oldHead.data;
     }

     removeBack() {
          if (this.isEmpty()) {
               return null;
          }

          // Only 1 node.
          if (this.head.next === null) {
               return this.removeHead();
          }

          // More than 1 node.
          let runner = this.head;

          while (runner.next.next) {
               runner = runner.next;
          }
     }


     /**
      * Retrieves the data of the second to last node in this list.
      * - Time: O(?).
      * - Space: O(?).
      * @returns {any} The data of the second to last node or null if there is no
      *    second to last node.
      */
     secondToLast() {
          let runner = this.head;
          if (runner == null || runner.next == null) return "Not enough nodes";

          while (runner != null) {
               if (runner.next.next == null) return runner.data;
               runner = runner.next;
          }
     }


     /**
      * Removes the node that has the matching given val as it's data.
      * - Time: O(?).
      * - Space: O(?).
      * @param {any} val The value to compare to the node's data to find the
      *    node to be removed.
      * @returns {boolean} Indicates if a node was removed or not.
      */
     removeVal(val) { }

     // EXTRA
     /**
      * Inserts a new node before a node that has the given value as its data.
      * - Time: O(?).
      * - Space: O(?).
      * @param {any} newVal The value to use for the new node that is being added.
      * @param {any} targetVal The value to use to find the node that the newVal
      *    should be inserted in front of.
      * @returns {boolean} To indicate whether the node was pre-pended or not.
      */
     prepend(newVal, targetVal) { }




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
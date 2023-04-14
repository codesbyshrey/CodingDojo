
class ListNode {
     constructor(data) {
          this.data = data;
          this.next = null;
     }
}


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
     * Creates a new node with the given data and inserts that node at the front
     * of this list.
     * - Time: (?).
     * - Space: (?).
     * @param {any} data The data for the new node.
     * @returns {SinglyLinkedList} This list.
     */
     insertAtFront(data) { }

     /**
      * Removes the first node of this list.
      * - Time: (?).
      * - Space: (?).
      * @returns {any} The data from the removed node.
      */
     removeHead() { }

     // EXTRA
     /**
      * Calculates the average of this list.
      * - Time: (?).
      * - Space: (?).
      * @returns {number|NaN} The average of the node's data.
      */
     average() { }



     insertAtBackMany(vals) {
          for (const item of vals) {
               this.insertAtBack(item);
          }
          return this;
     }

     /**
      * Converts this list into an array containing the data of each node.
      * - Time: O(n) linear.
      * - Space: O(n).
      * @returns {Array<any>} An array of each node's data.
      */
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
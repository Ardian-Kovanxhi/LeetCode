/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
//  Definition for singly-linked list.
//   function ListNode(val, next) {
//       this.val = (val===undefined ? 0 : val)
//       this.next = (next===undefined ? null : next)
//   }
var mergeTwoLists = function(list1, list2) {
     var res = new ListNode(0, null);

    // Get a reference to the head of the merged list
    var head = res;

    // Traverse both lists and compare values at each step
    while(list1 != null && list2 != null) {
        if(list1.val <= list2.val) {
            head.next = list1;
            list1 = list1.next;
        } else {
            head.next = list2;
            list2 = list2.next;
        }

        // Move the head pointer of the merged list
        head = head.next;
    }

    // Append the remaining nodes from list1
    while(list1 != null) {
        head.next = list1;
        list1 = list1.next;
        head = head.next;
    }

    // Append the remaining nodes from list2
    while(list2 != null) {
        head.next = list2;
        list2 = list2.next;
        head = head.next;
    }

    // Return the head of the merged list
    return res.next;
    
};
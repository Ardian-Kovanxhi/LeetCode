/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let sentinel = tail = new ListNode();
    let remainder = 0;
    while (l1 || l2 || remainder) {
        const sum = (l1?.val || 0) + (l2?.val || 0) + remainder;
        remainder = Math.floor(sum / 10);
        tail.next = new ListNode(sum % 10);
        tail = tail.next

        l1 = l1?.next || null;
        l2 = l2?.next || null;
    }

    return sentinel.next
};
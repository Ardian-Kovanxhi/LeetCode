/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    let curr = head;
    let currMid = head
    let count = 0;
    let midInd = 1;

    while (curr) {
            curr = curr.next;
            count++;

            const mid = count % 2 ? Math.ceil(count / 2) : (count / 2) + 1;

            if (midInd < mid) {
                currMid = currMid.next;
                midInd++
            }
    }

    return currMid;
};
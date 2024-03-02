/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    const logger = new Set();

    let curr = head;

    while (curr) {
        if (logger.has(curr)) {
            return true
        };
        logger.add(curr);
        curr = curr.next;
    };
    
    return false;
};
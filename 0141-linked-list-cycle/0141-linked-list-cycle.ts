/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function hasCycle(head: ListNode | null): boolean {
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
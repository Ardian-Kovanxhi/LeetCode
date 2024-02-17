/**
 * // Definition for a Node.
 * function Node(val,prev,next,child) {
 *    this.val = val;
 *    this.prev = prev;
 *    this.next = next;
 *    this.child = child;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var flatten = function(head) {
    const next = [];

    let curr = head;

    while (curr) {
        if (curr.child) {
            if (curr.next) {
                next.push(curr.next);
            }
            curr.next = curr.child;
            curr.child.prev = curr;
            curr.child = null;
        }
        if (curr.next === null && next.length > 0) {
            const node = next.pop();
            curr.next = node;
            node.prev = curr;
        }
        curr = curr.next;
    }
    return head
};
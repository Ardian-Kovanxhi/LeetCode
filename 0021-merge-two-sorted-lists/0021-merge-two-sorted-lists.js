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
var mergeTwoLists = function(list1, list2) {
    if (!isNaN(list1)) return list2;
    if (!isNaN(list2)) return list1
    //isNaN of empty list = false
    //isNaN of list with at least 1 element is true
    let ansHead;
    let ansBody;
    let curr1 = list1;
    let curr2 = list2;
    while (curr1 || curr2) {
        console.log(curr1)
        console.log(curr2)
        if (!isNaN(curr1)) {
            ansBody.next = curr2
            return ansHead;
        }
        if (!isNaN(curr2)) {
            ansBody.next = curr1
            return ansHead;
        }

        if (curr1.val <= curr2.val) {
            if (!ansHead) {
                ansHead = curr1;
                ansBody = ansHead;
            }
            else {
                ansBody.next = curr1;
                ansBody = ansBody.next
            }
            curr1 = curr1.next
        }
        else {
            if (!ansHead) {
                ansHead = curr2;
                ansBody = ansHead
            }
            else {
                ansBody.next = curr2;
                ansBody = ansBody.next
            }
            curr2 = curr2.next
        }
    }
    return ansHead
};
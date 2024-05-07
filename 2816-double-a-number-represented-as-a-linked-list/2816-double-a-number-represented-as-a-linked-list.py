# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        tail = head

        while tail != None:
            stack.append(tail)
            tail = tail.next
        
        rem = 0

        while stack:
            curr = stack.pop()
            tmpV = (curr.val * 2) + rem

            curr.val = tmpV%10
            rem = tmpV//10

        if rem: head = ListNode(rem, head)
        return head
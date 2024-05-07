"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newList = tail = ListNode()

        headPoint = head

        logger = {}
        while headPoint:
            tail.next = ListNode(headPoint.val)
            logger[headPoint] = tail.next
            tail = tail.next
            headPoint = headPoint.next
        
        headPoint = head
        while headPoint:
            logger[headPoint].random = logger[headPoint.random] if headPoint.random else None
            headPoint = headPoint.next

        return newList.next
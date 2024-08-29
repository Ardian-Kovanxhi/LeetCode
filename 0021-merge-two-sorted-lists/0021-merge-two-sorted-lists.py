# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2: return list2
        if not list2 and list1: return list1

        head = sentinel = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                sentinel.next = ListNode(list1.val)
                sentinel = sentinel.next
                list1 = list1.next
            else:
                sentinel.next = ListNode(list2.val)
                sentinel = sentinel.next
                list2 = list2.next
        
        while list1 or list2:
            if list1:
                sentinel.next = ListNode(list1.val)
                sentinel = sentinel.next
                list1 = list1.next
            if list2:
                sentinel.next = ListNode(list2.val)
                sentinel = sentinel.next
                list2 = list2.next
        return head.next
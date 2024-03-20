# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        sptr = list1
        for _ in range(a - 1):
            sptr = sptr.next

        eptr = sptr.next
        for _ in range(b - a + 1):
            eptr = eptr.next

        sptr.next = list2
        while list2.next is not None:
            list2 = list2.next
        list2.next = eptr

        return list1 
        

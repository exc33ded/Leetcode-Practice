# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start_ptr = list1
        for _ in range(a - 1):
            start_ptr = start_ptr.next
        
        end_ptr = start_ptr.next
        for _ in range(b - a + 1):
            end_ptr = end_ptr.next
        
        start_ptr.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = end_ptr

        return list1


        
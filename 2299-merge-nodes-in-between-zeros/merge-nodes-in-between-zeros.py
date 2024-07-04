# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head.next
        sum = 0
        while ptr2:
            if ptr2.val != 0:
                sum += ptr2.val
            else:
                ptr1 = ptr1.next
                ptr1.val = sum
                sum = 0
            ptr2 = ptr2.next
        ptr1.next = None
        return head.next
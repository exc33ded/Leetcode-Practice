# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        curr = head.next
        sum = 0
        while curr:
            if curr.val is 0:
                lst.append(sum)
                sum = 0
            else:
                sum += curr.val
            curr = curr.next
        
        dummy = ListNode(-1)
        curr = dummy

        for num in lst:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next

        
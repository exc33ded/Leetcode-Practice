# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = ""
        curr = head
        while curr:
            res += str(curr.val)
            curr = curr.next
        
        return int(res, 2)
        
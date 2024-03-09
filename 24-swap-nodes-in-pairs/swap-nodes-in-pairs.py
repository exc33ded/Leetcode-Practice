# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        lst = []
        while curr: 
            lst.append(curr.val)
            curr = curr.next

        for i in range(1,len(lst), 2):
            lst[i-1], lst[i] = lst[i], lst[i-1]
        
        dummy = ListNode(-1)
        curr = dummy

        for i in range(len(lst)):
            curr.next = ListNode(lst[i])
            curr = curr.next

        return dummy.next
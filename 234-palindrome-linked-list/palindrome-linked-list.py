# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        
        while prev:
            if prev.val != head.val:
                return False
            head, prev = head.next, prev.next
        return True
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the other half
        prev = None
        curr = slow

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Compare
        max_ = 0
        while prev:
            max_ = max(max_, prev.val + head.val)
            prev = prev.next
            head = head.next

        return max_
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        while head.val in nums:
            head = head.next

        res = ListNode(head.val, head)

        while head and head.next:
            if head.next.val in nums:
                head.next = head.next.next
            else:
                head = head.next
        
        return res.next
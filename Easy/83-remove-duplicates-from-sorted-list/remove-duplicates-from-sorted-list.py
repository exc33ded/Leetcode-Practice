# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        dummy = curr = ListNode(head.val)
        while head is not None:
            if dummy.val != head.val:
                dummy.next = ListNode(head.val)
                dummy = dummy.next
                head = head.next
            else:
                head = head.next
        return curr
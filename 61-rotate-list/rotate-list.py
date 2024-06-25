# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        k = (len(lst)-k) % len(lst)
        lst[:] = lst[k:] + lst[:k]

        dummy = ListNode(-1)
        curr = dummy
        for num in lst:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next
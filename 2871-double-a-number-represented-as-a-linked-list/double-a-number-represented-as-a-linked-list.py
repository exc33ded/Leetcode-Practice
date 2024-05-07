# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
sys.set_int_max_str_digits(0)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = ""
        curr = head
        while curr:
            num += str(curr.val)
            curr = curr.next
        
        twice = str(int(num) * 2)
        curr = dummy = ListNode(-1)
        for n in twice:
            curr.next = ListNode(n)
            curr = curr.next

        return dummy.next

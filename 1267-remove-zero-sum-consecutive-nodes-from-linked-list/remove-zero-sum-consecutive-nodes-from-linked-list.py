# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prefixSumToNode = {}
        prefixSum = 0

        curr = dummy
        while curr:
            prefixSum += curr.val
            if prefixSum in prefixSumToNode:
                prev = prefixSumToNode[prefixSum]
                toRemove = prev.next
                p = prefixSum + (toRemove.val if toRemove else 0)
                while p != prefixSum:
                    del prefixSumToNode[p]
                    toRemove = toRemove.next
                    p += toRemove.val if toRemove else 0
                prev.next = curr.next
            else:
                prefixSumToNode[prefixSum] = curr
            curr = curr.next
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []
        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                lst.append(curr.val)
                curr = curr.next
        lst.sort()

        dummy = ListNode(-1)
        curr = dummy

        for num in lst:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next

            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev
    
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head = self.reverseList(head)
        
        current = reversed_head
        max_value = float('-inf')
        prev = None
        
        while current:
            if current.val < max_value:
                prev.next = current.next
            else:
                max_value = current.val
                prev = current
            
            current = current.next
        
        return self.reverseList(reversed_head)
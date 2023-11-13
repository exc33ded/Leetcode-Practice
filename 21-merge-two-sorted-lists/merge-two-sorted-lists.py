# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = dummy = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next

            curr = curr.next

        if not list1:
            curr.next = list2
        else:
            curr.next = list1
        
        return dummy.next

    # Points to Remember
    # 1. First we define a dummy node and current node pointing to nothing.
    # 2. Then we start the loop for both l1 and l2.
    # 3. Now we check which first element is greater for the linked lists.
    # 4. For instance l1 is greater l2, then we point the next value of the current node to the l2 linked list.
    # 5. We also point the l2 to the l2.next (next element)
    # 6. For the "else" condition we perform viceversa.
    # 7. we set the "while" change condition to [curr = curr.next].
    # 8. Second, we look at the edge cases, if l1 is empty then the curr.next will point to l2.
    # 9. Viceversa, for the "else" condition
    # 10. Finally we return the dummpy node(according to the question on what to return).
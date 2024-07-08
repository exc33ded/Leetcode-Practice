class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        head = None
        tail = None

        for i in range(1, n+1):
            node = Node(i)
            if not head:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node
        
        tail.next = head

        ## Solving the problem now
        curr = head
        cross = 0
        while cross != (n-1):
            for _ in range(k-1):
                curr = curr.next
                while curr.val < 0:
                    curr = curr.next
            curr.val *= -1 
            cross += 1 
            if cross == (n-1):
                break 
            curr = curr.next
            if curr.val < 0:
                while curr.val < 0:
                    curr = curr.next

        curr = head
        while curr:
            if curr.val > 0: # Finding the only value > 0, that's our answer
                return curr.val
            curr = curr.next
        
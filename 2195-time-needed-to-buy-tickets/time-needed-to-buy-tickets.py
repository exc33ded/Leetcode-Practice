class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time, i = 0, 0
        while tickets[k] != 0 and i < len(tickets):
            if tickets[i] != 0:
                tickets[i] -= 1
                time += 1
                
            i += 1  # Move to the next person

            if i == len(tickets):
                i = 0  # Reset to the first person if reached the end of the list
            
            if i == k and tickets[i] == 0:
                return time

        return time

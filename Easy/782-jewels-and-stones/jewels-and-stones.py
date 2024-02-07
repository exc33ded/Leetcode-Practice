class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Brute Force

        # counter = 0
        # for j in jewels:
        #     for s in stones:
        #         if j == s:
        #             counter += 1        
        # return counter
        

        # Optimized
        set_jewels = set(jewels)
        counter = 0

        for item in stones:
            if item in set_jewels:
                counter += 1
        
        return counter
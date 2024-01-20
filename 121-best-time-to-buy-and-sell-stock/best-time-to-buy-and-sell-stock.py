class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min, max = float("inf"), 0 

        for price in prices:
            if price < min:
                min = price
            elif price - min > max:
                max = price - min
        
        return max
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minNum = float("inf")
        for price in prices:
            if minNum > price:
                minNum = price
            maxi = price - minNum
            if maxi > maxProfit:
                maxProfit = maxi

        return maxProfit
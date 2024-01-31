class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n:
            n = n & (n - 1)
            sum += 1
        return sum
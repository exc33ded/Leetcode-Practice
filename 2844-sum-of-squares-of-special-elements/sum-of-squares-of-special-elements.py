class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sum_ = 0
        for idx, num in enumerate(nums):
            if n % (idx+1) == 0:
                sum_ += num*num

        return sum_
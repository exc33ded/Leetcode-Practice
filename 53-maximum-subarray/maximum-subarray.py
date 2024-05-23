class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cum_sum = 0
        max_sum = float('-inf')

        for num in nums:
            cum_sum += num
            max_sum = max(max_sum, cum_sum)
            if cum_sum < 0:
                cum_sum = 0
        return max_sum
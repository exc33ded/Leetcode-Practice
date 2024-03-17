class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum = max(num, curr_sum + num)
            maxi = max(maxi, curr_sum)
        return maxi
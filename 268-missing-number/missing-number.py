class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = n * (n + 1) // 2
        s = sum(nums)
        return max_sum - s
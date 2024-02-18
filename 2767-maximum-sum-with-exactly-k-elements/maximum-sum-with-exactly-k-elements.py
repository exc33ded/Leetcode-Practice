class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        m = 0
        for i in range(k):
            m += nums[len(nums) - 1] + i
        return m
        
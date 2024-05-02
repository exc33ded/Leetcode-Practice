class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = sorted(nums)[::-1]
        for num in nums:
            if -num in nums:
                return num
        return -1
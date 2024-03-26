class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # brute force
        res = 1
        nums.sort()
        for num in nums:
            if num == res:
                res += 1
        return res
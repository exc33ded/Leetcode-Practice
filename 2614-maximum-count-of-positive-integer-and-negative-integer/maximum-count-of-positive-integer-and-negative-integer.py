class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        max_pos = 0
        max_neg = 0

        for num in nums:
            if num > 0:
                max_pos += 1
            elif num < 0:
                max_neg += 1
        return max(max_pos, max_neg)
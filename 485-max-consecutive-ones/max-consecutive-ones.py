class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones_cnt = 0
        maxi = 0
        for num in nums:
            if num == 1:
                max_ones_cnt += 1
            else:
                max_ones_cnt = 0
            maxi = max(maxi, max_ones_cnt)

        return maxi
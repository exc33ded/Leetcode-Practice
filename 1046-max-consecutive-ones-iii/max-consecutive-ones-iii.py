class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCnt = 0
        l, r = 0, 0
        maxLen = -1
        while (r < len(nums)):
            if nums[r] == 0:
                zeroCnt += 1
            while zeroCnt > k:
                if nums[l] == 0:
                    zeroCnt -= 1
                l += 1
            maxLen = max(maxLen, r-l+1)
            r += 1
        return maxLen
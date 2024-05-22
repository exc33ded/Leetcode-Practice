class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k = 0
        while (True):
            if k in nums:
                k += 1
            else:
                return k
                
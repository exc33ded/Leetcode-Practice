class Solution:
    def check(self, nums: List[int]) -> bool:
        k = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                k += 1
            if k > 1: return False
        return True
        
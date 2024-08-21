class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        min_ = float('inf')
        nums.sort()
        l = 0
        r = len(nums) - 1

        while l < r:
            avg = (nums[l] + nums[r])/ 2
            min_ = min(min_, avg)
            l += 1
            r -= 1

        return min_

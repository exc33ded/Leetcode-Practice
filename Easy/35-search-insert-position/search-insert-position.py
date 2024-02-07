class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # As it is asking for a time complexity of O(logn) it's binary search
        l = 0
        r = len(nums)

        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l


            
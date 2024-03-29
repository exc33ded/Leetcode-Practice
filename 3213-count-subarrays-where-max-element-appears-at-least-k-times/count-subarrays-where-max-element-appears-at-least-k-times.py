class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        biggest_num = max(nums)
        l, count, res = 0,0,0
        for r, val in enumerate(nums):
            if val == biggest_num:
                count += 1
            while count == k:
                if nums[l] == biggest_num:
                    count -= 1
                l += 1
            res += l
        return res
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_count = 0
        max_value = max(nums)
        res = 0
        left = 0

        for right, val in enumerate(nums):
            while left < len(nums) and max_count < k:
                max_count += nums[left] == max_value
                left += 1

            if max_count >= k:
                res += len(nums) - left + 1

            max_count -= val == max_value

        return res

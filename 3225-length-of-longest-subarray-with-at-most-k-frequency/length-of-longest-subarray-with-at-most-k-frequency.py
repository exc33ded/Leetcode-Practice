class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0 
        hm = defaultdict(int)
        l = 0

        for r in range(len(nums)):
            hm[nums[r]] += 1
            while hm[nums[r]] > k:
                hm[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
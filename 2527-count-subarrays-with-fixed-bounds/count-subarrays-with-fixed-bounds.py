class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        bad = mi = ma = -1
        for i, val in enumerate(nums):
            if not minK <= val <= maxK:
                bad = i

            if minK == val: mi=i
            if maxK == val: ma=i

            start = min(mi, ma)

            if start > bad: res += (start - bad)

        return res
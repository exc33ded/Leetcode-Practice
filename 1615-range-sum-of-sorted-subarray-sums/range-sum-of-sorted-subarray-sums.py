class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        MOD = 10**9 + 7
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                res.append(sum(nums[i:j+1]) % MOD)
        res.sort()
        sum_ = 0
        for i in range(left-1, right):
            sum_ += res[i] % MOD
        return sum_ % MOD
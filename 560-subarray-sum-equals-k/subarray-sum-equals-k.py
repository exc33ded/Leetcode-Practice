class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0:1}
        currSum = 0
        res = 0
        for num in nums:
            currSum += num
            diff = currSum - k
            if diff in hm:
                res += hm[diff]
            hm[currSum] = hm.get(currSum, 0) + 1
        return res
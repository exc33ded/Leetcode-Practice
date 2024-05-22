class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1

        for key, val in hm.items():
            if val == 1:
                return key
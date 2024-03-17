class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1

        for idx, val in hm.items():
            if val > n:
                return idx

        return 0
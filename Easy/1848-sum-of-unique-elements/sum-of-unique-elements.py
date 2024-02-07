class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hm = {}
        sum = 0
        for num in set(nums):
            hm[num] = nums.count(num)

        for key, val in hm.items():
            if val == 1:
                sum += key
        return sum
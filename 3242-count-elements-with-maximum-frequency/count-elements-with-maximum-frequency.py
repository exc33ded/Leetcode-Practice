class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dummy = {}

        for num in set(nums):
            dummy[num] = nums.count(num)

        maxi = 0
        for val in dummy.values():
            maxi = max(maxi, val)

        sum = 0
        for val in dummy.values():
            if val == maxi:
                sum += val
        
        return sum
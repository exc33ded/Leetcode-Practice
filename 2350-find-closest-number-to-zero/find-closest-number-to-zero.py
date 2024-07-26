class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        MIN = float('inf')
        for num in nums:
            if abs(num) < abs(MIN):
                MIN = num
            elif abs(num) == abs(MIN):
                MIN = max(num, MIN)
        return MIN
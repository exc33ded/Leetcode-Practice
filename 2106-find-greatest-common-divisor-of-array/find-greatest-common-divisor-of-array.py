class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b= max(nums)
        while a:
            a, b = b % a, a

        return b

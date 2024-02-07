class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        sum = []
        for i in range(1, len(nums),2):
            sum += [nums[i]] * nums[i-1]

        return sum
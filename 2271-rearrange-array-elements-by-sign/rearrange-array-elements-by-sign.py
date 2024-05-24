class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        temp = [0]*len(nums)
        posIdx, negIdx = 0, 1
        for num in nums:
            if num > 0:
                temp[posIdx] = num
                posIdx += 2
            else:
                temp[negIdx] = num
                negIdx += 2
        return temp
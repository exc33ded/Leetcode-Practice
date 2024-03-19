class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        
        lst = [0] * len(nums)
        
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                lst[j] = nums[i]
                j += 1
        
        return lst
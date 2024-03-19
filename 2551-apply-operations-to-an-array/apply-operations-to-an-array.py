class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            i += 1

        # Rearrange non-zero elements to the left
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if j != i:
                    nums[i] = 0
                j += 1

        return nums
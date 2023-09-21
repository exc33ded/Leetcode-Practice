class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_count = 1
        if len(nums) == 0:
            return 0
        else:
            for i in range(1, len(nums)):
                if nums[i] != nums[i - 1]:
                    nums[unique_count] = nums[i]
                    unique_count += 1

        return unique_count 
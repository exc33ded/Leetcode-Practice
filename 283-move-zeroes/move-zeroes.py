class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        zeros = nums.count(0)
        for num in nums:
            if num != 0:
                temp.append(num)
        temp[:] += [0]*zeros
        for i in range(len(nums)):
            nums[i] = temp[i]

        
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j] and i != j:
                    count += 1
            lst.append(count)
        return lst
                    
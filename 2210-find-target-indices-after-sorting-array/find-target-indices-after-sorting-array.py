class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums.sort()
        for idx, val in enumerate(nums):
            if nums[idx] == target:
                res.append(idx)

        return res
        
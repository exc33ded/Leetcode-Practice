class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in hm:
                return [hm[diff], idx]
            hm[val] = idx
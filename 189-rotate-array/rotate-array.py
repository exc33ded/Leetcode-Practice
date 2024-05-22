class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = k % len(nums)
        nums[:] = nums[len(nums)-idx:] + nums[:len(nums)-idx]
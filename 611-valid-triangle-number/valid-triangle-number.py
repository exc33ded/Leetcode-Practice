class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        for i in range(len(nums)-1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[i] < nums[left] + nums[right]:
                    cnt += right - left
                    right -= 1
                else:
                    left += 1
        return cnt
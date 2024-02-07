class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Method 1
        # right_arr = [0] * len(nums)
        # left_arr = [0] * len(nums)
        
        # left = 0
        # right = 0

        # for i in range(len(nums)):
        #     if i > 0:
        #         left += nums[i - 1]
        #     left_arr[i] = left

        # for i in range(len(nums)-1, -1, -1):
        #     if i+1 < len(nums):
        #         right += nums[i+1]
        #     right_arr[i] = right

        # # zipping the array with zip() method
        # return [abs(l- r) for l, r in zip(left_arr, right_arr)]

        # ----------------------- OR ----------------------
        left, right = 0, sum(nums)
        ans = []
        for x in nums:
            right -= x
            ans.append(abs(left - right))
            left += x
        return ans
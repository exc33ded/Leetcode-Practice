class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # ans = []

        # for i in range(len(nums)):
        #     ans.append(nums[nums[i]])

        # return ans
        
        n = len(nums)
        for idx, val in enumerate(nums):
            nums[idx] += n * (nums[nums[idx]] % n)
        
        for i in range(len(nums)):
            nums[i] //= n

        return nums
    
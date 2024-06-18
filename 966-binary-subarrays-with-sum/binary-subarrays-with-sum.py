class Solution:
    def numSubarraysWithSumLessThanGoal(self,nums,goal):
        if goal<0:
            return 0
        left, right = 0,0
        Sum = 0
        count = 0 
        

        while right<len(nums):
            Sum += nums[right]

            while Sum>goal:
                Sum = Sum - nums[left]
                left+=1
            count+= right - left +1
            right+=1
        return count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        Ans = self.numSubarraysWithSumLessThanGoal(nums,goal) - self.numSubarraysWithSumLessThanGoal(nums,goal-1)
        return Ans
    
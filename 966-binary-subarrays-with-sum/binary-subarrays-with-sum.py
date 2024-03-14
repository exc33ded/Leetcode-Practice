class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum, totalCount = 0, 0
        prefixSum = [0] * (len(nums)+1)
        prefixSum[0] = 1

        for num in nums:
            sum += num

            if sum >= goal:
                totalCount += prefixSum[sum - goal]
            prefixSum[sum] += 1

        return totalCount
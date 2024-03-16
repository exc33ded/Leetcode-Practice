class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        prefix_sum = {0: -1} 

        max_len = 0
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num

            if curr_sum in prefix_sum:
                max_len = max(max_len, i - prefix_sum[curr_sum])
            else:
                prefix_sum[curr_sum] = i

        return max_len
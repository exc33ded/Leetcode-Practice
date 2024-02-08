class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ## Brute 

        def to_binary_one(num):
            count_one = 0
            while (num > 0):
                rem = num % 2
                if rem == 1:
                    count_one += 1
                num = num // 2
            return count_one

        sum_ = 0
        for i in range(len(nums)):
            if to_binary_one(i) == k:
                sum_ += nums[i]

        return sum_
            
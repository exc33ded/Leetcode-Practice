class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum = 0
        digit_sum = 0
        
        for num in nums:
            sum += num
            
            while num > 0:
                digit_sum = digit_sum + num % 10
                num = num // 10
            
        return abs(sum - digit_sum)
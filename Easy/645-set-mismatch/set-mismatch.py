class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = n*(n+1)//2
        set_sum = sum(set(nums))
        nor_sum = sum(nums)

        rep = nor_sum - set_sum
        loss = total_sum - set_sum

        return [rep, loss]
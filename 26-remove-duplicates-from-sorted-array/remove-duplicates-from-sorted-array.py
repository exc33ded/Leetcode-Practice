class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        for num in nums:
            if num not in unique:
                unique.append(num)
        
        k = len(unique)
        cnt = 0
        for i in range(len(nums)):
            if k > 0:
                nums[i] = unique[i]
                k -= 1
                cnt += 1
            else:
                nums[i] = 0
        return cnt
        
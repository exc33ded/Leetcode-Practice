class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        rev = []

        for num in nums:
            rev.append(int(str(num)[::-1]))
        
        st = set(nums).union(set(rev))
        print(st)
        return len(st)
        

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hm = defaultdict(int)
        hm[0] = 1

        prefix = 0
        res = 0

        for num in nums:
            prefix += num
            res += hm.get(prefix - goal, 0)
            hm[prefix] = hm.get(prefix, 0) + 1
        
        return res
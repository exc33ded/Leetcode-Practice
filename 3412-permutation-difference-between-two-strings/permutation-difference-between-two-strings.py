class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        hm = {}
        for idx, val in enumerate(s):
            hm[val] = idx

        for idx, val in enumerate(t):
            hm[val] = abs(hm[val] - idx)
        
        sum_ = 0
        for k, v in hm.items():
            sum_ += v
        return sum_
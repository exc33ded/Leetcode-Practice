class Solution:
    def maxScore(self, s: str) -> int:
        one_count = s.count('1')
        res = 0
        zero_count = 0
        for i in range(len(s) - 1):
            if s[i] == '1':
                one_count -= 1
            else:
                zero_count += 1
            res = max(res, zero_count + one_count)
        return res
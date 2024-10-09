class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = cnt = 0
        for c in s:
            if c == "(":
                res += 1
            elif res > 0:
                res -= 1
            else:
                cnt += 1
        return cnt + res
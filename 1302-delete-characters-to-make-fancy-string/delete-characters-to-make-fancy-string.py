class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[0]
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == res[-1]:
                cnt += 1
                if cnt < 3:
                    res += s[i]
            else:
                cnt = 1
                res += s[i]
        return res
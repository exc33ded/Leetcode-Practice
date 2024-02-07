class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = count = 0
        for i in range(len(s)):
            if s[i] == "L":
                res += 1
            else:
                res -= 1
            if res == 0:
                count += 1
        return count
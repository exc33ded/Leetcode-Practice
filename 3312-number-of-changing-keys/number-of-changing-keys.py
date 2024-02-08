class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        count = 0
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                count += 1 
        return count 
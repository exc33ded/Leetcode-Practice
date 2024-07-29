class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 0
        maxLen = -1
        hs = set()
        while (r < len(s)):
            if s[r] not in hs:
                hs.add(s[r])
                r += 1
                maxLen = max(maxLen, r - l)
            else:
                hs.remove(s[l])
                l += 1
        return maxLen

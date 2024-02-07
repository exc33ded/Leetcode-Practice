class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = j = 0
        g.sort()
        s.sort()
        while j < len(s) and i < len(g):
            if g[i] <= s[j]:
                i += 1
            j += 1
        
        return i
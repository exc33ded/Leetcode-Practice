class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorting so that the letters will assigned the same
        return sorted(s) == sorted(t)
        
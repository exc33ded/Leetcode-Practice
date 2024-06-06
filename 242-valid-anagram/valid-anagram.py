class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hm = {}
        for char in s:
            if char not in hm:
                hm[char] = 1
            else:
                hm[char] += 1
        
        for char in t:
            if char not in hm:
                return False
            else:
                hm[char] -= 1
                if hm[char] < 0:
                    return False
        return True
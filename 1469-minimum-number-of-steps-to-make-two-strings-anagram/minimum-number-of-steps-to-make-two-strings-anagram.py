class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hm = {}
        for char in s:
            if char not in hm:
                hm[char] = 1
            else:
                hm[char] += 1

        steps = 0
        for char in t:
            if char in hm and hm[char] > 0:
                hm[char] -= 1
            else:
                steps += 1
        
        return steps
        
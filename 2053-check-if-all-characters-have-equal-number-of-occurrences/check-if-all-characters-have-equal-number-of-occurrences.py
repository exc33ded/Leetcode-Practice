class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hm = {}
        for char in s:
            if char not in hm:
                hm[char] = 1
            else:
                hm[char] += 1

        return len(list(set(list(hm.values())))) == 1

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hm = {char: 0 for char in order}
        for char in s:
            if char in hm:
                hm[char] += 1

        res = ""
        for st in order:
            res += st * hm[st]
        
        for st in s:
            if st not in order:
                res += st

        return res
    
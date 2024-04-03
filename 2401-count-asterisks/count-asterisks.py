class Solution:
    def countAsterisks(self, s: str) -> int:
        res = 0
        bar = 0
        for char in s:
            if char == "|":
                bar += 1
            else:
                if bar % 2 == 0 and char == "*":
                    res += 1
        return res
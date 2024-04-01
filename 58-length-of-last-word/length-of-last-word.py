class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.strip().split(" ")[-1])
        # -------------------- OR ----------------------

        res = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                res += 1
            elif res:
                return res
        return res
        
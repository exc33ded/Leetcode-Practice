class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hm = {" " : " "}
        all = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        for char in key:
            if char not in hm:
                hm[char] = all[i]
                i += 1
        res = ""
        for char in message:
            res += hm[char]

        return res
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        comb = ""

        for word in words:
            comb += word[0]

        if comb == s:
            return True
        return False
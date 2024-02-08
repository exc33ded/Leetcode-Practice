class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        counter = 0
        for i in range(left, right+1):
            n = len(words[i])
            if words[i][0] in "aeiou" and words[i][n-1] in "aeiou":
                counter += 1

        return counter
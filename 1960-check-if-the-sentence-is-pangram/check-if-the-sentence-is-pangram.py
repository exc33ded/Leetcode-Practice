class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        unique = set(sentence)
        return len(unique) == 26
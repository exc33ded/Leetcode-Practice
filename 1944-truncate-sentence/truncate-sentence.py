class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        splitting_arr = s.split(" ")
        return " ".join(splitting_arr[:k])
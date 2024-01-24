class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        comb = [0] * len(s)

        for idx, char in enumerate(s):
            comb[indices[idx]] = char

        return "".join(comb)
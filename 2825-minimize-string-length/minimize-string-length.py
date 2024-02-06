class Solution:
    def minimizedStringLength(self, s: str) -> int:
        st = "".join(set(list(s)))
        return len(st)
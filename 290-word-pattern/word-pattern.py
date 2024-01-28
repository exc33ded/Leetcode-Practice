class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        st = s.split(" ")

        if len(pattern) != len(st):
            return False
        if len(set(pattern)) != len(set(st)):
            return False

        dummy = {}
        for i, j in zip(pattern, st):
            if (i in dummy and j != dummy[i]):
                return False
            dummy[i] = j
            if len(set(dummy.values())) != len(set(dummy.keys())):
                return False
        return True
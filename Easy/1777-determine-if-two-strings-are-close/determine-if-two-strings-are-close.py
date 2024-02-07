class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        wl1 = " ".join(list(word1))
        wl2 = " ".join(list(word2))

        if len(wl1) != len(wl2):
            return False
        if set(wl1) != set(wl2):
            return False
        
        lst1 = []
        lst2 = []

        for x in set(wl1):
            lst1.append(wl1.count(x))

        for y in set(wl2):
            lst2.append(wl2.count(y))

        return sorted(lst1) == sorted(lst2)
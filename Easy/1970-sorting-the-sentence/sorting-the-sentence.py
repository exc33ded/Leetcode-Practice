class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split()
        res = [None]*len(lst)

        for word in lst:
            idx = int(word[-1]) - 1
            res[idx] = word[:-1]
        
        return " ".join(res)

        
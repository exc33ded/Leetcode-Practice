class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hm = {}
        for word in s1.split():
            if word in hm:
                hm[word] += 1
            else:
                hm[word] = 1
        
        for word in s2.split():
            if word not in hm:
                hm[word] = 1
            else:
                hm[word] += 1
        res = []
        for key,val in hm.items():
            if val == 1:
                res.append(key)

        return res

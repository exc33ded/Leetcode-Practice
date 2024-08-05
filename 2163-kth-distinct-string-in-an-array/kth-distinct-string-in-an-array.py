class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hm = {}
        res = []

        for c in arr:
            if c in hm:
                hm[c] += 1
            else:
                hm[c] = 1
        
        for key, v in hm.items():
            if v == 1:
                res.append(key)
        if k <= len(res):
            return res[k-1] 
        else:
            return ""
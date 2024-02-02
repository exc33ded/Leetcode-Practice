class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] = hm[num] + 1
        
        hm = dict(sorted(hm.items(), key=lambda x: x[1], reverse=True))
        res = list(hm.keys())[:k]

        return res
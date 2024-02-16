class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hm = {}

        for num in arr:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        
        for idx, val in enumerate(sorted(hm.values())):
            k = k - val #k -= val
            if k < 0:
                return len(hm) - idx
        return 0
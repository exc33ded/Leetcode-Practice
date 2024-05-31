class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        res = []
        for val, key in hm.items():
            if key == 1:
                res.append(val)
        return res
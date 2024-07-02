class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = {}
        res = []
        for num in nums1:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

        for num in nums2:
            if num in hm:
                if hm[num] == 0:
                    continue
                else:
                    res.append(num)
                    hm[num] -= 1
        return res
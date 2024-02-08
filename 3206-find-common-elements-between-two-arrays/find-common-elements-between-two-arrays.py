class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0] * 2

        for num in nums1:
            if num in nums2:
                res[0] += 1
        
        for num in nums2:
            if num in nums1:
                res[1] += 1

        return res
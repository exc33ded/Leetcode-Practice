class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # a = set(nums1)
        # b = set(nums2)
        # return a.intersection(b)

        x = set(nums1)
        y = set(nums2)
        return list(y-(y-x))
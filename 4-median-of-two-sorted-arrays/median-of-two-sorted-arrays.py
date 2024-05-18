class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = nums1 + nums2
        total.sort()

        if len(total) % 2 != 0:
            return total[len(total)//2]
        else:
            mid = len(total)//2
            f = total[mid]
            l = total[mid - 1]

            med = (f + l) / 2
            return med
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0

        common = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] == nums2[j] :
                common = nums1[i]
                break
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        if common == 0:
            return -1
        return common        
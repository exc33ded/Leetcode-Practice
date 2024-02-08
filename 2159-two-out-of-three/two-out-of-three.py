class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s = set()
        for i in nums1:
            if i in nums2 or i in nums3:
                s.add(i)
        for j in nums2:
            if j in nums1 or j in nums3:
                s.add(j)
        for k in nums3:
            if k in nums1 or k in nums2:
                s.add(k)
        return s
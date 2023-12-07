class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # return sum(i if i % m else -i for i in range(1, n + 1))
        # or

        nums1 = []
        nums2 = []
        for i in range(1, n + 1):
            if i % m == 0:
                nums2.append(i)
            else:
                nums1.append(i)
        return sum(nums1) - sum(nums2)
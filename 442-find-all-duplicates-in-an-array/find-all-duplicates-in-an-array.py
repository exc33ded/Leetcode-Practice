class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hm = {}
        dup = []
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                # hm[num] += 1
                dup.append(num)
        return dup
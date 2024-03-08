class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hm = {}

        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1

        max_ = max(hm.values())

        count = 0
        for val in hm.values():
            if val == max_:
                count += val
        
        return count
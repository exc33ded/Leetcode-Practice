class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1

        sorted_nums = sorted(nums, key=lambda x: (hm[x],-x))
        return sorted_nums
        

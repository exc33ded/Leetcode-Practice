class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        time = len(nums)//3
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        res = []
        for val, times in hm.items():
            if times > time:
               res.append(val)

        return res 
        
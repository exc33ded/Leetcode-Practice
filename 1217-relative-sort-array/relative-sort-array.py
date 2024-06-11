class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hm = {}
        for num in arr2:
            hm[num] = arr2.count(num) - 1
        not_arr = []
        for num in arr1:
            if num in arr2:
                hm[num] += 1
            else:
                not_arr.append(num)

        not_arr.sort()
        res = []

        for idx, val in hm.items():
            res.extend([idx]*val)
        
        res[:] = res[:] + not_arr[:]
        return res
            


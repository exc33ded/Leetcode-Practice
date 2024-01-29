class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        even_arr = []
        odd_arr = []

        for num in nums:
            if num >= 0:
                even_arr.append(num)
            else:
                odd_arr.append(num)
        lst = []
        for i, j in zip(even_arr, odd_arr):
            lst.append(i)
            lst.append(j)

        return lst
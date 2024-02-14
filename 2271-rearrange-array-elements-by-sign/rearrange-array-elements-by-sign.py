class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg_arr = []
        pos_arr = []

        for num in nums:
            if num >= 0:
                pos_arr.append(num)
            else:
                neg_arr.append(num)
        
        lst = []
        for x, y in zip(pos_arr, neg_arr):
            lst.append(x)
            lst.append(y)

        return lst
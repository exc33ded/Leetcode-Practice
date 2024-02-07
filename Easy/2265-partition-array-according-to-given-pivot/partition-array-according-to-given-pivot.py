class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Brute Force?
        lst = []
        for i in nums:
            if i < pivot:
                lst.append(i)
                
        for j in nums:
            if j==pivot:
                lst.append(j)
                
        for k in nums:
            if k>pivot:
                lst.append(k)
                
        return lst
            
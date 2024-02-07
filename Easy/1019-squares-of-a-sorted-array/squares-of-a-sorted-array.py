class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = []
        for num in nums:
            lst.append(pow(num, 2))
        return sorted(lst)
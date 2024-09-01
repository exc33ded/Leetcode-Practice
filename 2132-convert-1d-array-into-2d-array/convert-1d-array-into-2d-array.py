class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # using slicing logic
        res = []
        if len(original) == m*n:
            for i in range(0, len(original), n):
                res.append(original[i:n+i])
        return res
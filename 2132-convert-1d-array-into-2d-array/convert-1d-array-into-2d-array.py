class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        
        res = [[0] * n for _ in range(m)]
        row, col = 0, 0
        for num in original:
            res[row][col] = num
            col += 1
            if col == n:
                col = 0
                row += 1
        return res 
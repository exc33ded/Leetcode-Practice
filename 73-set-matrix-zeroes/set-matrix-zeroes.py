class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = [1]*len(matrix[0])
        rows = [1]*len(matrix)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] == 0 or cols[j] == 0:
                    matrix[i][j] = 0
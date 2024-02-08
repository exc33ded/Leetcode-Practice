class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ## this is brute force
        neg = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    neg += 1

        return neg
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
    
        n = len(matrix) 
        m = len(matrix[0]) 

        TOP = 0
        RIGHT = m - 1
        LEFT = 0
        BOTTOM = n - 1

        while TOP <= BOTTOM and LEFT <= RIGHT:
            for i in range(LEFT, RIGHT+1):
                res.append(matrix[TOP][i])
            TOP += 1 
        
            for i in range(TOP, BOTTOM+1):
                res.append(matrix[i][RIGHT])
            RIGHT -= 1

            if (TOP <= BOTTOM):
                for i in range(RIGHT, LEFT-1, -1):
                    res.append(matrix[BOTTOM][i])
                BOTTOM -= 1
            
            if (LEFT <= RIGHT):
                for i in range(BOTTOM, TOP-1, -1):
                    res.append(matrix[i][LEFT])
                LEFT += 1
        return res
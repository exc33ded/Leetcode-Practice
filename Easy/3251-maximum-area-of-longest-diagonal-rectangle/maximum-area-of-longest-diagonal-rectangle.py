class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        n = len(dimensions)

        maxArea = 0
        maxDiag = 0
       
        for i in range(n):
 
            l, w = dimensions[i]

            currDiag = l**2 + w**2
            if currDiag > maxDiag or (currDiag == maxDiag and l * w > maxArea):
                maxDiag = currDiag
                maxArea = l * w
        return maxArea
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []

        for x, y, r in queries:
            res = 0
            for i, j in points:
                dist = ((x - i)**2 + (y - j)**2)
                if dist <= r**2: # lies inside
                    res += 1
            ans.append(res)
        return ans
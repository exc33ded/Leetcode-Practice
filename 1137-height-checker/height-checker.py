class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected_height = sorted(heights)
        cnt = 0
        for i in range(len(heights)):   
            if expected_height[i] != heights[i]:
                cnt += 1
        return cnt
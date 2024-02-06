class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_height = sorted(heights)
        counter = 0
        for x, y in zip(heights, sort_height):
            if x != y:
                counter += 1

        return counter
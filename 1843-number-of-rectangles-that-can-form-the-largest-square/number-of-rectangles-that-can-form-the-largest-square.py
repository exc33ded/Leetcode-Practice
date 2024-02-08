class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        lst = [0] * len(rectangles)
        i = 0
        for rect in rectangles:
            lst[i] = min(rect)
            i += 1

        max_rect = max(lst)
        count = 0
        for num in lst:
            if num == max_rect:
                count += 1

        return count




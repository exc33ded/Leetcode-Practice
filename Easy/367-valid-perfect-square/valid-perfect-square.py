class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        target = num
        start = 1
        end = num

        if num == 1:
            return True

        while (start <= end):
            mid = start + (end - start)//2

            if mid*mid == target:
                return True
            elif mid*mid > target:
                end = mid - 1
            else:
                start = mid + 1
        return False
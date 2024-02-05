# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        last = n
        res = -1
        while (start <= last):
            mid = start + (last - start)//2
            if isBadVersion(mid):
                res = mid
                last = mid - 1
            else:
                start = mid + 1

        return res
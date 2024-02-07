class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        min_range = -2**31
        max_range = 2**31 - 1
        # if value is 0
        if x == 0:
            return 0
        else:
            # check for negative
            is_negative = x < 0
            x = abs(x)

            while (x > 0):
                rem = x % 10
                res = res*10 + rem
                x = x // 10

            if (res > max_range) or (res < min_range):
                return 0
                
        return -res if is_negative else res
        
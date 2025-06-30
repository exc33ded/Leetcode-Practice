class Solution:
    def reverse(self, x: int) -> int:
        min_range = -2**31
        max_range = 2**31 + 1

        is_negative = x < 0
        x = abs(x)

        rev = 0
        
        if x == 0:
            return 0
        else:
            while (x > 0):
                rem = x % 10
                rev = rev*10 + rem
                x //= 10

        if rev < min_range or rev > max_range:
            return 0

        return -rev if is_negative else rev
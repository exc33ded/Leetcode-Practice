class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time %= (n * 2 - 2)
        return n - abs(n - 1 - time)
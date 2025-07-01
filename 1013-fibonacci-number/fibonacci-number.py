class Solution:
    def fib(self, n: int) -> int:
        def f(n):
            if n == 0 or n == 1:
                return n
            else:
                return f(n-1) + f(n-2)
        return f(n)
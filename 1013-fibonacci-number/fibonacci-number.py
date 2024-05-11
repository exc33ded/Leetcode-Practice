class Solution:
    def fib(self, n: int) -> int:
        @cache
        def f(n):
            if n == 1 or n == 0:
                return n
            return f(n-2)+f(n-1)

        return f(n)
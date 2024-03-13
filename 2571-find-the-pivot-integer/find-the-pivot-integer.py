class Solution:
    def pivotInteger(self, n: int) -> int:
        sum_ = n*(n+1)//2
        pivot = int(sum_**0.5)
        return pivot if pivot*pivot == sum_ else -1 
class Solution:
    def minSteps(self, n: int) -> int:
        res = []
        while n % 2 == 0:
            res.append(2)
            n = n // 2

        for i in range(3, int(math.sqrt(n))+1, 2):
            while n % i == 0:
                res.append(i)
                n = n / i

        if n > 2:
            res.append(n)

        print(res)
        return int(sum(res))
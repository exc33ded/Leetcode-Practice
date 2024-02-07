class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [x for x in range(n+1)]

        def to_binary_one(num):
            res = 0
            while num > 0:
                rem = num % 2
                if rem == 1:
                    res += rem
                num = num // 2
            return res

        for i in range(n+1):
            ans[i] = to_binary_one(ans[i])

        return ans


        

        
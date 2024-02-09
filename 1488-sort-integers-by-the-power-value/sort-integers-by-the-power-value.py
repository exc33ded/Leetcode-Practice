class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def collatz_steps(num):
            steps = 0
            while num != 1:
                if num % 2 == 0:
                    num //= 2
                else:
                    num = 3 * num + 1
                steps += 1
            return steps

        nums_with_steps = [(collatz_steps(num), num) for num in range(lo, hi + 1)]
        nums_with_steps.sort() 
        return nums_with_steps[k - 1][1] 
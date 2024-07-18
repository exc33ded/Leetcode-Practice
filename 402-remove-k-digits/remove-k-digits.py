import sys
sys.set_int_max_str_digits(0)

class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack = []
        for num in nums:
            while k > 0 and stack and stack[-1] > num:
                k -= 1
                stack.pop()
            stack.append(num)
        stack = stack[:len(stack)-k]
        res = "".join(stack)
        return str(int(res)) if res else "0"

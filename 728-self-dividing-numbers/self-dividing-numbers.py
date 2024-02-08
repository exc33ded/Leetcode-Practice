class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right + 1):
            str_num = str(num)
            is_self_dividing = True

            for n in str_num:
                digit = int(n)
                if digit == 0 or num % digit != 0:
                    is_self_dividing = False
                    break

            if is_self_dividing:
                res.append(num)

        return res

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary = ""

        while (n > 0):
            rem = n % 2
            binary += str(rem)
            n = n // 2

        answer = [0] * 2

        for i in range(len(binary)):
            if i % 2 == 0:
                if binary[i] == "1":
                    answer[0] += 1
            else:
                if 1 % 2 != 0:
                    if binary[i] == "1":
                        answer[1] += 1

        return answer
        
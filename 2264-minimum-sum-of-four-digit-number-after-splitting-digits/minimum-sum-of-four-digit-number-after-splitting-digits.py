class Solution:
    def minimumSum(self, num: int) -> int:
        lst = []
        i = 0
        while(num != 0):
            rem = num % 10
            lst.append(rem)
            num = num // 10
            i += 1

        while len(lst) < 4:
            lst.append(0)
            
        lst.sort()
        num1 = int(str(lst[0]) + str(lst[2]))
        num2 = int(str(lst[1]) + str(lst[3]))

        return num1 + num2

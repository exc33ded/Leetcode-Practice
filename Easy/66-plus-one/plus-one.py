class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        sum = 0
        length = len(digits)
        
        for i in range(len(digits)):
            sum = digits[i] * pow(10, length - 1) + sum
            print(sum)
            length -= 1
        print(sum)
        sum = sum + 1

        lst = [int(x) for x in str(sum)]

        return lst

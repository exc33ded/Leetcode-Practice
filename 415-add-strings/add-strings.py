import sys
sys.set_int_max_str_digits(0)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        def str2int(num):
            numDict = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,
                  '6' : 6, '7' : 7, '8' : 8, '9' : 9}
            output = 0
            for d in num:
                output = output * 10 + numDict[d]
            return output
        
        return str(str2int(num1) + str2int(num2)) 
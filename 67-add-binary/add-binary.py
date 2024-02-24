class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        c = a + b
        c = int(str(c),10)
        return "{0:b}".format(int(c))
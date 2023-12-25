class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        lst = [0] * n
        for i in range(n):
            lst[i] = start + 2*i
        
        xor = 0
        for ele in lst:
            xor ^= ele
        
        return xor
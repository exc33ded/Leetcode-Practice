class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        res = []
        for i in range(len(str(low)), len(str(high))+1):
            for j in range(len(s) - i + 1):
                num = int(s[j:j+i])
                if low <= num <= high:
                    res.append(num)
        return res

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if num <= 9:
                res.append(num)
            else:
                temp = []
                while num > 0:
                    rem = num % 10 
                    temp.append(rem)
                    num = num // 10
                res.extend(temp[::-1])

        return res
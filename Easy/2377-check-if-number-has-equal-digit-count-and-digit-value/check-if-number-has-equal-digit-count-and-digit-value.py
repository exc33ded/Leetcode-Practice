class Solution:
    def digitCount(self, num: str) -> bool:
        n=len(num)
        dic={"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}

        for i in num:
            dic[i]+=1

        for i in range(n):
            if int(num[i])!=dic[str(i)]:
                return False
        
        return True

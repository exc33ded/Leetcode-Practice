class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # return num in {6, 28, 496, 8128, 33550336}

        if num == 1:
            return False
        
        sum = 1
        max = math.ceil(math.sqrt(num))
        
        for i in range(2,max):
            if num%i ==0:
                sum+= i + num/i
                
        return num == sum
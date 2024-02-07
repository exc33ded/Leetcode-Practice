class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum = 0
        for i in operations:
            if(i[1]=='+'):
                sum = sum+  1
            else:
                sum = sum - 1  
        return sum
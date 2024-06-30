class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curMin = self.getMin()
        if curMin == None or val < curMin:
            curMin = val
        self.stack.append((val, curMin))
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack)-1][0]

    def getMin(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack)-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
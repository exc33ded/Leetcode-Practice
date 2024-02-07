class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    res = a + b
                if token == "-":
                    res = a - b
                if token == "*":
                    res = a * b
                if token == "/":
                    res = int(float(a)/float(b))
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack.pop()
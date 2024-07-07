class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {
            '(':')', 
            '{':'}',
            '[':']'
            }
        for char in s:
            if char in hm:
                stack.append(char)
            elif stack == [] or hm[stack.pop()] != char:
                return False
        return stack == []
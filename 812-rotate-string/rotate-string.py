class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) == len(goal):
            return goal in s + s
        return False
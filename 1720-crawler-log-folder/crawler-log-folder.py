class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = 0
        for log in logs:
            if log == "../":
                steps = max(steps-1, 0)
            elif log != "./":
                steps += 1
        return steps
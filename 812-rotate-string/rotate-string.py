class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        When the s string is combined (s + s), we get a string which contains the pattern 
        of the rotated inside the merged string so we can check then if the goal string 
        exist there or not.
        """
        if len(s) == len(goal):
            if goal in s + s: 
                return True
        return False
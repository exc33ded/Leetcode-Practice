class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        striping = s.strip()
        spliting = striping.split(" ")
        return len(spliting[-1])
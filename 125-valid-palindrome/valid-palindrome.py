class Solution:
    def isPalindrome(self, s: str) -> bool:
        w = ""
        for word in s:
            if word.isalpha() or word.isnumeric():
                w += word.lower()

        return w == w[::-1]

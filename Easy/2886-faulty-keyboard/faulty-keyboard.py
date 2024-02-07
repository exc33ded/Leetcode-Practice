class Solution:
    def finalString(self, s: str) -> str:
        def rev(st):
            return st[::-1]

        reverse = ""
        for char in s:
            if char == "i":
                reverse = rev(reverse)
            else:
                reverse += char

        return reverse
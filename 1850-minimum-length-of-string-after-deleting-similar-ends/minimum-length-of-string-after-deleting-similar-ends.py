class Solution:
    def minimumLength(self, s: str) -> int:
        left_pointer, right_pointer = 0, len(s) - 1
      
        while left_pointer < right_pointer and s[left_pointer] == s[right_pointer]:
            while left_pointer + 1 < right_pointer and s[left_pointer] == s[left_pointer + 1]:
                left_pointer += 1

            while left_pointer < right_pointer - 1 and s[right_pointer - 1] == s[right_pointer]:
                right_pointer -= 1

            left_pointer, right_pointer = left_pointer + 1, right_pointer - 1
            
        return max(0, right_pointer - left_pointer + 1)
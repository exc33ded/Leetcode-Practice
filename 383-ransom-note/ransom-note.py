class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = {}

        for char in magazine:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1

        for char in ransomNote:
            if char in dictionary and dictionary[char] > 0:
                dictionary[char] -= 1
            else:
                return False
        
        return True
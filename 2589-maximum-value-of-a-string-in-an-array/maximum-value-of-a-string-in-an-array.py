class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_ = 0
        for word in strs:
            if word.isnumeric():
                if max_ < int(word):
                    max_ = int(word)

            else:
                if max_ < len(word):
                    max_ = len(word)
        
        return max_
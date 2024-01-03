class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        split_words = []
      
        for word in words:
            word_parts = word.split(separator)
            for part in word_parts:
                if part: 
                    split_words.append(part)
      
        return split_words
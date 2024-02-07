class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        lst = []
        for i, word in enumerate(words):
            if x in word:
                lst.append(i)
            
        return lst
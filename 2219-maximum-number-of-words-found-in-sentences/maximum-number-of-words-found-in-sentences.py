class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for sentence in sentences:
            if max < sentence.count(" "):
                max = sentence.count(" ")
        return max+1

        
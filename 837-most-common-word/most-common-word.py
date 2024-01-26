class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = paragraph
        ban = set(banned)
        words = re.findall(r'\w+', p.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
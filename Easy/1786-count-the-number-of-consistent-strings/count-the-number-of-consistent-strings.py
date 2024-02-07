class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed = set(allowed)
        for word in words:
            for w in word:
                if w not in allowed:
                    count += 1
                    break
        return len(words) - count

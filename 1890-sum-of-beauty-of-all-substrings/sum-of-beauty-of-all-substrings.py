class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s):
            freq = defaultdict(int)
            freq[ch] += 1
            for j in range(i+1, len(s)):
                freq[s[j]] += 1
                if len(freq) > 1:
                    total += max(freq.values()) - min(freq.values())
        return total
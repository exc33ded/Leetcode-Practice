class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        cnt = Counter()
        for x, y in items1 + items2:
            cnt[x] += y
        return sorted(cnt.items())
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank_map = {}
        for i, val in enumerate(sorted_unique):
            rank_map[val] = i + 1 
        
        rank = []
        for val in arr:
            rank.append(rank_map[val])
        
        return rank
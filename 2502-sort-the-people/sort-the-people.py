class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hm = {}
        for x, y in zip(names, heights):
            hm[y] = x
        
        heights.sort()

        lst = []
        for x in heights:
            lst.append(hm[x])
        return lst[::-1]
        
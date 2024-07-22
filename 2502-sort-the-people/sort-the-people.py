class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hm = {}
        for name,height in zip(names, heights):
            hm[height] = name

        heights.sort()

        res = []
        for x in heights:
            res.append(hm[x])
        return res[::-1]
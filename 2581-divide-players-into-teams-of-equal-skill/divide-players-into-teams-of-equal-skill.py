class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res = []
        l = len(skill)-1
        for s in range(len(skill)//2):
            res.append((skill[s], skill[l], skill[s] + skill[l]))
            l -= 1
        
        sum_ = res[0][2]
        prod = 0

        for i in range(len(res)):
            if res[i][2] != sum_:
                return -1
            else:
                prod += (res[i][1] * res[i][0])
        return prod
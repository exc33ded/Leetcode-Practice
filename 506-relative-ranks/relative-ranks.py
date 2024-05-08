class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        def got(cnt):
            if cnt == 1:
                return "Gold Medal"
            elif cnt == 2:
                return "Silver Medal"
            elif cnt == 3:
                return "Bronze Medal"
            else:
                return f"{cnt}"
        scores = sorted(score)[::-1]
        hm = {}
        cnt = 1
        for sc in scores:
            hm[sc] = got(cnt)
            cnt += 1

        lst = []
        for sc in score:
            lst.append(hm[sc])
        return lst     
        

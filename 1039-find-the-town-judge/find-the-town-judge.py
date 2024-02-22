class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        length = len(trust)
        hm = {}
        for tr in trust:
            if tr[1] not in hm:
                hm[tr[1]] = 1
            else:
                hm[tr[1]] += 1

        max_ = 0
        judge = 0
        for key, val in hm.items():
            if val > max_:
                max_ = val
                judge = key

        if max_ == n - 1 and judge not in [tr[0] for tr in trust]:
            return judge
        return -1

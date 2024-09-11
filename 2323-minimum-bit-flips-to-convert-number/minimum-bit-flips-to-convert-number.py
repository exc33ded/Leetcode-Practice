class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin = format(start, 'b')
        goal_bin = format(goal, 'b')

        max_len = max(len(start_bin), len(goal_bin))

        start_bin = start_bin.zfill(max_len)
        goal_bin = goal_bin.zfill(max_len)
        
        cnt = 0
        for i in range(max_len):
            if start_bin[i] != goal_bin[i]:
                cnt += 1
        return cnt
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        curr_score = max_score = 0

        while (l <= r):
            if tokens[l] <= power:
                power -= tokens[l]
                curr_score += 1
                max_score = max(max_score, curr_score)
                l += 1
            elif curr_score >= 1:
                power += tokens[r]
                curr_score -= 1
                r -= 1
            else:
                break
        return max_score
        
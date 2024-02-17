class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_ = 0
        sum = 0
        for g in gain:
            sum += g
            max_ = max(sum, max_)

        return max_
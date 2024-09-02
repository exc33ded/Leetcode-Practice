class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        for idx, val in enumerate(chalk):
            if k < val:
                return idx
            k -= val
        return -1
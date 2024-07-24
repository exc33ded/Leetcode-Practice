class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []
        for idx, val in enumerate(nums):
            val = str(val)
            mapped_val = 0
            for c in val:
                mapped_val *= 10
                mapped_val += mapping[int(c)]
            pairs.append((mapped_val, idx))

        pairs.sort()

        return [nums[p[1]] for p in pairs]
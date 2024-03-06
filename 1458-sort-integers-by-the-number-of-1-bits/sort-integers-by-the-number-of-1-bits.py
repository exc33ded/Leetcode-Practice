class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def helper_key(num):
            bit_count = bin(num).count("1")
            return (bit_count, num)

        arr.sort(key=helper_key)
        return arr
        
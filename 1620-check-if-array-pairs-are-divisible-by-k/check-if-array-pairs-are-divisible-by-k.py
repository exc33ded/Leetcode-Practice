class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        from collections import defaultdict

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = defaultdict(int)
        
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        
        for remainder in range(1, k // 2 + 1):
            if remainder_count[remainder] != remainder_count[k - remainder]:
                return False
        
        return remainder_count[0] % 2 == 0
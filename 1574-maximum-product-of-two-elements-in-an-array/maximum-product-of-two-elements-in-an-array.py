class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float('-inf')  # Initialize max_product with negative infinity

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): 
                product = (nums[i] - 1) * (nums[j] - 1)
                max_product = max(max_product, product)

        return max_product

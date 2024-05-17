class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(nums: List[int], left: int, right: int) -> bool:
            subarray_length = right - left + 1
            subarray_set = set(nums[left : left + subarray_length])
            smallest, largest = min(subarray_set), max(subarray_set)
            common_diff, remainder = divmod(largest - smallest, subarray_length - 1)
          
            if remainder != 0:
                return False
          
            return all((smallest + i * common_diff) in subarray_set for i in range(subarray_length))
        return [is_arithmetic(nums, left, right) for left, right in zip(l, r)]
